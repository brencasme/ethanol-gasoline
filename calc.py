from re import X
from main import VDU,C4Yield,LNYield,HNYield,ATRYield,REFYield,ISOYield,LNStock 
from main import nCrude,nCDUCut,nATRRoute,nREFMode,nCCMode,nCCCut 
from main import crudeCut,CCCut,GASYield,LCNYield,HCNYield,REFORYield,gasolineProduction,gasolineProductionCDU,gasolineProductionISO,gasolineProductionREF,gasolineProductionCC,gasolineProductionHTLCN,gasolineProductionPOLY
from main import SG,SUL,RVP,IRVP,RON,MON,ARO,OLE
from main import gasolineSC,gasolineSCCDU,gasolineSCISO,gasolineSCCC,gasolineSCPOLY,gasolineSCREF,gasolineSCHTLCN,gasolineSCCDUCC,C4SC,LNSC,REFSC,HTLCNSC,ISOSC,POLYSC,MTBESC,ETHSC,REF2SC
from main import gasolineSCRONV,gasolineSCMONV,gasolineSCRON,gasolineSCMON,gasolineSCRVP,gasolineSCARO,gasolineSCARO2,gasolineSCOLE,gasolineSCSG,gasolineSCSUL
#from main import gasolineMTBE,gasolineETH,gasolineREF2
from main import nsc,nGC, plt,gasolineSCREFJUMP11,gasolineSCCCJUMP21,gasolineSCREFJUMP12,gasolineSCCCJUMP22,JUMP1,JUMP2,gasolineSCCCJUMPRFCC,gasolineSCCCJUMPFCC
import matplotlib.pyplot as plt
import numpy as np
import ini

# Selections Computing all scnenarios
# 1st Crude-Oil
# 2nd ATR Route
# 3rd CC Mode
# 4th REF Mode 

count = 0
counter = 0


# The Pure Petroleum-Refined Gasoline (PPRG) or the endogenous variavles + the 3 SC or exogenous variables (MTBE+ETH+REF2)

# Calculation of the Pure Petroleum-Refined Gasoline Productions (Yields)

