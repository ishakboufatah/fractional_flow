# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 17:54:30 2021

@author: ishak
"""
import matplotlib.pyplot as plt
import numpy as np
from data import *
from function import *
from matplotlib.gridspec import GridSpec
import matplotlib.lines as lines
import matplotlib.image as mpimg
print(Sw)


#SG=[0]*len(So)
#for i in range(len(So)):
#    SG[i]=1-So[i]
SS = np.arange(0., 1., 0.01)
"""
#plt.plot(Sw,Krw, '-b',label='water relative permeability Krw')
plt.plot(Sw,Krow,'ro',label='SCAL oil relative permeability ')
plt.plot(SS,Kr_oil_w(SS),'-r',label='oil relative permeability function')
plt.axis([0, 1., 0, 1.])
plt.xlabel(' Sw')
plt.ylabel('Kr')
plt.legend()
plt.show()
"""

"""
plt.plot(Sw,Krow,'-r',label='oil relative permeability Kro')
plt.axis([0, 1., 0, 1.])
plt.xlabel(' Sw')
plt.ylabel('Kr')
plt.legend()
plt.show()


"""
"""
#plt.plot(SG_OMG_832_14,KrG_OMG_832_14, 'og',label='Expirimental gas relative permeability ')
plt.plot(SG,KrG, 'og',label='Expirimental gas relative permeability ')

plt.plot(SS,Kr_GAS(SS),'-r',label='gas relative permeability function')
#plt.plot(Sg,Krog,'ro',label='SCAL oil relative permeability')
plt.xlabel('Sg')
plt.ylabel('Kr')
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()
#print(SS)
#print(SS[2])
#print(Kr_gas(SS))


#plt.plot(SG_OMG_832_14,KrO_OMG_832_14,'ro',label='Expirimental oil relative permeability')
plt.plot(SG,KrO,'ro',label='Expirimental oil relative permeability')

plt.plot(SS,Kr_oil_G(SS),'-g',label='oil relative permeability function')
plt.xlabel('Sg')
plt.ylabel('Kr')
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()
#print(SS)
#print(Kr_oil_G(SS))
##############################################################################
#-------------------------RELATIVE PERMIABILITY CURVE-------------------------
##############################################################################

fig, ax1 = plt.subplots()
color = 'tab:blue'
#ax1.plot(SG_OMG_832_14,KrO_OMG_832_14, 'bo',label='Kro expérimentale ')
#ax1.plot(SG,KrO, 'bo',label='Kro expérimentale ')


xx=[0]*len(SS)
ax1.plot(SS,Kr_oil_G(SS), '-b',label='fonction Kro')
ax1.set_ylabel('Kro', color=color)
ax1.set_xlabel('Sg' )
ax1.axis([0, 1., 0, 1.])
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc=2)
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Krg', color=color)
ax2.axis([0, 1., 0, 1.])

#ax2.plot(SG_OMG_832_14,KrG_OMG_832_14, 'ro',label='Krg expérimentale ')
#ax2.plot(SG,KrG, 'ro',label='Krg expérimentale ')
#ax2.plot(Sg1,Krg1,'ro')
ax2.plot(SS,Kr_GAS(SS),'-r',label=' fonction Krg')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc=0)
plt.show()
"""
"""
a=1-0.016332635
SG=[0.016332635,0.05,0.1,0.15,0.2,0.25,0.3,0.3203]
SO=[0.36385,0.4,0.5,0.6,0.7,0.8,0.9,a]
plt.plot(SO,Kr_oil_(SO), '-b',label='fonction Kro')
print("Kr_oil_(SO)",Kr_oil_(SO))
plt.plot(SG,Kr_GAS(SG),'-r',label=' fonction Krg')
print("Kr_GAS(SG)",Kr_GAS(SG))
plt.axis([0, 1., 0, 1.])
plt.legend(loc=0)
plt.show()

"""
"""

#######################################################################
#                             Fractional Flow OG gas
#######################################################################

#plt.plot(Sg,Krog,'ro',label='oil relative permeability Kro')
#plt.plot(SS,fg(SS,0.1185,0.2448),'-r',label='fg à 275.79 BARSG ECLIPSE SCAL')
#plt.plot(SS,fg(SS,0.1185,0.2165),'-b',label='fg à 275.79 BARSG khaled')
plt.plot(SS,FG(SS,0.02,0.233),'-b',label='fg à 220 BARG ')
plt.xlabel('Sg')
plt.ylabel('fg')
plt.title("débit fractionnaire de gaz")
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()
"""
plt.plot([2,5,8,10,13,15,17,100],[69.65,65.86,61.77,55.34,64.14,76.89,100,100],'-b')
plt.plot([2,5,8,10,13,15,17],[69.65,65.86,61.77,55.34,64.14,76.89,100],'ok',label='taux de récupération calculé ')
plt.plot([2],[69.65],'og',label='gaz associés')
plt.plot([17],[100],'or',label="minimum concentration d'enrichissement ")
plt.xlabel('Concentraction de C3-4')
plt.ylabel('taux de récupération')
plt.title("")
plt.legend(loc=3)
plt.axis([0, 100.5, 0, 100.5])
plt.show()
#######################################################################
#                             Fractional Flux of C1-2
#######################################################################
#    FC1_2(sg,vg,vo,cg,co):  cc1TD(Sg,c1g,c1o):
    
   
#########################################################################
#------------------  Gas-Oil OMJ-323 Sample 4   -----------------------
#------------------      GAS injection    ------------------------
#########################################################################  
"""
plt.figure(figsize=(7,7))

plt.plot(cc1TD(SS,0.9,0.59),FC1_2(SS,0.02,0.233,0.9,0.59),'-y',label='Fc1-2 injection tie line ')
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.803,0.9,0.59),0.02,0.233,0.9,0.59)
YM4=FC1_2v(Sgv(0.675,0.79,0.6),0.02,0.233,0.79,0.6)

plt.plot([0.98,0.803,0.675,0.39],[0.98,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.803,0.675],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.98-YM5)/(0.98-0.803)
v2=(YM5-YM4)/(0.803-0.675)
v3=(YM4-0.39)/(0.675-0.39)

print("v1=" , v1)     #0.4520347221881165
print("v2=" , v2)     #0.9226005250564254
print("v3=" , v3)     #1.3750771472473013
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.98,0.98,'ok',label='J ')

#plt.plot([0.62],[YM1],'*r',label='M1' )
#plt.plot([0.6725],[YM2],'*y',label='M2' )
#plt.plot([0.685],[YM3],'*g',label='M3' )


#plt.plot([0.68],[0.68],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.65, 1.985], [0.76, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.64, 1.985], [0.826, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.plot([0.6, 1.985], [0.5698, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5817, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend()
plt.axis([0.35, 1,0.35, 1])
plt.show()    
"""   
   
#########################################################################
#------------------  Gas-Oil OMJ-323 Sample 4   -----------------------
#------------------      17 % GPL injection    ------------------------
#########################################################################  
"""
plt.figure(figsize=(7,7))
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')

#plt.plot(cc1TD(SS,0.76,0.605),FC1_2(SS,0.02,0.233,0.76,0.605),'-r',label='Fc1-2 M1 ')
#plt.plot(cc1TD(SS,0.74,0.615),FC1_2(SS,0.02,0.233,0.74,0.615),'-y',label='Fc1-2 M2 ')
plt.plot(cc1TD(SS,0.72,0.62),FC1_2(SS,0.02,0.233,0.72,0.62),'-g',label='Fc1-2 passant par M3 ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')





#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')
YM1=FC1_2v(Sgv(0.625,0.76,0.605),0.02,0.233,0.76,0.605)
YM2=FC1_2v(Sgv(0.675,0.74,0.615),0.02,0.233,0.74,0.615)
YM3=FC1_2v(Sgv(0.7,0.72,0.62),0.02,0.233,0.72,0.62)

YM4=FC1_2v(Sgv(0.7,0.72,0.62),0.02,0.233,0.72,0.62)
YM5=FC1_2v(Sgv(0.6415,0.79,0.6),0.02,0.233,0.79,0.6)

plt.plot([0.83,0.7,0.6415,0.39],[0.83,YM4,YM5,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.7,0.6415],[YM4,YM5],'-r',linewidth=1,label='Solution Path ' )

v1=(0.83-YM4)/(0.83-0.7)
v2=(YM4-YM5)/(0.7-0.6415)
v3=(YM5-0.39)/(0.6415-0.39)






print("v1=" , v1)     #0.846153846153846
print("v2=" , v2)     #0.9949938518055673
print("v3=" , v3)     #1.0806873147887648
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.83,0.83,'ok',label='J ')

