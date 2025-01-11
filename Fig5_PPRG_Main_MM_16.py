## Fig4: PPRG Main (Yield plot): 16 main scenarios (Yields detailed per unit)
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

fig,ax = plt.subplots()
fig.set_size_inches(6.0,5.0)

ax.set_xlabel('Scenarios', fontsize=12)
ax.set_ylabel('Gasoline Production in KBPD or Yield in vol%' , fontsize=12)
ax.tick_params(axis='y')
ax.plot(SC,gasolineSC,color='red', label='Total',marker='x')

ax.plot(xl,yl,color='green', label='CDU')
ax.plot(xh,yh,color='green')
ax.plot(xll,yll,color='gray', label='REF', linestyle='dashed') 
ax.plot(xhh,yhh,color='gray', linestyle='dashed')

ax.plot(x1,y1,color='blue', linestyle='dashdot', label='RFCC') 
ax.plot(x2,y2,color='blue', linestyle='dashdot') 
ax.plot(x12,y12,color='blue', label='FCC',linestyle='dotted') 
ax.plot(x22,y22,color='blue',linestyle='dotted') 

ax.plot(SCJUMP11,gasolineSCREFJUMP11,'v', markersize=5, markerfacecolor='yellow', 
    markeredgecolor='purple', markeredgewidth=1.5, alpha=0.9, label='REF Low-ON')
ax.plot(SCJUMP12,gasolineSCREFJUMP12,'o', markersize=5, markerfacecolor='yellow', 
        markeredgecolor='purple', markeredgewidth=1.5, alpha=0.9, label='REF High-ON')
ax.plot(SCJUMP21,gasolineSCCCJUMP21,'s', markersize=5, markerfacecolor='orange', 
    markeredgecolor='blue', markeredgewidth=1.5, alpha=0.9, label='CC Gasoline')
ax.plot(SCJUMP22,gasolineSCCCJUMP22,'D', markersize=5, markerfacecolor='orange', 
        markeredgecolor='blue', markeredgewidth=1.5, alpha=0.9, label='CC Diesel')

ax.plot(SCR1,gasolineSCR1,linestyle='dotted')
ax.plot(SCR2,gasolineSCR2,linestyle='dotted')
ax.plot(SCR3,gasolineSCR3,linestyle='dotted')

text = ax.text(7.55,34.58, "Petroleum", fontsize=9)
text = ax.text(6.50,33.58, "<------------", fontsize=8)
text = ax.text(8.75,33.58,"------------>", fontsize=8)
text = ax.text(7.0,32.58, "lighter", fontsize=9)
text = ax.text(8.8,32.58, "heavier", fontsize=9)
#
import matplotlib.ticker as plticker

loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)
ax.legend(fontsize=6.5)
## Set the range of x-axis
plt.xlim(1, 16)
plt.ylim(0, 36)

plt.savefig('fig5.png', bbox_inches='tight')

plt.close()