# Crude Distillation Unit Yields (C4, LN, HN, ATR)
for i in range(nCrude):

   C4Yield[i]  = crudeFeed * crudeCut[i][0]
   LNYield[i]  = crudeFeed * crudeCut[i][1]
   HNYield[i]  = crudeFeed * crudeCut[i][2]
   ATRYield[i] = crudeFeed * crudeCut[i][3]
   
   if ISO == True:
     # ISO
     ISOYield[i] = LNYield[i] * ISOFeed 
     LNYield[i] = LNYield[i] - ISOYield[i]
   else:     
     ISOYield[i] = 0
 
   # LN Stocks and for gasoline pool
   # 
   LNStock[i] = Stock_LN*LNYield[i]
   LNYield[i] = (LNYield[i]-LNStock[i])

   gasolineProductionISO[i] = ISOYield[i]
   gasolineProductionCDU[i] = C4Yield[i] + LNYield[i]

   # ATR Route (RFCC or FCC)
   for k in range(nATRRoute):
       
       # CC mode (Gasoline or Diesel)
       for l in range(nCCMode):
          GASYield[i][k][l] = ATRYield[i]*VDU[k]*CCCut[l][0]
          LCNYield[i][k][l] = ATRYield[i]*VDU[k]*CCCut[l][1]
          
          # Light Cracked Naphtha (LCN) produced and GASES into POLY

          gasolineProductionCC[i][k][l] =  LCNYield[i][k][l]
          gasolineProductionHTLCN[i][k][l] =  LCNYield[i][k][l]*HTLCNred
          
          if POLY == True:
             gasolineProductionPOLY[i][k][l] =  GASYield[i][k][l]*POLYFeed 
          else:
             gasolineProductionPOLY[i][k][l] =  0
                     
          # REF mode
          for j in range(nREFMode):
              REFORYield[i][j] = HNYield[i]*REFYield[j] 
              REFOR2Yield[i][j] = REF2[0]*REFYield[j]  
              gasolineProductionREF[i][j] =   REFORYield[i][j] 
              gasolineProductionREF2[i][j] =  REFOR2Yield[i][j]      
 
              # Save Gasoline Productions for each Scenario                                
              count = count + 1
              C4SC[count-1]    = C4Yield[i]
              LNSC[count-1]    = LNYield[i]
              ISOSC[count-1]   = ISOYield[i]
              REFSC[count-1]   = REFORYield[i][j] 
              if POLY == True:
                POLYSC[count-1]  = GASYield[i][k][l]*POLYFeed
              else:
                POLYSC[count-1]  = 0
              HTLCNSC[count-1] = LCNYield[i][k][l]*HTLCNred
              MTBESC[count-1]  = MTBE[0]
              ETHSC[count-1]   = ETH[0]
              REF2SC[count-1]  = REFOR2Yield[i][j] 

              gasolineSC[count-1]      = gasolineProductionCDU[i]+gasolineProductionISO[i]+gasolineProductionREF[i][j]+gasolineProductionHTLCN[i][k][l]+gasolineProductionPOLY[i][k][l] + gasolineProductionREF2[i][j] + MTBE[0] + ETH[0]
              #gasolineSC[count-1]      = gasolineProductionCDU[i]+gasolineProductionISO[i]+gasolineProductionREF[i][j]+gasolineProductionCC[i][k][l]+gasolineProductionPOLY[i][k][l]+gasolineProductionMTBE[s]+gasolineProductionETH[s]#+gasolineProductionREF2
              gasolineSCCDU[count-1]   = gasolineProductionCDU[i]
              gasolineSCISO[count-1]   = gasolineProductionISO[i]
              gasolineSCCDUCC[count-1] = gasolineProductionCDU[i]+gasolineProductionCC[i][k][l]
              gasolineSCCC[count-1]    = gasolineProductionCC[i][k][l]
              gasolineSCHTLCN[count-1] = gasolineProductionHTLCN[i][k][l] 
              gasolineSCPOLY[count-1]  = gasolineProductionPOLY[i][k][l] 
              gasolineSCREF[count-1]   = gasolineProductionREF[i][j] + gasolineProductionREF2[i][j]

# Final Check to see if (every scenario created in the 4-fold do-loop) the produced gasoline-like streams 
# are saved in the vector for the quality calculation
# Selections Computing all scnenarios
# 1st Crude-Oil
# 2nd ATR Route
# 3rd CC Mode
# 4th REF Mode 
               
if count == nsc: 
    print('Calc.py OK! Scenarios checked!')
else:
    print('Scenarios Construction Got an Error, Check Again!!!!!')

# Calculation of the Pure Petroleum-Refined Gasoline Properties                 

volumeComp = [0]*nsc
totalVolume = [0]*nsc
totalMass = [0]*nsc
Jv = [0]*nsc
ON=[0]*nsc
J = [0]*nGC
gasolineBlendSG = [0]*nsc 
gasolineBlendIRVP = [0]*nsc 
gasolineBlendSUL = [0]*nsc 
gasolineBlendRON  = [0]*nsc
gasolineBlendMON  = [0]*nsc
gasolineBlendRONV  = [0]*nsc
gasolineBlendMONV  = [0]*nsc
gasolineBlendARO  = [0]*nsc
gasolineBlendOLE  = [0]*nsc
gasolineBlendARO2 = [0]*nsc

volumeComp = [[0 for _ in range(nsc)] for _ in range(nGC)]
RONS = [[0 for _ in range(nGC)] for _ in range(nsc)]
MONS = [[0 for _ in range(nGC)] for _ in range(nsc)]
for s in range(nsc):
    volumeComp[0][s] = C4SC[s]
    volumeComp[1][s] = LNSC[s]
    volumeComp[2][s] = ISOSC[s]
    volumeComp[3][s] = REFSC[s]
    volumeComp[4][s] = POLYSC[s]
    volumeComp[5][s] = HTLCNSC[s]
    volumeComp[6][s] = MTBESC[s]
    volumeComp[7][s] = ETHSC[s]
    volumeComp[8][s] = REF2SC[s]

