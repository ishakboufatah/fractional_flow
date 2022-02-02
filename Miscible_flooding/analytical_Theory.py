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
#------------------      GAS injection    ------------------------
#########################################################################  

plt.figure(figsize=(7,7))

plt.plot(cc1TD(SS,0.9,0.59),FC1_2(SS,0.02,0.233,0.9,0.59),'-y',label='Fc1-2 injection tie line ')
plt.plot(cc1TD(SS,0.79,0.6),FC1_2(SS,0.02,0.233,0.79,0.6),'--b',label='Fc1-2 initial tie line ')


#plt.plot(cc1TD(SS,0.785,0.675),fC1_2(SS,0.1185,0.2448,0.785,0.675),'--g',label='fc1-2 M5 ')


YM5=FC1_2v(Sgv(0.77,0.9,0.59),0.02,0.233,0.9,0.59)
YM4=FC1_2v(Sgv(0.64,0.79,0.6),0.02,0.233,0.79,0.6)

plt.plot([0.98,0.77,0.64,0.39],[0.98,YM5,YM4,0.39],'-r',linewidth=1,label='Solution Path ' )
#plt.plot([0.77,0.64],[YM5,YM4],'-r',linewidth=1,label='Solution Path ' )

v1=(0.98-YM5)/(0.98-0.77)
v2=(YM5-YM4)/(0.77-0.64)
v3=(YM4-0.39)/(0.64-0.39)

print("v1=" , v1)     #0.3809523809523808
print("v2=" , v2)     #0.8821621745713428
print("v3=" , v3)     #1.5812756692229017
plt.plot(0.39,0.39,'*k',label='I ')
plt.plot(0.98,0.98,'ok',label='J ')

#plt.plot([0.62],[YM1],'*r',label='M1' )
#plt.plot([0.6725],[YM2],'*y',label='M2' )
#plt.plot([0.685],[YM3],'*g',label='M3' )


#plt.plot([0.68],[0.68],'*b',label='PP' )


plt.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.6, 1.985], [0.749, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.64, 1.985], [0.88, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.plot([0.6, 1.985], [0.586, 1.985],'-k',linewidth=0.3) #,clip_on=False
plt.plot([0.6, 1.985], [0.5917, 1.985],'-k',linewidth=0.3) #,clip_on=False

plt.xlabel('Cc1-2')
plt.ylabel('Fc1-2')
plt.title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
plt.legend()
plt.axis([0.35, 1,0.35, 1])
plt.show()    
   
   

#########################################################################
#------------------  Gas-Oil OMG-832 MOY   -----------------------
#------------------      17 % GPL injection    ------------------------
######################################################################### 


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
#------------------      GAS injection    ------------------------
#########################################################################

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
fig.suptitle("Injection GAS assoscié à 220 BARG  RF= 69.65 %")
#format_axes(fig)

plt.show()















#########################################################################
#------------------  Gas-Oil OMG-832 Sample 3   -----------------------
#------------------      17 % GPL injection    ------------------------
######################################################################### 

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