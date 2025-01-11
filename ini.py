#ini
import numpy as np

# Number of Gasoline Components
nGC = 9

# Specific Gravity (SG) in Volume
SG = [0]*nGC
SG[0]  = 0.0     # "C4"    # Butane
SG[1]  = 0.699   # "LN"    # Light Naphtha
SG[2]  = 0.850   # "ISO"   # Isomerated Stream
SG[3]  = 0.790   # "REF"   # Reformated Stream
SG[4]  = 0.785   # "POLY"  # Polymerated Stream
SG[5]  = 0.729   # "HTLCN" # Hydrotreated Light Cracked Naphtha
SG[6]  = 0.790   # "MTBE"  # Methyl terc Butil Ether
SG[7]  = 0.850   # "ETH"   # Ethanol
SG[8]  = 0.790   # "REF2"  # Extra Heavy Naphtha (HN for REF)

# Sulphur Concentration (SUL) in Mass
SUL = [0]*nGC
SUL[0]  = 0.0    # "C4"    # Butane
SUL[1]  = 0.005  # "LN"    # Light Naphtha
SUL[2]  = 0.005  # "ISO"   # Isomerated Stream
SUL[3]  = 0.005  # "REF"   # Reformated Stream
SUL[4]  = 0.002  # "POLY"  # Polymerated Stream
SUL[5]  = 0.005  # "HTLCN" # Hydrotreated Light Cracked Naphtha
SUL[6]  = 0.000  # "MTBE"  # Methyl terc Butil Ether
SUL[7]  = 0.000  # "ETH"   # Ethanol
SUL[8]  = 0.000  # "REF2"  # Extra Heavy Naphtha (HN for REF)

# Reid Vapor Pressure (RVP) in Psi IRVP is the property index of RVP
RVP = [0]*nGC         ; IRVP = [0]*nGC                  
RVP[0]  = 78.0        ; IRVP[0]  = (78.0000)**(1.25)   # "C4"    # Butane 
RVP[1]  = 13.0848     ; IRVP[1]  = (13.0848)**(1.25)   # "LN"    # Light Naphtha 
RVP[2]  = 12.352      ; IRVP[2]  = (12.3520)**(1.25)   # "ISO"   # Isomerated Stream 
RVP[3]  = 9.425       ; IRVP[3]  = (9.42500)**(1.25)   # "REF"   # Reformated Stream 
RVP[4]  = 7.54        ; IRVP[4]  = (7.54000)**(1.25)   # "POLY"  # Polymerated Stream 
RVP[5]  = 7.975       ; IRVP[5]  = (7.97500)**(1.25)   # "HTLCN" # Hydrotreated Light Cracked Naphtha 
RVP[6]  = 2.465       ; IRVP[6]  = (2.46500)**(1.25)   # "MTBE"  # Methyl terc Butil Ether 
RVP[7]  = 10.005      ; IRVP[7]  = (10.0050)**(1.25)   # "ETH"   # Ethanol 
RVP[8]  = 9.425       ; IRVP[8]  = (9.425)**(1.25)     # "REF2"  # Extra Heavy Naphtha (HN for REF)

# Research Octane Number (RON)
RON = [0]*nGC
RON[0]  = 93.8  #"C4"
RON[1]  = 69.1  #"LN"
RON[2]  = 87.0  #"ISO"
RON[3]  = 98.0  #"REF"
RON[4]  = 97.0  #"POLY"
RON[5]  = 83.0  #"HTLCN"
RON[6]  = 116.0 #"MTBE"
RON[7]  = 108.0 #"ETH"
RON[8]  = 98.0  #"REF"

# Motor Octane Number (MON)
MON = [0]*nGC
MON[0]  = 90.0  #"C4"
MON[1]  = 67.1  #"LN"
MON[2]  = 82.0  #"ISO"
MON[3]  = 90.0  #"REF"
MON[4]  = 83.0  #"POLY"
MON[5]  = 82.0  #"HTLCN"
MON[6]  = 101.0 #"MTBE"
MON[7]  = 90.7  #"ETH"
MON[8]  = 90.0  #"REF"

