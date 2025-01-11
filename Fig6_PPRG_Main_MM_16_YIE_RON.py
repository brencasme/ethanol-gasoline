### Fig5: PPRG Main (Yield and RON plots): 16 main scenarios (Yield and RON plots)
import matplotlib.pyplot as plt
# data initialization
exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/ini.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/ini.py','exec'))

#Ratio ISO-LN and POLY-GASES 
ISO = False
POLY = False
ISOFeed  = 0.0  # = 0 to exclude it
POLYFeed = 0.0  # = 0 to exclude it
HTLCNred = 0.98 # = 1 to exclude it

exec(compile(open(r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','rb').read(), r'D:/Cloud/OneDrive/HBKU/HBKU/students/Mahmoud/Ethanol/Plot_Ethanol/Plot_Ethanol/calc.py','exec'))

fig,ax1 = plt.subplots()
#fig.set_size_inches(6.0,5.0)


ax1.set_xlabel('Scenarios', fontsize=13)
ax1.set_ylabel('Gasoline Production in KBPD or Yield in vol% (   )' , fontsize=13)
ax1.tick_params(axis='y')

color = 'tab:red'
#ax1.plot(t,arrYield, color=color,   label='All', marker='+')

#
ax1.plot(t1,arrYieldLightRFCC, color=color)#, label='Yield')#  label='Light/RFCC', marker='x')
ax1.plot(t2,arrYieldLightFCC,  color=color, )#  label='Light/FCC', marker='v')
ax1.plot(t3,arrYieldHeavyRFCC, color=color, )#  label='Heavy/RFCC', marker='*')
ax1.plot(t4,arrYieldHeavyFCC,  color=color, )#  label='Heavy/FCC', marker='o')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylabel('RON (---)', fontsize=13)  # we already handled the x-label with ax1
ax2.tick_params(axis='y')

color = 'tab:blue'

ax2.plot(t1, arrRONLightRFCC, color=color, linestyle='dashed')#, label='RON')
ax2.plot(t2, arrRONLightFCC, color=color, linestyle='dashed' )  #, label='SC Case')
ax2.plot(t3, arrRONHeavyRFCC, color=color, linestyle='dashed')  #, label='SC Case')
ax2.plot(t4, arrRONHeavyFCC, color=color, linestyle='dashed' )  #, label='SC Case')

#fig.tight_layout()  # otherwise the right y-label is slightly clipped

text = ax1.text(1.4,27.58, "light/RFCC", fontsize=11.0)
text = ax1.text(5.8,27.58, "light/FCC",  fontsize=11.0)
text = ax1.text(9.5,27.58, "heavy/RFCC", fontsize=11.0)
text = ax1.text(13.5,27.58, "heavy/FCC", fontsize=11.0)

import matplotlib.ticker as plticker

loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
ax1.xaxis.set_major_locator(loc)
text = ax1.text(-1.30,36.375, "|", fontsize=13)

plt.savefig('fig6.png')


plt.close()