#plt.plot([0.625],[YM1],'*r',label='M1' )
#plt.plot([0.675],[YM2],'*y',label='M2' )
plt.plot([0.7],[YM3],'*g',label='M3' )


#plt.plot([0.68],[0.68],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.65, 1.985], [0.76, 1.985],'-k',linewidth=0.3) #,clip_on=False
#plt.plot([0.64, 1.985], [0.73, 1.985],'-k',linewidth=0.3) #,clip_on=False
#plt.plot([0.64, 1.985], [0.7118, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.64, 1.985], [0.698, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.621, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.plot([0.6, 1.985], [0.59, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5817, 1.985],'-k',linewidth=0.3) #,clip_on=False
#plt.plot([0.62, 1.985], [0.62, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend()
plt.axis([0.35,0.9,0.35, 0.9])
plt.show()

"""


#########################################################################
#------------------  Gas-Oil OMJ-323 MOY   -----------------------
#------------------      GAS injection M    ------------------------
#########################################################################  
"""
plt.figure(figsize=(6,6))

plt.plot(cc1TD(SS,0.9,0.59),FC1_2(SS,0.02,0.233,0.9,0.59),'-y',label="Fc1-2 ligne de raccordement d'injection")
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'-b',label='Fc1-2 ligne de raccordement initiale ')


plt.plot(cc1TD(SS,0.885,0.59),FC1_2(SS,0.02,0.233,0.885,0.59),'-g',label='Fc1-2 passant par M4 ')


YM5=FC1_2v(Sgv(0.807,0.9,0.59),0.02,0.233,0.9,0.59)
YM4=FC1_2v(Sgv(0.626,0.79,0.6),0.02,0.233,0.79,0.6)


YM=FC1_2v(Sgv(0.79,0.885,0.59),0.02,0.233,0.885,0.59)
plt.plot([0.98,0.807,0.626,0.39],[0.98,YM5,YM4,0.39],'-r',linewidth=1,label='chemin de solution ' )
#plt.plot([0.807,0.626],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.98-YM5)/(0.98-0.807)
v2=(YM5-YM4)/(0.807-0.626)
v3=(YM4-0.39)/(0.626-0.39)

print("v1=" , v1)     #0.4624277456647398
print("v2=" , v2)     #0.9168119088259006
print("v3=" , v3)     #1.4578688326377627
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.98,0.98,'ok',label='J ')

plt.text(0.89, 0.96, "v1", va="center", ha="center")
plt.text(0.7, 0.82, "v2", va="center", ha="center")
plt.text(0.54, 0.65, "v3", va="center", ha="center")


plt.plot([0.79],[YM],'*b',label='M4' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.71, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.845, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudo-composé C1-2 à 220 BARG")

plt.legend(loc=2,frameon=False)
plt.axis([0.35, 1,0.35, 1])
plt.show()    

"""

#########################################################################
#------------------  Gas-Oil OMJ-323 MOY   -----------------------
#------------------      GAS injection    ------------------------
#########################################################################  
"""
plt.figure(figsize=(6,6))

plt.plot(cc1TD(SS,0.9,0.59),FC1_2(SS,0.02,0.233,0.9,0.59),'-y',label="Fc1-2 ligne de raccordement d'injection")
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'-b',label='Fc1-2 ligne de raccordement initiale ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.77,0.9,0.59),0.02,0.233,0.9,0.59)
YM4=FC1_2v(Sgv(0.64,0.79,0.6),0.02,0.233,0.79,0.6)

plt.plot([0.98,0.77,0.64,0.39],[0.98,YM5,YM4,0.39],'-r',linewidth=1,label='chemin de solution ' )
#plt.plot([0.77,0.64],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.98-YM5)/(0.98-0.77)
v2=(YM5-YM4)/(0.77-0.64)
v3=(YM4-0.39)/(0.64-0.39)

print("v1=" , v1)     #0.3809523809523808
print("v2=" , v2)     #0.8821621745713428
print("v3=" , v3)     #1.5812756692229017
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.98,0.98,'ok',label='J ')

plt.text(0.89, 0.96, "v1", va="center", ha="center")
plt.text(0.7, 0.85, "v2", va="center", ha="center")
plt.text(0.54, 0.65, "v3", va="center", ha="center")


#plt.plot([0.68],[0.68],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.845, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudo-composé C1-2 à 220 BARG")

plt.legend(loc=2,frameon=False)
plt.axis([0.35, 1,0.35, 1])
plt.show()    
"""



#########################################################################
#------------------  Gas-Oil OMJ-323 MOY   -----------------------
#------------------      GAS injection 4.5% GPL  M  ------------------------
#########################################################################  
"""
plt.figure(figsize=(6,6))

plt.plot(cc1TD(SS,0.875,0.593),FC1_2(SS,0.02,0.233,0.875,0.593),'-y',label="Fc1-2 ligne de raccordement d'injection ")
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 ligne de raccordement initiale')


plt.plot(cc1TD(SS,0.86,0.595),FC1_2(SS,0.02,0.233,0.86,0.595),'-g',label='Fc1-2 ligne de raccordement passant par  M2 ')


YM5=FC1_2v(Sgv(0.835,0.875,0.593),0.02,0.233,0.875,0.593)
YM4=FC1_2v(Sgv(0.6198,0.79,0.6),0.02,0.233,0.79,0.6)

YM=FC1_2v(Sgv(0.82,0.86,0.595),0.02,0.233,0.86,0.595)

plt.plot([0.95,0.835,0.6198,0.39],[0.95,YM5,YM4,0.39],'-r',linewidth=1,label='chemin de solution ' )
#plt.plot([0.807,0.6228],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.955-YM5)/(0.955-0.807)
v2=(YM5-YM4)/(0.807-0.6228)
v3=(YM4-0.39)/(0.6228-0.39)

print("v1=" , v1)     #0.5405405405405406
print("v2=" , v2)     #1.1301630513448961
print("v3=" , v3)     #1.1891063829135313
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.955,0.955,'ok',label='J ')


plt.plot([0.82],[YM],'*g',label='M2' )


plt.text(0.88, 0.91, "v1", va="center", ha="center")
plt.text(0.725, 0.78, "v2", va="center", ha="center")
plt.text(0.54, 0.62, "v3", va="center", ha="center")


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.646, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.824, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend(loc=2,frameon=False)
plt.axis([0.35, 1,0.35, 1])
plt.show()    
     
"""



#########################################################################
#------------------  Gas-Oil OMJ-323 MOY   -----------------------
#------------------      GAS injection 5% GPL    ------------------------
#########################################################################  
"""
plt.figure(figsize=(7,7))

plt.plot(cc1TD(SS,0.875,0.593),FC1_2(SS,0.02,0.233,0.875,0.593),'-y',label='Fc1-2 injection tie line ')
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.74,0.875,0.593),0.02,0.233,0.875,0.593)
YM4=FC1_2v(Sgv(0.64,0.79,0.6),0.02,0.233,0.79,0.6)

plt.plot([0.95,0.74,0.64,0.39],[0.95,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.77,0.64],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.95-YM5)/(0.95-0.74)
v2=(YM5-YM4)/(0.74-0.64)
v3=(YM4-0.39)/(0.64-0.39)

print("v1=" , v1)     #0.357142857142857
print("v2=" , v2)     #0.8968108269427457
print("v3=" , v3)     #1.5812756692229017
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.95,0.95,'ok',label='J ')

#plt.plot([0.62],[YM1],'*r',label='M1' )
#plt.plot([0.6725],[YM2],'*y',label='M2' )
#plt.plot([0.685],[YM3],'*g',label='M3' )


#plt.plot([0.68],[0.68],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.824, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend()
plt.axis([0.6, 1,0.6, 0.9])
plt.show()    
     
"""


#########################################################################
#------------------       Gas-Oil OMJ-323 MOY   -----------------------
#------------------      GAS injection 8% GPL    ------------------------
#########################################################################  
"""
plt.figure(figsize=(7,7))

plt.plot(cc1TD(SS,0.83,0.593),FC1_2(SS,0.02,0.233,0.83,0.593),'-y',label='Fc1-2 injection tie line ')
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.69,0.83,0.593),0.02,0.233,0.83,0.593)
YM4=FC1_2v(Sgv(0.64,0.79,0.6),0.02,0.233,0.79,0.6)

plt.plot([0.92,0.69,0.64,0.39],[0.92,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.77,0.64],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.92-YM5)/(0.92-0.69)
v2=(YM5-YM4)/(0.69-0.64)
v3=(YM4-0.39)/(0.64-0.39)

