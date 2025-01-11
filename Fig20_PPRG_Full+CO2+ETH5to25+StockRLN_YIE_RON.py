#### Fig19: CO2 reduction by PPRG-Full + stock_RLN (when hits ARO at 25%) + ETH 5% to 25%: stock remaing LN (considering 30% divert to ISO)
import matplotlib.pyplot as plt
# data initialization
exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/ini.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/ini.py','exec'))

fig,ax1 = plt.subplots()
fig.set_size_inches(9.0,9.0)

ax1.set_xlabel('Scenarios', fontsize=13)
ax1.set_ylabel('CO2 in Kton (   )', fontsize=13)
ax1.tick_params(axis='y')

color = 'tab:brown'

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylabel('CO2 in Kg/L (---)', fontsize=13)  # we already handled the x-label with ax1
ax2.tick_params(axis='y')

color = 'tab:red'

ISO = True
POLY = True

#Ratio ISO-LN and POLY-GASES 
ISOFeed  = 0.30 # = 0 to exclude it
POLYFeed = 0.50 # = 0 to exclude it
HTLCNred = 0.98 # = 1 to exclude it
Stock_LN = 0.0

ECO2 = 8887 # grams CO2 / Gallon
# 1 Barrels = 42 Gallons
ECO2B = 8887 * 42 / 1000 # (373.254 kg CO2 per barrel) = (2.347697028243671923596159051577 kg CO2 per liter)
# 1 barrel = 158.987295 liter


exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))

gasolineSCCO2 = [0]*nsc
gasolineSCCO2a = [ECO2B]*nsc

for f in range(nsc):
    gasolineSCCO2[f] = gasolineSC[f]*ECO2B * 1000 # gasolineSC in KBPD and gasolineSCCO2 in kg
    gasolineSCCO2[f] = gasolineSCCO2[f] / 1000 / 1000 # gasolineSC in KBPD and gasolineSCCO2 in Kton
    gasolineSCCO2a[f] = gasolineSCCO2[f] / gasolineSC[f] * 1000/ 158.987295 # Kton / KBPD = ton / BPD = 1000 Kg / 158.987295 L 


ax1.plot(SC,gasolineSCCO2,color='green', label='Full PPRG')
ax2.plot(SC,gasolineSCCO2a,color='green', label='Full PPRG', linestyle='dashed')
#ETH = True

# Supply Chain (SC) or Exogenous Variables

MTBE_in_Gasoline = 0/100  ; ETH_in_Gasoline  = 5/100
REF2_in_Gasoline = 0/100 
total  = MTBE_in_Gasoline + ETH_in_Gasoline + REF2_in_Gasoline

for s in range(0,nsc):
    MTBE[s] = (1+total)*gasolineSC[s]*MTBE_in_Gasoline 
    ETH[s]  = (1+total)*gasolineSC[s]*ETH_in_Gasoline  
    REF2[s] = (1+total)*gasolineSC[s]*REF2_in_Gasoline    


Stock_LN = 0.80

exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))


for f in range(nsc):
    gasolineSCCO2[f] = gasolineSC[f]*(1-ETH_in_Gasoline)*ECO2B * 1000 # gasolineSC in KBPD and gasolineSCCO2 in kg
    gasolineSCCO2[f] = gasolineSCCO2[f] / 1000/ 1000 # gasolineSC in KBPD and gasolineSCCO2 in Kton
    gasolineSCCO2a[f] = gasolineSCCO2[f] / gasolineSC[f] * 1000/ 158.987295 # Kton / KBPD = ton / BPD = 1000 Kg / 158.987295 L 

ax1.plot(SC,gasolineSCCO2,color='green',label='80% StockRLN + ETH 5%', marker=3)
ax2.plot(SC,gasolineSCCO2a,color='green', label='80% StockRLN + ETH 5%', linestyle='dashed',  marker=3)

# Supply Chain (SC) or Exogenous Variables

MTBE_in_Gasoline = 0/100  ; ETH_in_Gasoline  = 10/100
REF2_in_Gasoline = 0/100 
total  = MTBE_in_Gasoline + ETH_in_Gasoline + REF2_in_Gasoline

for s in range(0,nsc):
    MTBE[s] = (1+total)*gasolineSC[s]*MTBE_in_Gasoline 
    ETH[s]  = (1+total)*gasolineSC[s]*ETH_in_Gasoline  
    REF2[s] = (1+total)*gasolineSC[s]*REF2_in_Gasoline    


Stock_LN = 0.90

exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))


for f in range(nsc):
    gasolineSCCO2[f] = gasolineSC[f]*(1-ETH_in_Gasoline)*ECO2B * 1000 # gasolineSC in KBPD and gasolineSCCO2 in kg
    gasolineSCCO2[f] = gasolineSCCO2[f] / 1000/ 1000 # gasolineSC in KBPD and gasolineSCCO2 in Kton
    gasolineSCCO2a[f] = gasolineSCCO2[f] / gasolineSC[f]  * 1000/ 158.987295 # Kton / KBPD = ton / BPD = 1000 Kg / 158.987295 L 
    
ax1.plot(SC,gasolineSCCO2,color='green',label='90% StockRLN + ETH 10%', marker=2)
ax2.plot(SC,gasolineSCCO2a,color='green', label='90% StockRLN + ETH 10%', linestyle='dashed', marker=2)


