## Fig11: PPRG-Full + ETH 10% + REF2(22%) (when hits ARO at 25%)
import matplotlib.pyplot as plt
# data initialization
exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/ini.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/ini.py','exec'))

#Ratio ISO-LN and POLY-GASES 
ISOFeed  = 0.30  # = 0 to exclude it
POLYFeed = 0.50  # = 0 to exclude it
HTLCNred = 0.98 # = 1 to exclude it

fig,ax1 = plt.subplots()
fig.set_size_inches(6.0,5.8)

ax1.set_xlabel('Scenarios', fontsize=13)
ax1.set_ylabel('Gasoline Production in KBPD or Yield/ARO in vol% (   )', fontsize=13)
ax1.tick_params(axis='y')

color = 'tab:brown'

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylabel('RON (---)', fontsize=13)  # we already handled the x-label with ax1
ax2.tick_params(axis='y')

color = 'tab:red'

exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/ini.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/ini.py','exec'))

ISO = True
POLY = True

exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))

ax1.plot(SC,gasolineSC,color='red', label='Full PPRG')
ax2.plot(SC,gasolineSCRON,color='blue',label='Full PPRG',linestyle='dashed')

#ETH = True

# Supply Chain (SC) or Exogenous Variables

MTBE_in_Gasoline = 0/100  ; ETH_in_Gasoline  = 10/100 #10%
REF2_in_Gasoline = 20/100 #10%
total  = MTBE_in_Gasoline + ETH_in_Gasoline + REF2_in_Gasoline

for s in range(0,nsc):
    MTBE[s] = (1+total)*gasolineSC[s]*MTBE_in_Gasoline 
    ETH[s]  = (1+total)*gasolineSC[s]*ETH_in_Gasoline  
    REF2[s] = (1+total)*gasolineSC[s]*REF2_in_Gasoline
    

exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))

ax1.plot(SC,gasolineSC,color='red', label='Full PPRG + ETH 10% + REF2 20%', marker='x')
ax1.plot(SC,gasolineSCARO,color='green',label='ARO', marker='o')
ax2.plot(SC,gasolineSCRON,color='blue',label='Full PPRG + ETH 10% + REF2 20%',linestyle='dashed', marker='x')

#fig.tight_layout()  # otherwise the right y-label is slightly clipped
#
import matplotlib.ticker as plticker

loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
ax1.xaxis.set_major_locator(loc)
## Put a legend to the right of the current axis
#ax1.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
#ax2.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
#ax1.legend()
#ax2.legend()
text = ax1.text(-1.43,54.15, "|", fontsize=13)
pos = ax1.get_position()
ax1.set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])
ax1.legend(
    fontsize = 9,
    loc='lower center', 
    bbox_to_anchor=(0.5, 1.14),
    ncol=2, 
)

ax2.set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])
ax2.legend(
    fontsize = 9,
    loc='upper center', 
    bbox_to_anchor=(0.5, 1.14),
    ncol=2
)


plt.savefig('fig12.png')
plt.close()