print("v1=" , v1)     #0.39130434782608714
print("v2=" , v2)     #0.8936216538854914
print("v3=" , v3)     #1.5812756692229017
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.92,0.92,'ok',label='J ')

#plt.plot([0.68],[0.68],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.786, 1.985],'-k',linewidth=0.3) #,clip_on=False

#plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend()
plt.axis([0.6, 1,0.6, 1])
plt.show()    
     
"""




#########################################################################
#------------------       Gas-Oil OMJ-323 MOY   -----------------------
#------------------      GAS injection 10% GPL    ------------------------
#########################################################################  
"""
plt.figure(figsize=(7,7))

plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial and injection tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')



YM4=FC1_2v(Sgv(0.64,0.79,0.6),0.02,0.233,0.79,0.6)

plt.plot([0.90,0.64,0.39],[0.90,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.77,0.64],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.9-YM4)/(0.9-0.64)
v3=(YM4-0.39)/(0.64-0.39)

print("v1=" , v1)     #0.357142857142857
print("v3=" , v3)     #1.5812756692229017
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.9,0.9,'ok',label='J ')



plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend()
plt.axis([0.35,0.95,0.35, 0.95])
plt.show() 
"""

#########################################################################
#------------------      Gas-Oil OMJ-323 MOY   -----------------------
#------------------      GAS injection 13% GPL    ------------------------
#########################################################################  
"""
plt.figure(figsize=(7,7))

plt.plot(cc1TD(SS,0.745,0.61),FC1_2(SS,0.02,0.233,0.745,0.61),'-y',label='Fc1-2 injection tie line ')
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.64,0.745,0.61),0.02,0.233,0.745,0.61)
YM4=FC1_2v(Sgv(0.6255,0.79,0.6),0.02,0.233,0.79,0.6)

plt.plot([0.87,0.64,0.6255,0.39],[0.87,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.64,0.6255],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.87-YM5)/(0.87-0.64)
v2=(YM5-YM4)/(0.64-0.6255)
v3=(YM4-0.39)/(0.6255-0.39)

print("v1=" , v1)     #0.5530953632067798
print("v2=" , v2)     #0.9113956476616084
print("v3=" , v3)     #1.4419228431904347
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.87,0.87,'ok',label='J ')

#plt.plot([0.62],[YM1],'*r',label='M1' )
#plt.plot([0.6725],[YM2],'*y',label='M2' )
#plt.plot([0.685],[YM3],'*g',label='M3' )


#plt.plot([0.68],[0.68],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.707, 1.985],'-k',linewidth=0.3) #,clip_on=False

#plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend()
plt.axis([0.35, 0.9,0.35, 0.9])
plt.show()    

"""


#########################################################################
#------------------       Gas-Oil OMJ-323 MOY   -----------------------
#------------------      GAS injection 15.5% GPL  M    ------------------------
#########################################################################  
"""
plt.figure(figsize=(7,7))

plt.plot(cc1TD(SS,0.7,0.625),FC1_2(SS,0.02,0.233,0.7,0.625),'-y',label="Fc1-2 ligne de raccordement d'injection ")
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 ligne de raccordement initiale')


plt.plot(cc1TD(SS,0.745,0.61),FC1_2(SS,0.02,0.233,0.745,0.61),'--g',label='Fc1-2 ligne de raccordement passant par  M2 ')


YM5=FC1_2v(Sgv(0.64,0.7,0.625),0.02,0.233,0.7,0.625)
YM4=FC1_2v(Sgv(0.6193,0.79,0.6),0.02,0.233,0.79,0.6)

YM=FC1_2v(Sgv(0.705,0.745,0.61),0.02,0.233,0.745,0.61)

plt.plot([0.845,0.705,0.6193,0.39],[0.845,YM,YM4,0.39],'-r',linewidth=1,label='chemin de solution ' )
#plt.plot([0.64,0.621],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.845-YM)/(0.845-0.705)
v2=(YM-YM4)/(0.705-0.6193)
v3=(YM4-0.39)/(0.6193-0.39)

print("v1=" , v1)     #0.7142857142857141
print("v2=" , v2)     #0.9779796292184891
print("v3=" , v3)     #1.1826739894285894
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.845,0.845,'ok',label='J ')

#plt.plot([0.62],[YM1],'*r',label='M1' )
#plt.plot([0.6725],[YM2],'*y',label='M2' )
plt.plot([0.705],[YM],'*g',label='M2' )


#plt.plot([0.68],[0.68],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.642, 1.985],'-k',linewidth=0.3) #,clip_on=False

#plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend(loc=2,frameon=False)
plt.axis([0.35, 1,0.35, 1])
plt.show()    
     
"""




#########################################################################
#------------------       Gas-Oil OMJ-323 MOY   -----------------------
#------------------      GAS injection 15% GPL    ------------------------
#########################################################################  
"""
plt.figure(figsize=(7,7))

plt.plot(cc1TD(SS,0.7,0.625),FC1_2(SS,0.02,0.233,0.7,0.625),'-y',label='Fc1-2 injection tie line ')
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.64,0.7,0.625),0.02,0.233,0.7,0.625)
YM4=FC1_2v(Sgv(0.621,0.79,0.6),0.02,0.233,0.79,0.6)

plt.plot([0.85,0.64,0.621,0.39],[0.85,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.64,0.621],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.85-YM5)/(0.85-0.64)
v2=(YM5-YM4)/(0.64-0.621)
v3=(YM4-0.39)/(0.621-0.39)

print("v1=" , v1)     #0.7269850783074581
print("v2=" , v2)     #0.8728354608341232
print("v3=" , v3)     #1.2586548043272097
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.85,0.85,'ok',label='J ')

#plt.plot([0.62],[YM1],'*r',label='M1' )
#plt.plot([0.6725],[YM2],'*y',label='M2' )
#plt.plot([0.685],[YM3],'*g',label='M3' )


#plt.plot([0.68],[0.68],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.66, 1.985],'-k',linewidth=0.3) #,clip_on=False

#plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend()
plt.axis([0.6, 1,0.6, 0.9])
plt.show()    
     
"""
#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      17 % GPL injection M3   ------------------------
######################################################################### 
"""

plt.figure(figsize=(7,7))
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')

#plt.plot(cc1TD(SS,0.76,0.605),FC1_2(SS,0.02,0.233,0.76,0.605),'-r',label='Fc1-2 M1 ')
#plt.plot(cc1TD(SS,0.74,0.615),FC1_2(SS,0.02,0.233,0.74,0.615),'-y',label='Fc1-2 M2 ')
plt.plot(cc1TD(SS,0.72,0.62),FC1_2(SS,0.02,0.233,0.72,0.62),'-g',label='Fc1-2 passant par M3 ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')
YM1=FC1_2v(Sgv(0.625,0.76,0.605),0.02,0.233,0.76,0.605)
YM2=FC1_2v(Sgv(0.675,0.74,0.615),0.02,0.233,0.74,0.615)
YM3=FC1_2v(Sgv(0.7,0.72,0.62),0.02,0.233,0.72,0.62)

YM4=FC1_2v(Sgv(0.7,0.72,0.62),0.02,0.233,0.72,0.62)
YM5=FC1_2v(Sgv(0.617,0.79,0.6),0.02,0.233,0.79,0.6)

plt.plot([0.83,0.7,0.617,0.39],[0.83,YM4,YM5,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.7,0.617],[YM4,YM5],'-r',linewidth=1,label='Solution Path ' )

v1=(0.83-YM4)/(0.83-0.7)
v2=(YM4-YM5)/(0.7-0.617)
v3=(YM5-0.39)/(0.617-0.39)

print("v1=" , v1)     #0.846153846153846
print("v2=" , v2)     #0.9900975088481873
print("v3=" , v3)     #1.091726461522469
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.83,0.83,'ok',label='J ')

#plt.plot([0.625],[YM1],'*r',label='M1' )
#plt.plot([0.675],[YM2],'*y',label='M2' )
plt.plot([0.7],[YM3],'*g',label='M3' )


