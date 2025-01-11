### Fig6: PPRG Main and Secondary (Yield and RON plots): 16 + (ISO, POLY and Both): 16 (Main) + 16 (Main+ISO) + 16 (Main+POLY) + 16 (Main+Both) = 64
import matplotlib.pyplot as plt
# data initialization
exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/ini.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/ini.py','exec'))

#Ratio ISO-LN and POLY-GASES 
ISOFeed  = 0.30  # = 0 to exclude it
POLYFeed = 0.50  # = 0 to exclude it
HTLCNred = 0.98 # = 1 to exclude it

fig,ax1 = plt.subplots()
fig.set_size_inches(6.0,5.2)

ax1.set_xlabel('Scenarios', fontsize=13)
ax1.set_ylabel('Gasoline Production in KBPD or Yield in %vol (   )' , fontsize=13)
ax1.tick_params(axis='y')

color = 'tab:red'

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylabel('RON (---)', fontsize=13)  # we already handled the x-label with ax1
ax2.tick_params(axis='y')

color = 'tab:blue'

ISO = False
POLY = False
exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))

ax1.plot(SC,gasolineSC,color='red', label='PPRG')
ax2.plot(SC,gasolineSCRON,color='blue', linestyle='dashed', label='PPRG')

ISO = True
POLY = False
exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))

ax1.plot(SC,gasolineSC,color='red', label='PPRG+ISO', marker='o')
ax2.plot(SC,gasolineSCRON,color='blue', linestyle='dashed', label='PPRG+ISO', marker='o')

ISO = False
POLY = True
exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))

ax1.plot(SC,gasolineSC,color='red', label='PPRG+POLY', marker='s')
ax2.plot(SC,gasolineSCRON,color='blue',label='PPRG+POLY', linestyle='dashed', marker='s')

ISO = True
POLY = True

exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))

ax1.plot(SC,gasolineSC,color='red', label='PPRG+Both', marker='x')
ax2.plot(SC,gasolineSCRON,color='blue',label='PPRG+Both',linestyle='dashed', marker='x')


#fig.tight_layout()  # otherwise the right y-label is slightly clipped
#
import matplotlib.ticker as plticker

loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
ax1.xaxis.set_major_locator(loc)
## Put a legend to the right of the current axis
ax1.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
ax2.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
ax1.legend()
ax2.legend()
text = ax1.text(-1.9,38.9, "|", fontsize=13)
pos = ax1.get_position()
ax1.set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])
ax1.legend(
    fontsize = 10,
    loc='lower center', 
    bbox_to_anchor=(0.5, 1.17),
    ncol=2, 
)

ax2.set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])
ax2.legend(
    fontsize = 10,
    loc='upper center', 
    bbox_to_anchor=(0.5, 1.17),
    ncol=2
)

plt.savefig('fig7.png')
plt.close()