for s in range(nsc):
   
    RON[5] = RONCC + ONCC[s]     +  ONHT[s]  
    MON[5] = MONCC + ONCC[s]/2   +  ONHT[s]/2
  
    RON[3] = RONREF + ONREF[s]   
    MON[3] = MONREF + ONREF[s]/2 

    for i in range(nGC):
        #Volume-Based (SG, RONV, MONV, AROV, OLEV, ARO^2V)
        #totalVolume[s]        = totalVolume[s]       + volumeComp[i][s]
        totalVolume[s]        += volumeComp[i][s]

        gasolineBlendSG[s]    = gasolineBlendSG[s]   + SG[i]*volumeComp[i][s]
        gasolineBlendIRVP[s]  = gasolineBlendIRVP[s] + IRVP[i]*volumeComp[i][s]
        gasolineBlendRONV[s]  = gasolineBlendRONV[s] + RON[i]*volumeComp[i][s]
        gasolineBlendMONV[s]  = gasolineBlendMONV[s] + MON[i]*volumeComp[i][s]
        gasolineBlendARO[s]   = gasolineBlendARO[s]  + ARO[i]*volumeComp[i][s]
        gasolineBlendOLE[s]   = gasolineBlendOLE[s]  + OLE[i]*volumeComp[i][s]
        gasolineBlendARO2[s]  = gasolineBlendARO2[s] + ARO[i]*ARO[i]*volumeComp[i][s]

        #Mass-Based (SUL)
        totalMass[s]  = totalMass[s]  + volumeComp[i][s]*SG[i]
        gasolineBlendSUL[s]    = gasolineBlendSUL[s]     + SG[i]*SUL[i]*volumeComp[i][s]

    gasolineSCSG[s]    = gasolineBlendSG[s]/totalVolume[s]
    gasolineSCRVP[s]   = (gasolineBlendIRVP[s]/totalVolume[s])**(1/1.25)
    gasolineSCSUL[s]   = gasolineBlendSUL[s]/totalMass[s]
    gasolineSCRONV[s]  = gasolineBlendRONV[s]/totalVolume[s] 
    gasolineSCMONV[s]  = gasolineBlendMONV[s]/totalVolume[s] 
    gasolineSCARO[s]   = gasolineBlendARO[s]/totalVolume[s] 
    gasolineSCOLE[s]   = gasolineBlendOLE[s]/totalVolume[s]  
    gasolineSCARO2[s]  = gasolineBlendARO2[s]/totalVolume[s]

a = 0.01929
b = 0.00043
c = 0.00144
d = 0.00165
e = 0.0445
f = 0.00081
g = 0.000000645

j11 = [0,2,4,6,8,10,12,14]
j12 = [1,3,5,7,9,11,13,16]

j21 = [0,1,4,5,8,9,12,13] 
j22 = [2,3,6,7,10,11,14,15] 

for s in range(nsc):
   
    RON[5] = RONCC + ONCC[s]    +  ONHT[s]  
    MON[5] = MONCC + ONCC[s]/2  +  ONHT[s]/2
    #
    RON[3] = RONREF + ONREF[s]
    MON[3] = MONREF + ONREF[s]/2

    for i in range(nGC):
        #Ethyl (RON, MON)
        Jv[s] = gasolineSCRONV[s] - gasolineSCMONV[s]
        J[i] = RON[i] - MON[i]
        RONS[s][i] = RON[i]+a*((RON[i]-gasolineSCRONV[s])*(J[i]-Jv[s]))+b*(ARO[i]-gasolineSCARO[s])**2+c*(OLE[i]-gasolineSCOLE[s])**2+d*(((ARO[i]-gasolineSCARO[s])*(OLE[i]-gasolineSCOLE[s])))
        MONS[s][i] = MON[i]+e*((MON[i]-gasolineSCMONV[s])*(J[i]-Jv[s]))+f*(ARO[i]-gasolineSCARO[s])**2+g*((2*(OLE[i]-gasolineSCOLE[s])**2*(gasolineSCARO2[s]-gasolineSCARO[s]**2))-(gasolineSCARO2[s]-gasolineSCARO[s]**2)**2)

        gasolineBlendRON[s]  = gasolineBlendRON[s]   + RONS[s][i]*volumeComp[i][s]
        gasolineBlendMON[s]  = gasolineBlendMON[s]   + MONS[s][i]*volumeComp[i][s]


    gasolineSCRON[s]  = gasolineBlendRON[s]/totalVolume[s] 
    gasolineSCMON[s]  = gasolineBlendMON[s]/totalVolume[s] 