#plt.plot([0.68],[0.68],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
#plt.plot([0.6, 1.985], [0.728, 1.985],'-k',linewidth=0.3) #,clip_on=False
#plt.plot([0.6, 1.985], [0.7038, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.679, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.621, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.plot([0.59, 1.987], [0.5855, 1.985],'-k',linewidth=0.3) #,clip_on=False
#plt.plot([0.6, 1.985], [0.5817, 1.985],'-k',linewidth=0.3) #,clip_on=False
#plt.plot([0.62, 1.985], [0.62, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend()
#plt.axis([0.585, 0.8,0.585, 0.8])
plt.axis([0.35, 0.85,0.35, 0.85])
plt.show()
"""

#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      17 % GPL injection M2    ------------------------
######################################################################### 


plt.figure(figsize=(7,7))
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'-b',label='Fc1-2 ligne de raccordement initiale')

plt.plot(cc1TD(SS,0.745,0.61),FC1_2(SS,0.02,0.233,0.745,0.61),'-g',label='Fc1-2 ligne de raccordement passant par  M2 ')


YM4=FC1_2v(Sgv(0.67,0.745,0.61),0.02,0.233,0.745,0.61)
YM5=FC1_2v(Sgv(0.62254,0.79,0.6),0.02,0.233,0.79,0.6)


plt.plot([0.83,0.67,0.62254,0.39],[0.83,YM4,YM5,0.39],'-r',linewidth=1,label='chemin de solution ' )
#plt.plot([0.7,0.617],[YM4,YM5],'-r',linewidth=1,label='Solution Path ' )

v1=(0.83-YM4)/(0.83-0.67)
v2=(YM4-YM5)/(0.67-0.62254)
v3=(YM5-0.39)/(0.62254-0.39)
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.83,0.83,'ok',label='J ')




plt.plot([0.67],[YM4],'*r',label='M2' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.678, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.plot([0.59, 1.987], [0.5855, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend(loc=2,frameon=False)
#plt.axis([0.585, 0.8,0.585, 0.8])
plt.axis([0.35, 1,0.35, 1])
plt.show()

#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      17 % GPL injection    ------------------------
######################################################################### 
"""

plt.figure(figsize=(7,7))
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


plt.plot([0.83,0.39],[0.83,0.39],'-r',linewidth=3,label='Solution Path ' )
#plt.plot([0.7,0.617],[YM4,YM5],'-r',linewidth=1,label='Solution Path ' )

v1=v2=v3=1

print("v1=" , v1)     #0.846153846153846
print("v2=" , v2)     #0.9900975088481873
print("v3=" , v3)     #1.091726461522469
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.83,0.83,'ok',label='J ')




plt.plot([0.66],[0.66],'*r',label='PT' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False


plt.plot([0.59, 1.987], [0.5855, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend()
#plt.axis([0.585, 0.8,0.585, 0.8])
plt.axis([0.35, 0.85,0.35, 0.85])
plt.show()
"""
#######################################################################

#######################################################################
"""

plt.figure(figsize=(7,7))
plt.plot(cc1TD(SS,0.95,0.7),FC1_2(SS,0.1185,0.2448,0.95,0.7),'--b',label='fc1-2 initial tie line ')
plt.plot(cc1TD(SS,0.895,0.695),FC1_2(SS,0.1185,0.2448,0.895,0.695),'-y',label='fc1-2 M1 ')
plt.plot(cc1TD(SS,0.88,0.695),FC1_2(SS,0.1185,0.2448,0.88,0.695),'-g',label='fc1-2 M2 ')
plt.plot(cc1TD(SS,0.865,0.69),FC1_2(SS,0.1185,0.2448,0.865,0.69),'-r',label='fc1-2 M3 ')
plt.plot(cc1TD(SS,0.845,0.69),FC1_2(SS,0.1185,0.2448,0.845,0.69),'-c',label='fc1-2 M4 ')
plt.plot(cc1TD(SS,0.825,0.685),FC1_2(SS,0.1185,0.2448,0.825,0.685),'-m',label='fc1-2 M5 ')
plt.plot(cc1TD(SS,0.8,0.68),FC1_2(SS,0.1185,0.2448,0.8,0.68),'-b',label='fc1-2 M6 ')
plt.plot(0.4,0.4,'*k',label='I ')
plt.plot(0.98,0.98,'*k',label='J ')
#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')
YM1=FC1_2v(Sgv(0.865,0.895,0.695),0.1185,0.2448,0.895,0.695)
YM2=FC1_2v(Sgv(0.82,0.88,0.695),0.1185,0.2448,0.88,0.695)
YM3=FC1_2v(Sgv(0.785,0.865,0.69),0.1185,0.2448,0.865,0.69)
YM4=FC1_2v(Sgv(0.765,0.845,0.69),0.1185,0.2448,0.845,0.69)
YM5=FC1_2v(Sgv(0.735,0.825,0.685),0.1185,0.2448,0.825,0.685)
#YM6=fC1_2v(Sgv(0.69,0.8,0.68),0.1185,0.2448,0.8,0.68)
plt.plot([0.865,0.82,0.785,0.765,0.735],[YM1,YM2,YM3,YM4,YM5],'-k',label='Solution Path ' )
plt.plot([0.865],[YM1],'*y',label='M1' )
plt.plot([0.82],[YM2],'*g',label='M2' )
plt.plot([0.785],[YM3],'*r',label='M3' )
plt.plot([0.761],[YM4],'*c',label='M4' )
plt.plot([0.735],[YM5],'*m',label='M5' )
#plt.plot([0.69],[YM6],'*b',label='M6' )
plt.plot([0.68],[0.68],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.68, 2], [0.8, 2],'-k',linewidth=1) #,clip_on=False
plt.plot([0.785, 2], [YM3, 2],'-k',linewidth=1) #,clip_on=False
plt.xlabel('Cc1-2')
plt.ylabel('fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 275.79 BARSG")
plt.legend()
plt.axis([0.4, 1.,0.4, 1.])
plt.show()

#########################################################################

plt.figure(figsize=(7,7))
plt.plot(cc1TD(SS,0.82,0.635),FC1_2(SS,0.1185,0.233,0.82,0.635),'-b',label='ligne de raccordement initiale ')
plt.plot(cc1TD(SS,0.77,0.66),FC1_2(SS,0.1185,0.233,0.77,0.66),'-y',label='ligne de raccordement passant par M')


YM1=FC1_2v(Sgv(0.74,0.77,0.66),0.1185,0.233,0.77,0.66)
#YM6=fC1_2v(Sgv(0.69,0.8,0.68),0.1185,0.2448,0.8,0.68)
plt.plot([0.88,0.74,0.4],[0.88,YM1,0.4],'-r',label='chemin de solution ' )
plt.plot(0.4,0.4,'*g',label='I ')
plt.plot(0.88,0.88,'*k',label='J ')
plt.plot([0.74],[YM1],'*y',label='M' )
#plt.plot([0.701],[0.701],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
#plt.plot([0.68, 2], [0.8, 2],'-k',linewidth=1) #,clip_on=False
#plt.plot([0.785, 2], [YM3, 2],'-k',linewidth=1) #,clip_on=False
plt.xlabel('Cc1-2')
plt.ylabel('fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 275.79 BARSG")
plt.legend()
plt.axis([0.4, 1.,0.4, 1.])
plt.show()



plt.figure(figsize=(6,6))
plt.plot(cc1TD(SS,0.82,0.635),FC1_2(SS,0.1185,0.233,0.82,0.635),'-k',label='ligne de raccordement initiale ')
plt.plot(cc1TD(SS,0.91,0.62),FC1_2(SS,0.1185,0.233,0.91,0.62),'--k',label="ligne de raccordement d'injection")


#YM1=FC1_2v(Sgv(0.74,0.77,0.66),0.1185,0.233,0.77,0.66)
#YM6=fC1_2v(Sgv(0.69,0.8,0.68),0.1185,0.2448,0.8,0.68)
plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.68, 2], [0.772, 2],'-k',linewidth=0.5,clip_on=True) #,clip_on=False
plt.plot([0.68, 2], [0.827, 2],'-k',linewidth=0.5,clip_on=True)
plt.plot([0.6, 2], [0.545, 2],'-k',linewidth=0.5,clip_on=True)
plt.plot([0.6, 2], [0.566, 2],'-k',linewidth=0.5,clip_on=True)
plt.plot([0.98,0.828,0.73,0.4],[0.98,0.91,0.82,0.4],'-k',label='chemin de solution ' ,linewidth=2.5 )
plt.plot(0.4,0.4,'k*',label='I ')
plt.plot(0.98,0.98,'ok',label='J ')
plt.text(0.91, 0.96, "v1", va="center", ha="center")
plt.text(0.78, 0.85, "v2", va="center", ha="center")
plt.text(0.617, 0.65, "v3", va="center", ha="center")

v1=(0.98-0.91)/(0.98-0.83)
v2=(0.91-0.82)/(0.83-0.735)
v3=(0.82-0.4)/(0.735-0.4)
#d=v1*t  t=d/v1


#plt.plot([0.785, 2], [YM3, 2],'-k',linewidth=1) #,clip_on=False
plt.xlabel('Cc1-2')
plt.ylabel('fc1-2')
plt.title("flux fractionnaire de pseudo-composé C1-2 à 220 BARSG")

plt.legend(loc=2,frameon=False)
plt.axis([0.3, 1.,0.3, 1.])
plt.show()

###########################################################################

plt.figure(figsize=(6,6))
plt.plot(cc1TD(SS,0.82,0.635),FC1_2(SS,0.1185,0.233,0.82,0.635),'-k',label='ligne de raccordement initiale ')
plt.plot(cc1TD(SS,0.77,0.66),FC1_2(SS,0.1185,0.233,0.77,0.66),'--k',label='ligne de raccordement passant par M')


YM1=FC1_2v(Sgv(0.74,0.77,0.66),0.1185,0.233,0.77,0.66)
#YM6=fC1_2v(Sgv(0.69,0.8,0.68),0.1185,0.2448,0.8,0.68)
plt.plot([0.88,0.74,0.4],[0.88,YM1,0.4],'-k',label='chemin de solution ',linewidth=2.5 )
plt.plot(0.4,0.4,'*k',label='I ')
plt.plot(0.88,0.88,'ok',label='J ')
plt.plot([0.74],[YM1],'vk',label='M' )
plt.text(0.82, 0.85, "v1", va="center", ha="center")
plt.text(0.6, 0.64, "v2", va="center", ha="center")
#plt.plot([0.701],[0.701],'*b',label='PP' )

v1=(0.88-YM1)/(0.88-0.74)
v2=(YM1-0.4)/(0.74-0.4)
#d=v1*t  t=d/v1
plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
#plt.plot([0.68, 2], [0.8, 2],'-k',linewidth=1) #,clip_on=False
#plt.plot([0.785, 2], [YM3, 2],'-k',linewidth=1) #,clip_on=False
plt.xlabel('Cc1-2')
plt.ylabel('fc1-2')
plt.title("flux fractionnaire de pseu-docomposé C1-2 à 220 BARSG")
plt.legend(loc=2,frameon=False)
plt.axis([0.3, 1.,0.3, 1.])
plt.show()


"""


"""
###########################################################################


def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])

# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax1.plot(cc1TD(SS,0.82,0.635),FC1_2(SS,0.1185,0.233,0.82,0.635),'-b',label='ligne de raccordement initiale ')
ax1.plot(cc1TD(SS,0.77,0.66),FC1_2(SS,0.1185,0.233,0.77,0.66),'-y',label='ligne de raccordement passant par M')


YM1=FC1_2v(Sgv(0.74,0.77,0.66),0.1185,0.233,0.77,0.66)
#YM6=fC1_2v(Sgv(0.69,0.8,0.68),0.1185,0.2448,0.8,0.68)
ax1.plot([0.88,0.74,0.4],[0.88,YM1,0.4],'-r',label='chemin de solution ' )
ax1.plot(0.4,0.4,'*g',label='I ')
ax1.plot(0.88,0.88,'*k',label='J ')
ax1.plot([0.74],[YM1],'*y',label='M' )
#plt.plot([0.701],[0.701],'*b',label='PP' )

v1=(0.88-YM1)/(0.88-0.74)
v2=(YM1-0.4)/(0.74-0.4)
#d=v1*t  t=d/v1
ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
#plt.plot([0.68, 2], [0.8, 2],'-k',linewidth=1) #,clip_on=False
#plt.plot([0.785, 2], [YM3, 2],'-k',linewidth=1) #,clip_on=False
ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('fc1-2')
ax1.set_title("flux fractionnaire de pseu-docomposé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('GPLINJECTION_PY.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])
def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(0.88)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(0.74)
        elif XD[i]>(v2*TD):
            a.append(0.4)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(0.88)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(0.77)
        elif XD[i]>(v2*TD):
            a.append(0.)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(0.)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(0.66)
        elif XD[i]>(v2*TD):
            a.append(0.4)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,0.1),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.1),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.1),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=0.5 (injection de 12% de GPL au premier contact)")
#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.0995,0.1991,0.2986,0.3982,0.49779,0.599449,0.7019533,0.801509,0.9016,
          0.9410311],
         [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],'-y' ,label='huil produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.3, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.4, "huile en place", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 12% GPL à 220 BARG (point de mélange en M)")
#format_axes(fig)

plt.show()
"""
##############################################################################




#########################################################################
#------------------  Gas-Oil OMJ-323 Sample 4   -----------------------
#------------------      GAS injection    ------------------------
#########################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.9,0.59),FC1_2(SS,0.02,0.233,0.9,0.59),'-y',label='Fc1-2 injection tie line ')
ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.803,0.9,0.59),0.02,0.233,0.9,0.59)
YM4=FC1_2v(Sgv(0.675,0.79,0.6),0.02,0.233,0.79,0.6)

ax1.plot([0.98,0.803,0.675,0.39],[0.98,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.803,0.675],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.98-YM5)/(0.98-0.803)
v2=(YM5-YM4)/(0.803-0.675)
v3=(YM4-0.39)/(0.675-0.39)

print("v1=" , v1)     #0.4520347221881165
print("v2=" , v2)     #0.9226005250564254
print("v3=" , v3)     #1.3750771472473013   1/v3=0.7272319244
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.98,0.98,'ok',label='J ')



ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.65, 1.985], [0.76, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.64, 1.985], [0.826, 1.985],'-k',linewidth=0.3) #,clip_on=False

ax1.plot([0.6, 1.985], [0.5698, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.5817, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('gasinjectionmoy_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.98         ; C1_2gas_J=0.98    ; C1_2huil_J=0
C1_2_s1=0.803        ; C1_2gas_s1=0.9   ; C1_2huil_s1=0.59
C1_2_s2=0.675        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39
def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,0.5),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.5),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.5),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=0.5 ")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.6951799,0.80648162],[0,0.7272319244,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection GAS assoscié à 220 BARG  RF= 80.65 %")
#format_axes(fig)

plt.show()
"""















#########################################################################
#------------------  Gas-Oil OMJ-323 Sample 4   -----------------------
#------------------      17 % GPL injection    ------------------------
#########################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')

ax1.plot(cc1TD(SS,0.72,0.62),FC1_2(SS,0.02,0.233,0.72,0.62),'-g',label='Fc1-2 passant par M3 ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')





#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')
YM1=FC1_2v(Sgv(0.625,0.76,0.605),0.02,0.233,0.76,0.605)
YM2=FC1_2v(Sgv(0.675,0.74,0.615),0.02,0.233,0.74,0.615)
YM3=FC1_2v(Sgv(0.7,0.72,0.62),0.02,0.233,0.72,0.62)

YM4=FC1_2v(Sgv(0.7,0.72,0.62),0.02,0.233,0.72,0.62)
YM5=FC1_2v(Sgv(0.6415,0.79,0.6),0.02,0.233,0.79,0.6)

ax1.plot([0.83,0.7,0.6415,0.39],[0.83,YM4,YM5,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.7,0.6415],[YM4,YM5],'-r',linewidth=1,label='Solution Path ' )

v1=(0.83-YM4)/(0.83-0.7)
v2=(YM4-YM5)/(0.7-0.6415)
v3=(YM5-0.39)/(0.6415-0.39)

print("v1=" , v1)     #0.846153846153846
print("v2=" , v2)     #0.9949938518055673
print("v3=" , v3)     #1.0806873147887648   1/v3=0.925337
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.83,0.83,'ok',label='J ')

#plt.plot([0.625],[YM1],'*r',label='M1' )
#plt.plot([0.675],[YM2],'*y',label='M2' )
ax1.plot([0.7],[YM3],'*g',label='M3' )

ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.65, 1.985], [0.76, 1.985],'-k',linewidth=0.3) #,clip_on=False
#plt.plot([0.64, 1.985], [0.73, 1.985],'-k',linewidth=0.3) #,clip_on=False
#plt.plot([0.64, 1.985], [0.7118, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.64, 1.985], [0.698, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.621, 1.985],'-k',linewidth=0.3) #,clip_on=False

ax1.plot([0.6, 1.985], [0.59, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.5817, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('gplinjectionOMJ-323_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.83         ; C1_2gas_J=0.83    ; C1_2huil_J=0
C1_2_s1=0.7        ; C1_2gas_s1=0.72   ; C1_2huil_s1=0.62
C1_2_s2=0.6415        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39
def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,0.5),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.5),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.5),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=0.5 ")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.90926,0.963544],[0,0.925337,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 17% GPL à 220 BARG  RF= 96.35 %")
#format_axes(fig)

plt.show()