# Aromatic Content (ARO) in Volume
ARO = [0]*nGC
ARO[0]  = 0.0    # "C4"    # Butane
ARO[1]  = 0.001  # "LN"    # Light Naphtha
ARO[2]  = 0.0    # "ISO"   # Isomerated Stream
ARO[3]  = 54.0   # "REF"   # Reformated Stream
ARO[4]  = 0.0    # "POLY"  # Polymerated Stream
ARO[5]  = 25.0   # "HTLCN" # Hydrotreated Light Cracked Naphtha
ARO[6]  = 0.0    # "MTBE"  # Methyl terc Butil Ether
ARO[7]  = 0.0    # "ETH"   # Ethanol
ARO[8]  = 54.0   # "REF2"  # Extra Heavy Naphtha (HN for REF)

# Olefinic Content (OLE) in Volume
OLE = [0]*nGC
OLE[0]  = 0.0   # "C4"    # Butane
OLE[1]  = 0.1   # "LN"    # Light Naphtha
OLE[2]  = 0.0   # "ISO"   # Isomerated Stream
OLE[3]  = 20.0  # "REF"   # Reformated Stream
OLE[4]  = 29.0  # "POLY"  # Polymerated Stream
OLE[5]  = 10.0  # "HTLCN" # Hydrotreated Light Cracked Naphtha
OLE[6]  = 0.0   # "MTBE"  # Methyl terc Butil Ether
OLE[7]  = 0.0   # "ETH"   # Ethanol
OLE[8]  = 20.0  # "REF2"  # Extra Heavy Naphtha (HN for REF)

# Combinatorics of the Problem: (See Figure 3 in the Article)
# 
# 2^1 = 2   scenarios for crude-oil raw materials
# 2^2 = 4   scenarions for crude-oil raw materials +  ATR Route
# 2^3 = 8   scenarions for crude-oil raw materials +  ATR Route + Reformate operational modes
# 2^4 = 16  scenarions for crude-oil raw materials +  ATR Route + Reformate operational modes + Catalytic Cracking operational modes
# 2^5 = 32  scenarions for crude-oil raw materials +  ATR Route + Reformate operational modes + Catalytic Cracking operational modes + ISO[No,Yes]
# 2^6 = 48  scenarions for crude-oil raw materials +  ATR Route + Reformate operational modes + Catalytic Cracking operational modes + POLYM[No,Yes]
# 2^6 = 64  scenarions for crude-oil raw materials +  ATR Route + Reformate operational modes + Catalytic Cracking operational modes + ISO[No,Yes] + POLYM[No,Yes]

crudeFeed = 100 # Kbbl/day
ISO = False #True
POLY = False #True

Stock_LN = 0.0 # LN to be stocked instead of blended gasoline pool (save it to produce higher ON grades of gasoline)

nCrude   = 2   # 2 options of crude-oil
nCDUCut  = 4   # 4 CDU basic gasoline components (C4, LN, HN, ATR)
nATRRoute = 2  # 2 ART Routes (RFCC or FCC) 
nREFMode  = 2  # 2 REF Mode (Low or High RON/MON) 
nCCMode  = 2   # 2 CC (RFCC/FCC) modes (gasoline or diesel)
nCCCut   = 3   # 3 CC basic gasoline components (GAS, LCN, HCN) # HCN is added as an alternative if using a reactor to crack it to gasoline-like stream
 
crudeCut               = [[0 for _ in range(nCDUCut)]  for _ in range(nCrude)]
CCCut                  = [[0 for _ in range(nCCCut)] for _ in range(nCCMode)]
GASYield               = [[[0 for _ in range(nCrude)] for _ in range(nATRRoute)] for _ in range(nCCMode)]
LCNYield               = [[[0 for _ in range(nCrude)] for _ in range(nATRRoute)] for _ in range(nCCMode)]
HCNYield               = [[[0 for _ in range(nCrude)] for _ in range(nATRRoute)] for _ in range(nCCMode)]
REFORYield             = [[0 for _ in range(nCrude)] for _ in range(nREFMode)]
REFOR2Yield             = [[0 for _ in range(nCrude)] for _ in range(nREFMode)]
gasolineProduction     = [[[[0 for _ in range(nCrude)] for _ in range(nATRRoute)] for _ in range(nCCMode)] for _ in range(nREFMode)]