# Supply Chain (SC) or Exogenous Variables

MTBE_in_Gasoline = 0/100  ; ETH_in_Gasoline  = 15/100
REF2_in_Gasoline = 0/100 
total  = MTBE_in_Gasoline + ETH_in_Gasoline + REF2_in_Gasoline

for s in range(0,nsc):
    MTBE[s] = (1+total)*gasolineSC[s]*MTBE_in_Gasoline 
    ETH[s]  = (1+total)*gasolineSC[s]*ETH_in_Gasoline  
    REF2[s] = (1+total)*gasolineSC[s]*REF2_in_Gasoline    


Stock_LN = 1.0

exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))

for f in range(nsc):
    gasolineSCCO2[f] = gasolineSC[f]*(1-ETH_in_Gasoline)*ECO2B * 1000 # gasolineSC in KBPD and gasolineSCCO2 in kg
    gasolineSCCO2[f] = gasolineSCCO2[f] / 1000/ 1000 # gasolineSC in KBPD and gasolineSCCO2 in Kton
    gasolineSCCO2a[f] = gasolineSCCO2[f] / gasolineSC[f] * 1000/ 158.987295 # Kton / KBPD = ton / BPD = 1000 Kg / 158.987295 L  
    

ax1.plot(SC,gasolineSCCO2,color='green',label='100% StockRLN + ETH 15%', marker=4)
ax2.plot(SC,gasolineSCCO2a,color='green',label='100% StockRLN + ETH 15%', linestyle='dashed', marker=4)

# Supply Chain (SC) or Exogenous Variables

MTBE_in_Gasoline = 0/100  ; ETH_in_Gasoline  = 20/100
REF2_in_Gasoline = 0/100 
total  = MTBE_in_Gasoline + ETH_in_Gasoline + REF2_in_Gasoline

for s in range(0,nsc):
    MTBE[s] = (1+total)*gasolineSC[s]*MTBE_in_Gasoline 
    ETH[s]  = (1+total)*gasolineSC[s]*ETH_in_Gasoline  
    REF2[s] = (1+total)*gasolineSC[s]*REF2_in_Gasoline    


Stock_LN = 1.0

exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))

for f in range(nsc):
    gasolineSCCO2[f] = gasolineSC[f]*(1-ETH_in_Gasoline)*ECO2B * 1000 # gasolineSC in KBPD and gasolineSCCO2 in kg
    gasolineSCCO2[f] = gasolineSCCO2[f] / 1000/ 1000 # gasolineSC in KBPD and gasolineSCCO2 in Kton
    gasolineSCCO2a[f] = gasolineSCCO2[f] / gasolineSC[f] * 1000/ 158.987295 # Kton / KBPD = ton / BPD = 1000 Kg / 158.987295 L  

ax1.plot(SC,gasolineSCCO2,color='green',label='100% StockRLN + ETH 20%', marker=5)
ax2.plot(SC,gasolineSCCO2a,color='green',label='100% StockRLN + ETH 20%', linestyle='dashed', marker=5)

# Supply Chain (SC) or Exogenous Variables

MTBE_in_Gasoline = 0/100  ; ETH_in_Gasoline  = 25/100
REF2_in_Gasoline = 0/100 
total  = MTBE_in_Gasoline + ETH_in_Gasoline + REF2_in_Gasoline

for s in range(0,nsc):
    MTBE[s] = (1+total)*gasolineSC[s]*MTBE_in_Gasoline 
    ETH[s]  = (1+total)*gasolineSC[s]*ETH_in_Gasoline  
    REF2[s] = (1+total)*gasolineSC[s]*REF2_in_Gasoline    


Stock_LN = 1.0 

exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))

for f in range(nsc):
    gasolineSCCO2[f] = gasolineSC[f]*(1-ETH_in_Gasoline)*ECO2B * 1000 # gasolineSC in KBPD and gasolineSCCO2 in kg
    gasolineSCCO2[f] = gasolineSCCO2[f] / 1000/ 1000 # gasolineSC in KBPD and gasolineSCCO2 in Kton
    gasolineSCCO2a[f] = gasolineSCCO2[f] / gasolineSC[f] * 1000/ 158.987295 # Kton / KBPD = ton / BPD = 1000 Kg / 158.987295 L 

ax1.plot(SC,gasolineSCCO2,color='green', label='100% StockRLN + ETH 25%', marker=6)
ax2.plot(SC,gasolineSCCO2a,color='green', label='100% StockRLN + ETH 25%', linestyle='dashed',  marker=6)

import matplotlib.ticker as plticker

loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
ax1.xaxis.set_major_locator(loc)
## Put a legend to the right of the current axis
#ax1.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
#ax2.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
#ax1.legend()
#ax2.legend()
text = ax1.text(-0.89,10.5, "|", fontsize=13)

pos = ax1.get_position()
ax1.set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])

ax1.legend(
    fontsize = 10,
    loc='lower center', 
    bbox_to_anchor=(0.5, 1.14),
    ncol=2, 
)

ax2.set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])
ax2.legend(
    fontsize = 10,
    loc='upper center', 
    bbox_to_anchor=(0.5, 1.14),
    ncol=2
)

plt.savefig('fig20.png')


plt.close()