"""



#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      GAS injection M    ------------------------
#########################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.9,0.59),FC1_2(SS,0.02,0.233,0.9,0.59),'-y',label="Fc1-2 ligne de raccordement d'injection")
ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'-b',label='Fc1-2 ligne de raccordement initiale ')


#ax1.plot(cc1TD(SS,0.885,0.59),FC1_2(SS,0.02,0.233,0.885,0.59),'-g',label='Fc1-2 passant par M4 ')


YM5=FC1_2v(Sgv(0.807,0.9,0.59),0.02,0.233,0.9,0.59)
YM4=FC1_2v(Sgv(0.626,0.79,0.6),0.02,0.233,0.79,0.6)


YM=FC1_2v(Sgv(0.79,0.885,0.59),0.02,0.233,0.885,0.59)
ax1.plot([0.98,0.807,0.626,0.39],[0.98,YM5,YM4,0.39],'-r',linewidth=1,label='chemin de solution ' )
#plt.plot([0.807,0.626],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.98-YM5)/(0.98-0.807)
v2=(YM5-YM4)/(0.807-0.626)
v3=(YM4-0.39)/(0.626-0.39)

print("v1=" , v1)     #0.4624277456647398
print("v2=" , v2)     #0.9168119088259006
print("v3=" , v3)     #1.4578688326377627   0.685933
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.98,0.98,'ok',label='J ')

ax1.text(0.89, 0.96, "v1", va="center", ha="center")
ax1.text(0.7, 0.82, "v2", va="center", ha="center")
ax1.text(0.54, 0.65, "v3", va="center", ha="center")

ax1.plot([0.79],[YM],'*b',label='M4' )

ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.6, 1.985], [0.71, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.845, 1.985],'-k',linewidth=0.3) #,clip_on=False

ax1.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend(frameon=False)
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('gasinjectionmoyM_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.98         ; C1_2gas_J=0.98    ; C1_2huil_J=0
C1_2_s1=0.807        ; C1_2gas_s1=0.9   ; C1_2huil_s1=0.59
C1_2_s2=0.626        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39
def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,1),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,1),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,1),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,1),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=1 ")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.581028,0.791177],[0,0.685933,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection GAS assoscié à 220 BARG   RF= 79.12 %")
#format_axes(fig)

plt.show()

"""





#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      GAS injection    ------------------------
#########################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.9,0.59),FC1_2(SS,0.02,0.233,0.9,0.59),'-y',label='Fc1-2 injection tie line ')
ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.77,0.9,0.59),0.02,0.233,0.9,0.59)
YM4=FC1_2v(Sgv(0.64,0.79,0.6),0.02,0.233,0.79,0.6)

ax1.plot([0.98,0.77,0.64,0.39],[0.98,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.77,0.64],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.98-YM5)/(0.98-0.77)
v2=(YM5-YM4)/(0.77-0.64)
v3=(YM4-0.39)/(0.64-0.39)

print("v1=" , v1)     #0.3809523809523808
print("v2=" , v2)     #0.8821621745713428
print("v3=" , v3)     #1.5812756692229017  1/v3=0.6324
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.98,0.98,'ok',label='J ')




ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.64, 1.985], [0.88, 1.985],'-k',linewidth=0.3) #,clip_on=False

ax1.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('gasinjectionmoy_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.98         ; C1_2gas_J=0.98    ; C1_2huil_J=0
C1_2_s1=0.77        ; C1_2gas_s1=0.9   ; C1_2huil_s1=0.59
C1_2_s2=0.64        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39
def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,0.5),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.5),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.5),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=0.5 ")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.51697546,0.69648722],[0,0.6324,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection GAS assoscié à 220 BARG   RF= 69.65 %")
#format_axes(fig)

plt.show()

"""




#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      GAS injection 4.5% GPL  M   ------------------------
#########################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.875,0.593),FC1_2(SS,0.02,0.233,0.875,0.593),'-y',label="Fc1-2 ligne de raccordement d'injection ")
ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 ligne de raccordement initiale')


#ax1.plot(cc1TD(SS,0.86,0.595),FC1_2(SS,0.02,0.233,0.86,0.595),'-g',label='Fc1-2 ligne de raccordement passant par  M2 ')


YM5=FC1_2v(Sgv(0.835,0.875,0.593),0.02,0.233,0.875,0.593)
YM4=FC1_2v(Sgv(0.6198,0.79,0.6),0.02,0.233,0.79,0.6)

YM=FC1_2v(Sgv(0.82,0.86,0.595),0.02,0.233,0.86,0.595)

ax1.plot([0.95,0.835,0.6198,0.39],[0.95,YM5,YM4,0.39],'-r',linewidth=1,label='chemin de solution ' )
#plt.plot([0.807,0.6228],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.955-YM5)/(0.955-0.835)
v2=(YM5-YM4)/(0.835-0.6198)
v3=(YM4-0.39)/(0.6198-0.39)

print("v1=" , v1)     #0.6666666666666664
print("v2=" , v2)     #0.9673607530563659
print("v3=" , v3)     #1.2046299649359011     0.830130
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.955,0.955,'ok',label='J ')


ax1.plot([0.82],[YM],'*g',label='M2' )


ax1.text(0.88, 0.91, "v1", va="center", ha="center")
ax1.text(0.725, 0.78, "v2", va="center", ha="center")
ax1.text(0.54, 0.62, "v3", va="center", ha="center")


ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.6, 1.985], [0.646, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.824, 1.985],'-k',linewidth=0.3) #,clip_on=False

ax1.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('4.5%_gpl_injection_pyM.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.955         ; C1_2gas_J=0.955    ; C1_2huil_J=0
C1_2_s1=0.835        ; C1_2gas_s1=0.875   ; C1_2huil_s1=0.593
C1_2_s2=0.6198        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39


def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,0.5),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.5),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.5),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=0.5  ")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.788217,0.925654],[0,0.830130,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 4.5% GPL à 220 BARG  RF= 92.57 %")
#format_axes(fig)

plt.show()

"""




#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      GAS injection 5% GPL   ------------------------
#########################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.875,0.593),FC1_2(SS,0.02,0.233,0.875,0.593),'-y',label='Fc1-2 injection tie line ')
ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.74,0.875,0.593),0.02,0.233,0.875,0.593)
YM4=FC1_2v(Sgv(0.64,0.79,0.6),0.02,0.233,0.79,0.6)

ax1.plot([0.95,0.74,0.64,0.39],[0.95,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.77,0.64],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.95-YM5)/(0.95-0.74)
v2=(YM5-YM4)/(0.74-0.64)
v3=(YM4-0.39)/(0.64-0.39)

print("v1=" , v1)     #0.357142857142857
print("v2=" , v2)     #0.8968108269427457
print("v3=" , v3)     #1.5812756692229017   1/v3=0.6324
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.95,0.95,'ok',label='J ')


ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.824, 1.985],'-k',linewidth=0.3) #,clip_on=False

ax1.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('5%_gpl_injection_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.95         ; C1_2gas_J=0.95    ; C1_2huil_J=0
C1_2_s1=0.74        ; C1_2gas_s1=0.875   ; C1_2huil_s1=0.593
C1_2_s2=0.64        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39

#C1_2_J=0.05         ; C1_2gas_J=0.05    ; C1_2huil_J=0
#C1_2_s1=0.055        ; C1_2gas_s1=0.055   ; C1_2huil_s1=0.0625
#C1_2_s2=0.12        ; C1_2gas_s2=0.1   ; C1_2huil_s2=0.125
#C1_2_I=0.145         ; C1_2gas_I=0       ; C1_2huil_I=0.145

def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,0.5),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.5),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.5),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=0.5  ")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.493319,0.6586333],[0,0.6324,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 5% GPL à 220 BARG  RF= 65.86 %")
#format_axes(fig)

plt.show()