gasolineProductionCDU     = [0 for _ in range(nCrude)]
gasolineProductionISO     = [0 for _ in range(nCrude)]
gasolineProductionREF     = [[0 for _ in range(nCrude)] for _ in range(nREFMode)]
gasolineProductionREF2     = [[0 for _ in range(nCrude)] for _ in range(nREFMode)]
gasolineProductionCC      = [[[0 for _ in range(nCrude)] for _ in range(nATRRoute)] for _ in range(nCCMode)] 
gasolineProductionHTLCN   = [[[0 for _ in range(nCrude)] for _ in range(nATRRoute)] for _ in range(nCCMode)] 
gasolineProductionPOLY    = [[[0 for _ in range(nCrude)] for _ in range(nATRRoute)] for _ in range(nCCMode)] 

#lightCrude =  [1,15,10,20]  # C4,LN,HN,ATR
#heahvyCrude = [0.5,10,5,30] # C4,LN,HN,ATR
crude =  ['lightCrude','heahvyCrude']
crudeCut[0][0] = 1     /100
crudeCut[0][1] = 15    /100
crudeCut[0][2] = 10    /100
crudeCut[0][3] = 20    /100
crudeCut[1][0] = 0.5   /100
crudeCut[1][1] = 10    /100
crudeCut[1][2] = 5     /100
crudeCut[1][3] = 30    /100

VDU      = [0]*2
C4Yield  = [0]*2
LNYield  = [0]*2 
ISOYield = [0]*2 
HNYield  = [0]*2 
ATRYield = [0]*2 

LNStock  = [0]*2 

# 2 options of ATR Route
ATRRoute =  ['RFCC','FCC']
VDU[0] = 1    # RFFC Route ATR = RFCC Feed      
VDU[1] = 0.5  # FCC Routs  FCC = ATR-VR = 0.5 RFCC

# 2 options of Reformate operational modes
REFMode = ['low','high']
#REFModeLowYield  = 92 
#REFModeHighYield = 88 
REFYield = [0]*2
REFYield[0] = 92   /100
REFYield[1] = 88   /100

# 2 options of Catalytic Cracking operational modes
CCMode = ['gasoline','diesel']
CCCut[0][0] = 15  /100  # Gasoline  #GAS
CCCut[0][1] = 50 /100   # Gasoline  #LCN
CCCut[0][2] = 10 /100   # Gasoline  #HCN
CCCut[1][0] = 8  /100   # Diesel    #GAS
CCCut[1][1] = 35 /100   # Diesel    #LCN
CCCut[1][2] = 20 /100   # Diesel    #HCN

# 2^4 = 16  scenarions for crude-oil raw materials +  ATR Route + Reformate operational modes + Catalytic Cracking operational modes
nsc = 16
JUMP2 = int(nsc/2)
JUMP1 = int(nsc/2)
MTBE =[0]*nsc
ETH=[0]*nsc
REF2 =[0]*nsc
gasolineSC      = [0]*nsc
gasolineSCCDU   = [0]*nsc
gasolineSCCC    = [0]*nsc
gasolineSCREF   = [0]*nsc
gasolineSCISO  = [0]*nsc
gasolineSCPOLY  = [0]*nsc
gasolineSCHTLCN  = [0]*nsc
gasolineSCMTBE = [0]*nsc
gasolineSCETH  = [0]*nsc
gasolineSCREF2 = [0]*nsc
gasolineSCCCJUMP21    = [0]*JUMP2
gasolineSCREFJUMP11   = [0]*JUMP1
gasolineSCCCJUMPRFCC   = [0]*JUMP1
gasolineSCCCJUMPFCC    = [0]*JUMP2
gasolineSCCCJUMP22    = [0]*JUMP2
gasolineSCREFJUMP12   = [0]*JUMP1
gasolineSCCDUCC = [0]*nsc
C4SC            = [0]*nsc
LNSC            = [0]*nsc
REFSC           = [0]*nsc
HTLCNSC         = [0]*nsc
ISOSC           = [0]*nsc
POLYSC          = [0]*nsc
MTBESC          = [0]*nsc
ETHSC           = [0]*nsc
REF2SC           = [0]*nsc