SC   = [1 for _ in range(nsc)]
SCJUMP11  = [1 for _ in range(JUMP1)]
SCJUMP12  = [1 for _ in range(JUMP1)]
SCJUMP21  = [1 for _ in range(JUMP2)]
SCJUMP22  = [1 for _ in range(JUMP2)]
SCJUMPRFCC  = [1 for _ in range(JUMP2)]
SCJUMPFCC  = [1 for _ in range(JUMP2)]
SC1Y = [0 for _ in range(4)]
SC2Y = [0 for _ in range(4)]
SC3Y = [0 for _ in range(4)]
SC4Y = [0 for _ in range(4)]
SC1  = [0 for _ in range(4)]
SC2  = [0 for _ in range(4)]
SC3  = [0 for _ in range(4)]
SC4  = [0 for _ in range(4)]
SCR1 = [0 for _ in range(4)]
SCR2 = [0 for _ in range(4)]
SCR3 = [0 for _ in range(4)]
SCR4 = [0 for _ in range(4)]
gasolineProductionSC = [0 for _ in range(nsc)]
gasolineSCR1 = [0 for _ in range(4)]
gasolineSCR2 = [0 for _ in range(4)]
gasolineSCR3 = [0 for _ in range(4)]
gasolineSCR4 = [0 for _ in range(4)]
scenario = 0

for i in range(nsc):
   SC[i] = SC[i]*i + 1

pacePlot = 4
   
minYield1 = (gasolineSC[3]+gasolineSC[4])/2 + 0.5
r1 = (minYield1 - 0) / (pacePlot-1)
minYield2 = (gasolineSC[7]+gasolineSC[8])/2 + 0.5
r2 = (minYield2 - 0) / (pacePlot-1)
minYield3 = (gasolineSC[11]+gasolineSC[12])/2
r3 = (minYield3 - 0) / (pacePlot-1)
#minYield4 = (gasolineSC[14]+gasolineSC[15])/2
#r4 = (minYield4 - 0) / (pacePlot-1)

for i in range(0*pacePlot,1*pacePlot):
   SC1Y[i] = gasolineSC[i] 
   SC1[i] = i+1 
   SCR1[i] = pacePlot+0.5
   gasolineSCR1[i]= r1*(i-0.5/r1)

for i in range(1*pacePlot,2*pacePlot):
   SC2Y[i-pacePlot] = gasolineSC[i] 
   SC2[i-pacePlot] = i+1 
   SCR2[i-pacePlot] = pacePlot*2+0.5
   gasolineSCR2[i-pacePlot]= r2*(i-pacePlot-0.5/r2)

for i in range(2*pacePlot,3*pacePlot):
   SC3Y[i-8] = gasolineSC[i] 
   SC3[i-8] = i+1
   SCR3[i-8] = pacePlot*3+0.5
   gasolineSCR3[i-8]= r3*(i-2*pacePlot-0.5/r3)

for i in range (JUMP1):
        
    SCJUMP11[i] = SC[i*2]
    SCJUMP12[i] = SC[i*2+1]
    gasolineSCREFJUMP11[i] = gasolineSCREF[i*2]
    gasolineSCREFJUMP12[i] = gasolineSCREF[i*2+1]