"""

#########################################################################
#------------------      Gas-Oil OMG-832 MOY   -----------------------
#------------------      GAS injection 8% GPL   ------------------------
#########################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.83,0.593),FC1_2(SS,0.02,0.233,0.83,0.593),'-y',label='Fc1-2 injection tie line ')
ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.69,0.83,0.593),0.02,0.233,0.83,0.593)
YM4=FC1_2v(Sgv(0.64,0.79,0.6),0.02,0.233,0.79,0.6)

ax1.plot([0.92,0.69,0.64,0.39],[0.92,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.77,0.64],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.92-YM5)/(0.92-0.69)
v2=(YM5-YM4)/(0.69-0.64)
v3=(YM4-0.39)/(0.64-0.39)

print("v1=" , v1)     #0.39130434782608714
print("v2=" , v2)     #0.8936216538854914
print("v3=" , v3)     #1.5812756692229017    0.6324
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.92,0.92,'ok',label='J ')

#plt.plot([0.68],[0.68],'*b',label='PP' )


ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.786, 1.985],'-k',linewidth=0.3) #,clip_on=False

#ax1.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('8%_gpl_injection_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.92         ; C1_2gas_J=0.92    ; C1_2huil_J=0
C1_2_s1=0.69        ; C1_2gas_s1=0.83   ; C1_2huil_s1=0.593
C1_2_s2=0.64        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39

#C1_2_J=0.05         ; C1_2gas_J=0.05    ; C1_2huil_J=0
#C1_2_s1=0.055        ; C1_2gas_s1=0.055   ; C1_2huil_s1=0.0625
#C1_2_s2=0.12        ; C1_2gas_s2=0.1   ; C1_2huil_s2=0.125
#C1_2_I=0.145         ; C1_2gas_I=0       ; C1_2huil_I=0.145

def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,1),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,1),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,1),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,1),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=1 Injection 8% GPL   RF= 61.77 % ")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.4654867,0.6177467],[0,0.6324,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 8% GPL à 220 BARG  RF= 61.77 %")
#format_axes(fig)

plt.show()

"""



#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      GAS injection 10% GPL   ------------------------
#########################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial and injection tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')



YM4=FC1_2v(Sgv(0.64,0.79,0.6),0.02,0.233,0.79,0.6)

ax1.plot([0.90,0.64,0.39],[0.90,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.77,0.64],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.9-YM4)/(0.9-0.64)
v3=(YM4-0.39)/(0.64-0.39)

print("v1=" , v1)     #0.4410810872856714
print("v3=" , v3)     #1.5812756692229017
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.9,0.9,'ok',label='J ')



ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('10%_gpl_injection_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.90         ; C1_2gas_J=0.90    ; C1_2huil_J=0
C1_2_s1=0.64        ; C1_2gas_s1=0.79   ; C1_2huil_s1=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39

def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s1)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s1)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s1)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,1),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,1),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,1),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,1),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=1 Injection 10% GPL   RF= 55.34 % ")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.422367,0.55337655],[0,0.6324,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v3],'--k' ,label='v2')
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 10% GPL à 220 BARG  RF= 55.34 %")
#format_axes(fig)

plt.show()

"""

#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      GAS injection 13% GPL   ------------------------
#########################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.745,0.61),FC1_2(SS,0.02,0.233,0.745,0.61),'-y',label='Fc1-2 injection tie line ')
ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.64,0.745,0.61),0.02,0.233,0.745,0.61)
YM4=FC1_2v(Sgv(0.6255,0.79,0.6),0.02,0.233,0.79,0.6)

ax1.plot([0.87,0.64,0.6255,0.39],[0.87,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.64,0.6255],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.87-YM5)/(0.87-0.64)
v2=(YM5-YM4)/(0.64-0.6255)
v3=(YM4-0.39)/(0.6255-0.39)

print("v1=" , v1)     #0.5530953632067798
print("v2=" , v2)     #0.9113956476616084
print("v3=" , v3)     #1.4419228431904347   1.441929
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.87,0.87,'ok',label='J ')


ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.707, 1.985],'-k',linewidth=0.3) #,clip_on=False

#plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('13%_gpl_injection_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.87         ; C1_2gas_J=0.87    ; C1_2huil_J=0
C1_2_s1=0.64        ; C1_2gas_s1=0.745   ; C1_2huil_s1=0.61
C1_2_s2=0.6255        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39


def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,1),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,1),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,1),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,1),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=1 Injection 13% GPL   RF= 64.14 %")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.5185093,0.64139],[0,0.76007,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 13% GPL à 220 BARG  RF= 64.14 %")
#format_axes(fig)

plt.show()

"""


#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      GAS injection 15.5% GPL   ------------------------
#########################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.7,0.625),FC1_2(SS,0.02,0.233,0.7,0.625),'-y',label="Fc1-2 ligne de raccordement d'injection ")
ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 ligne de raccordement initiale')


#ax1.plot(cc1TD(SS,0.745,0.61),FC1_2(SS,0.02,0.233,0.745,0.61),'--g',label='Fc1-2 ligne de raccordement passant par  M2 ')


YM5=FC1_2v(Sgv(0.64,0.7,0.625),0.02,0.233,0.7,0.625)
YM4=FC1_2v(Sgv(0.6193,0.79,0.6),0.02,0.233,0.79,0.6)

YM=FC1_2v(Sgv(0.705,0.745,0.61),0.02,0.233,0.745,0.61)

ax1.plot([0.845,0.705,0.6193,0.39],[0.845,YM,YM4,0.39],'-r',linewidth=1,label='chemin de solution ' )
#plt.plot([0.64,0.621],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.845-YM)/(0.845-0.705)
v2=(YM-YM4)/(0.705-0.6193)
v3=(YM4-0.39)/(0.6193-0.39)

print("v1=" , v1)     #0.7142857142857141
print("v2=" , v2)     #0.9779796292184891
print("v3=" , v3)     #1.1826739894285894    0.845542
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.845,0.845,'ok',label='J ')

#plt.plot([0.62],[YM1],'*r',label='M1' )
#plt.plot([0.6725],[YM2],'*y',label='M2' )
ax1.plot([0.705],[YM],'*g',label='M2' )


#plt.plot([0.68],[0.68],'*b',label='PP' )


ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.642, 1.985],'-k',linewidth=0.3) #,clip_on=False

#plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('15.5%_gpl_injection_pyM.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.845         ; C1_2gas_J=0.845    ; C1_2huil_J=0
C1_2_s1=0.705        ; C1_2gas_s1=0.745   ; C1_2huil_s1=0.61
C1_2_s2=0.6193        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39


def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,0.5),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.5),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.5),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=0.5 ")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.778772,0.901112],[0,0.845542,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 15.5% GPL à 220 BARG  RF= 90.11 %")
#format_axes(fig)

plt.show()
"""


#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      GAS injection 15% GPL   ------------------------
#########################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.7,0.625),FC1_2(SS,0.02,0.233,0.7,0.625),'-y',label='Fc1-2 injection tie line ')
ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.64,0.7,0.625),0.02,0.233,0.7,0.625)
YM4=FC1_2v(Sgv(0.621,0.79,0.6),0.02,0.233,0.79,0.6)

ax1.plot([0.85,0.64,0.621,0.39],[0.85,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.64,0.621],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.85-YM5)/(0.85-0.64)
v2=(YM5-YM4)/(0.64-0.621)
v3=(YM4-0.39)/(0.621-0.39)

print("v1=" , v1)     #0.7269850783074581
print("v2=" , v2)     #0.8728354608341232
print("v3=" , v3)     #1.2586548043272097        0.794499
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.85,0.85,'ok',label='J ')

ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.66, 1.985],'-k',linewidth=0.3) #,clip_on=False

#plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('15%_gpl_injection_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.85         ; C1_2gas_J=0.85    ; C1_2huil_J=0
C1_2_s1=0.64        ; C1_2gas_s1=0.7   ; C1_2huil_s1=0.625
C1_2_s2=0.621        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39


def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,1),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,1),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,1),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,1),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=1 Injection 15% GPL   RF= 76.89 %")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.6324796,0.7688819],[0,0.794499,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 15% GPL à 220 BARG  RF= 76.89 %")
#format_axes(fig)

plt.show()

"""
#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      GAS injection 13% GPL   ------------------------
#########################################################################

fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'-b',label='Fc1-2 ligne de raccordement initiale')

ax1.plot(cc1TD(SS,0.745,0.61),FC1_2(SS,0.02,0.233,0.745,0.61),'-g',label='Fc1-2 ligne de raccordement passant par  M2 ')


YM4=FC1_2v(Sgv(0.745,0.745,0.61),0.02,0.233,0.745,0.61)
YM5=FC1_2v(Sgv(0.62254,0.79,0.6),0.02,0.233,0.79,0.6)


ax1.plot([0.83,0.745,0.62254,0.39],[0.83,YM4,YM5,0.39],'-r',linewidth=1,label='chemin de solution ' )
#plt.plot([0.7,0.617],[YM4,YM5],'-r',linewidth=1,label='Solution Path ' )

v1=(0.83-YM4)/(0.83-0.67)
v2=(YM4-YM5)/(0.67-0.62254)
v3=(YM5-0.39)/(0.62254-0.39)

print("v1=" , v1)     #0.53125
print("v2=" , v2)     #0.9762988416682589
print("v3=" , v3)     #1.3273624192587272    0.753374

ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.83,0.83,'ok',label='J ')




plt.plot([0.745],[YM4],'*r',label='M2' )


ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
ax1.plot([0.6, 1.985], [0.678, 1.985],'-k',linewidth=0.3) #,clip_on=False