gasolineSCRONV = [0]*nsc
gasolineSCMONV = [0]*nsc
gasolineSCRON  = [0]*nsc
gasolineSCMON  = [0]*nsc
gasolineSCRVP  = [0]*nsc
gasolineSCARO  = [0]*nsc
gasolineSCARO2 = [0]*nsc
gasolineSCOLE  = [0]*nsc
gasolineSCSG   = [0]*nsc
gasolineSCSUL  = [0]*nsc

# modifications in qualities on CC and REF modes

RONCC = RON[5]
MONCC = RON[5]

RONREF = RON[3]
MONREF = MON[3]

ONREF = [0]*nsc
ONCC = [0]*nsc
ONHT = [0]*nsc

ONREF[2-1]  = 1.5     # REF mode high-ON in even (2, 4, 6, ...) scenarios but represented with i-1 in python vectors
ONREF[4-1]  = 1.5     # REF mode high-ON in even (2, 4, 6, ...) scenarios but represented with i-1 in python vectors
ONREF[6-1]  = 1.5     # REF mode high-ON in even (2, 4, 6, ...) scenarios but represented with i-1 in python vectors
ONREF[8-1]  = 1.5     # REF mode high-ON in even (2, 4, 6, ...) scenarios but represented with i-1 in python vectors
ONREF[10-1] = 1.5     # REF mode high-ON in even (2, 4, 6, ...) scenarios but represented with i-1 in python vectors
ONREF[12-1] = 1.5     # REF mode high-ON in even (2, 4, 6, ...) scenarios but represented with i-1 in python vectors
ONREF[14-1] = 1.5     # REF mode high-ON in even (2, 4, 6, ...) scenarios but represented with i-1 in python vectors
ONREF[16-1] = 1.5     # REF mode high-ON in even (2, 4, 6, ...) scenarios but represented with i-1 in python vectors

ONREF[1-1]  = -1.5    # REF mode low-ON in odd (1, 3, 5, ...) scenarios but represented with i-1 in python vector
ONREF[3-1]  = -1.5    # REF mode low-ON in odd (1, 3, 5, ...) scenarios but represented with i-1 in python vector
ONREF[5-1]  = -1.5    # REF mode low-ON in odd (1, 3, 5, ...) scenarios but represented with i-1 in python vector
ONREF[7-1]  = -1.5    # REF mode low-ON in odd (1, 3, 5, ...) scenarios but represented with i-1 in python vector
ONREF[9-1]  = -1.5    # REF mode low-ON in odd (1, 3, 5, ...) scenarios but represented with i-1 in python vector
ONREF[11-1] = -1.5    # REF mode low-ON in odd (1, 3, 5, ...) scenarios but represented with i-1 in python vector
ONREF[13-1] = -1.5    # REF mode low-ON in odd (1, 3, 5, ...) scenarios but represented with i-1 in python vector
ONREF[15-1] = -1.5    # REF mode low-ON in odd (1, 3, 5, ...) scenarios but represented with i-1 in python vector

ONCC[1-1]  = 0.5 # CC mode in gasoline in scenarions 1-2, 5-6, 9-10, 13-14
ONCC[2-1]  = 0.5
ONCC[5-1]  = 0.5
ONCC[6-1]  = 0.5
ONCC[9-1]  = 0.5
ONCC[10-1] = 0.5
ONCC[13-1] = 0.5
ONCC[14-1] = 0.5

ONCC[3-1]  = -0.5 # CC mode in diesel in scenarions 3-4, 7-8, 11-12, 15-16
ONCC[4-1]  = -0.5
ONCC[7-1]  = -0.5
ONCC[8-1]  = -0.5
ONCC[11-1] = -0.5
ONCC[12-1] = -0.5
ONCC[15-1] = -0.5
ONCC[16-1] = -0.5

ONHT[1-1]  = -0.5  # HT reduction the same for all scenarios
ONHT[2-1]  = -0.5
ONHT[3-1]  = -0.5
ONHT[4-1]  = -0.5
ONHT[5-1]  = -0.5
ONHT[6-1]  = -0.5
ONHT[7-1]  = -0.5
ONHT[8-1]  = -0.5
ONHT[9-1]  = -0.5 
ONHT[10-1] = -0.5
ONHT[11-1] = -0.5
ONHT[12-1] = -0.5
ONHT[13-1] = -0.5
ONHT[14-1] = -0.5
ONHT[15-1] = -0.5
ONHT[16-1] = -0.5
# 