count = 0 
ii = 0
jj=0
for i in range (JUMP2):
    if ii == 2:
       jj=jj+2
       ii=0
    SCJUMP21[i] = SC[i+jj]
    SCJUMP22[i] = SC[i+jj+2]
    gasolineSCCCJUMP21[i] = gasolineSCCC[i+jj]
    gasolineSCCCJUMP22[i] = gasolineSCCC[i+jj+2]
    ii=ii+1

x1=[1,2,3,4]
y1=[gasolineSCCC[0],gasolineSCCC[1],gasolineSCCC[2],gasolineSCCC[3]]
x12=[5,6,7,8]
y12=[gasolineSCCC[4],gasolineSCCC[5],gasolineSCCC[6],gasolineSCCC[7]]

x2=[9,10,11,12]
y2=[gasolineSCCC[8],gasolineSCCC[9],gasolineSCCC[10],gasolineSCCC[11]]

x22=[13,14,15,16]
y22=[gasolineSCCC[12],gasolineSCCC[13],gasolineSCCC[14],gasolineSCCC[15]]

xl=[1,2,3,4,5,6,7,8]
yl=[gasolineSCCDU[0],gasolineSCCDU[1],gasolineSCCDU[2],gasolineSCCDU[3],gasolineSCCDU[4],gasolineSCCDU[5],gasolineSCCDU[6],gasolineSCCDU[7]]

xh=[9,10,11,12,13,14,15,16]
yh=[gasolineSCCDU[8],gasolineSCCDU[9],gasolineSCCDU[10],gasolineSCCDU[11],gasolineSCCDU[12],gasolineSCCDU[13],gasolineSCCDU[14],gasolineSCCDU[15]]

xll=[1,2,3,4,5,6,7,8]
yll=[gasolineSCREF[0],gasolineSCREF[1],gasolineSCREF[2],gasolineSCREF[3],gasolineSCREF[4],gasolineSCREF[5],gasolineSCREF[6],gasolineSCREF[7]]

xhh=[9,10,11,12,13,14,15,16]
yhh=[gasolineSCREF[8],gasolineSCREF[9],gasolineSCREF[10],gasolineSCREF[11],gasolineSCREF[12],gasolineSCREF[13],gasolineSCREF[14],gasolineSCREF[15]]

arrYield = np.array(gasolineSC)
arrRON   = np.array(gasolineSCRON)

arrYieldLight = [0]*int(nsc/2)
arrRONLight = [0]*int(nsc/2)

arrYieldHeavy = [0]*int(nsc/2)
arrRONHeavy = [0]*int(nsc/2)

arrYieldLightRFCC = [0]*int(nsc/4)
arrRONLightRFCC = [0]*int(nsc/4)

arrYieldHeavyRFCC = [0]*int(nsc/4)
arrRONHeavyRFCC = [0]*int(nsc/4)

arrYieldLightFCC = [0]*int(nsc/4)
arrRONLightFCC = [0]*int(nsc/4)

arrYieldHeavyFCC = [0]*int(nsc/4)
arrRONHeavyFCC = [0]*int(nsc/4)

t = np.arange(1,17,1)
t1 = np.arange(1,5,1)
t2 = np.arange(5,9,1)

t3 = np.arange(9,13,1)
t4 = np.arange(13,17,1)

for i in range(0,int(nsc/4)):

    arrYieldLightRFCC[i] =  gasolineSC[i]
    arrRONLightRFCC[i] =    gasolineSCRON[i]
    arrYieldLightFCC[i] =  gasolineSC[i+int(nsc/4)]
    arrRONLightFCC[i] =    gasolineSCRON[i+int(nsc/4)]
    arrYieldHeavyRFCC[i] =  gasolineSC[i+int(2*nsc/4)]
    arrRONHeavyRFCC[i] =    gasolineSCRON[i+int(2*nsc/4)]
    arrYieldHeavyFCC[i] =  gasolineSC[i+int(3*nsc/4)]
    arrRONHeavyFCC[i] =    gasolineSCRON[i+int(3*nsc/4)]