ax1.plot([0.59, 1.987], [0.5855, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('17%_gpl_injectionM2_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.83         ; C1_2gas_J=0.83    ; C1_2huil_J=0
C1_2_s1=0.67       ; C1_2gas_s1=0.745   ; C1_2huil_s1=0.61
C1_2_s2=0.62254        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39


def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,0.5),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.5),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.5),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=0.5")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.579123,0.733878],[0,0.753374,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 17% GPL point de melange en M2 à 220 BARG  RF= 73.39 %")
#format_axes(fig)

plt.show()


#########################################################################
#------------------  Gas-Oil OMG-832 Sample 3   -----------------------
#------------------      17 % GPL injection M3    ------------------------
######################################################################### 
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')

#plt.plot(cc1TD(SS,0.76,0.605),FC1_2(SS,0.02,0.233,0.76,0.605),'-r',label='Fc1-2 M1 ')
#plt.plot(cc1TD(SS,0.74,0.615),FC1_2(SS,0.02,0.233,0.74,0.615),'-y',label='Fc1-2 M2 ')
ax1.plot(cc1TD(SS,0.72,0.62),FC1_2(SS,0.02,0.233,0.72,0.62),'-g',label='Fc1-2 M3 ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')
YM1=FC1_2v(Sgv(0.625,0.76,0.605),0.02,0.233,0.76,0.605)
YM2=FC1_2v(Sgv(0.675,0.74,0.615),0.02,0.233,0.74,0.615)
YM3=FC1_2v(Sgv(0.7,0.72,0.62),0.02,0.233,0.72,0.62)

YM4=FC1_2v(Sgv(0.7,0.72,0.62),0.02,0.233,0.72,0.62)
YM5=FC1_2v(Sgv(0.617,0.79,0.6),0.02,0.233,0.79,0.6)

plt.plot([0.83,0.7,0.617,0.39],[0.83,YM4,YM5,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.7,0.617],[YM4,YM5],'-r',linewidth=1,label='Solution Path ' )

v1=(0.83-YM4)/(0.83-0.7)
v2=(YM4-YM5)/(0.7-0.617)
v3=(YM5-0.39)/(0.617-0.39)

print("v1=" , v1)     #0.846153846153846
print("v2=" , v2)     #0.9900975088481873
print("v3=" , v3)     #1.091726461522469   1/v3=0.91598036
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.83,0.83,'ok',label='J ')

plt.plot([0.7],[YM3],'*g',label='M3' )



plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.679, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.621, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.plot([0.59, 1.987], [0.5855, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('gplinjectionOMJ-323_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.83         ; C1_2gas_J=0.83    ; C1_2huil_J=0
C1_2_s1=0.7        ; C1_2gas_s1=0.72   ; C1_2huil_s1=0.62
C1_2_s2=0.617        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39
def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,0.5),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.5),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.5),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=1 ")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.8879837,0.9602033],[0,0.91598036,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 17% GPL à 220 BARG  RF= 96.02 %")
#format_axes(fig)

plt.show()
"""





#########################################################################
#------------------  Gas-Oil OMG-832 Sample 3   -----------------------
#------------------      17 % GPL injection     ------------------------
######################################################################### 

fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])


  


ax1.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


ax1.plot([0.83,0.39],[0.83,0.39],'-r',linewidth=3,label='Solution Path ' )
#plt.plot([0.7,0.617],[YM4,YM5],'-r',linewidth=1,label='Solution Path ' )

v1=v2=v3=1

print("v1=" , v1)     #0.846153846153846
print("v2=" , v2)     #0.9900975088481873
print("v3=" , v3)     #1.091726461522469
ax1.plot(0.39,0.39,'*k',label='I ')
ax1.plot(0.83,0.83,'ok',label='J ')




ax1.plot([0.66],[0.66],'*r',label='M3' )


ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.plot([0.59, 1.987], [0.5855, 1.985],'-k',linewidth=0.3) #,clip_on=False


ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('Fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('17%_gpl_injection_py.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])

C1_2_J=0.83         ; C1_2gas_J=0.83    ; C1_2huil_J=0
C1_2_s1=0.7        ; C1_2gas_s1=0.72   ; C1_2huil_s1=0.62
C1_2_s2=0.617        ; C1_2gas_s2=0.79   ; C1_2huil_s2=0.6
C1_2_I=0.39          ; C1_2gas_I=0       ; C1_2huil_I=0.39
def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2_I)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2gas_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2gas_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2gas_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2gas_I)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(C1_2huil_J)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(C1_2huil_s1)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(C1_2huil_s2)
        elif XD[i]>(v3*TD):
            a.append(C1_2huil_I)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,1),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,1),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,1),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,1),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=1 Injection 17% GPL   RF= 100 % ")#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,1],[0,1],'-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v')

ax6.text(0.3, 0.6, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 17% GPL à 220 BARG  RF= 100 %")
#format_axes(fig)

plt.show()







"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])

# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax1.plot(cc1TD(SS,0.82,0.635),FC1_2(SS,0.1185,0.233,0.82,0.635),'-b',label='ligne de raccordement initiale ')
ax1.plot(cc1TD(SS,0.91,0.62),FC1_2(SS,0.1185,0.233,0.91,0.62),'-y',label="ligne de raccordement d'injection")


#YM1=FC1_2v(Sgv(0.74,0.77,0.66),0.1185,0.233,0.77,0.66)
#YM6=fC1_2v(Sgv(0.69,0.8,0.68),0.1185,0.2448,0.8,0.68)
ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.68, 2], [0.772, 2],'-k',linewidth=1) #,clip_on=False
ax1.plot([0.98,0.828,0.73,0.4],[0.98,0.91,0.82,0.4],'-r',label='chemin de solution ' )
ax1.plot(0.4,0.4,'*g',label='I ')
ax1.plot(0.98,0.98,'*k',label='J ')


v1=(0.98-0.91)/(0.98-0.828)
v2=(0.91-0.82)/(0.828-0.73)
v3=(0.82-0.4)/(0.73-0.4)
#d=v1*t  t=d/v1


#plt.plot([0.785, 2], [YM3, 2],'-k',linewidth=1) #,clip_on=False
ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('fc1-2')
ax1.set_title("flux fractionnaire de pseudo-composé C1-2 à 220 BARG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('GASINJECTION_PY.png')
plt.imshow(img)

ax2.tick_params(labelbottom=False, labelleft=False)
ax3 = fig.add_subplot(gs[0, -2:])
def C1_2(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(0.98)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(0.83)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(0.73)
        elif XD[i]>(v3*TD):
            a.append(0.4)
    return a
def C1_2gas(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(0.98)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(0.91)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(0.82)
        elif XD[i]>(v3*TD):
            a.append(0.0)
    return a
def C1_2huil(XD,TD):
    a=[]
    for i in range(len(XD)):
        if XD[i]<=(v1*TD):
            a.append(0.)
        elif (v1*TD)<XD[i]<=(v2*TD):
            a.append(0.62)
        elif (v2*TD)<XD[i]<=(v3*TD):
            a.append(0.635)
        elif XD[i]>(v3*TD):
            a.append(0.4)
    return a
def So(XD,TD):
    a=[]
    for i in range(len(XD)):
        a.append((C1_2(XD,TD)[i]-C1_2gas(XD,TD)[i])/(C1_2huil(XD,TD)[i]-C1_2gas(XD,TD)[i]))
    return a
#1.7      0.2
#1.05    x    x=0.724
#0.7     y    y=0.133    y*z+x=0.03607+0.724 =0.76007      
#0.85       0.2
#1.15      z=0.271
#Sg*c1g+So*c1o=cc1........(1-So-Swc)*c1g+So*c1o=cc1.......c1g+(-So-Swc)*c1g+So*c1o=cc1
#So(c1o-c1g)=cc1-c1g+Swc*c1g.........So=(cc1-c1g+Swc*c1g)/(c1o-c1g)  So=(cc1+(Swc-1)*c1g)/(c1o-c1g)   So=(cc1-0.91*c1g)/(c1o-c1g)   A=((C1_2-c1o+0.09*c1o)/(c1g-c1o))
XD = np.arange(0., 1., 0.001)
ax3.plot(XD,C1_2(XD,0.1),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.1),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.1),'--b',label='C1_2huile')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de composition à TD=0.5 (injection de gaz assosié)")
#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.0964,0.19216,0.2882255,0.38891,0.484264,0.5855,0.678546,0.772724,
          0.799026,0.8348511],[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
         '-y' ,label='huile produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huile")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huile")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huile en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huile + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection de gaz associé à 220 BARG ")
#format_axes(fig)

plt.show()
"""