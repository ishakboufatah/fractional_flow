# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 17:54:30 2021

@author: ishak
"""
import matplotlib.pyplot as plt
import numpy as np
from data import *
from function import Kr_oil_w,Kr_oil_g,Kr_gas,fg,fC1_2,cc1TD,fC1_2v,Kr_oil_G,Kr_GAS,FG,FC1_2,FC1_2v,Sgv
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

#plt.plot(Sg,Krg, 'og',label='gas relative permeability Krg ')
plt.plot(SG,KrG, 'og',label='Expirimental gas relative permeability ')
#plt.plot(SS,Kr_gas(SS),'-g',label='gas relative permeability function')
plt.plot(SS,Kr_GAS(SS),'-g',label='gas relative permeability function')
#plt.plot(Sg,Krog,'ro',label='SCAL oil relative permeability')
plt.xlabel('Sg')
plt.ylabel('Kr')
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()
#print(SS)
#print(SS[2])
#print(Kr_gas(SS))


#plt.plot(Sg,Krog,'ro',label='oil relative permeability Kro')
plt.plot(SG,KrO,'ro',label='Expirimental oil relative permeability')
#plt.plot(SS,Kr_oil_g(SS),'-r',label='oil relative permeability function')
plt.plot(SS,Kr_oil_G(SS),'-r',label='oil relative permeability function')
plt.xlabel('Sg')
plt.ylabel('Kr')
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()
#print(SS)
#print(Kr_oil_G(SS))


#######################################################################
#                             Fractional Flow OG gas
#######################################################################
"""
#plt.plot(Sg,Krog,'ro',label='oil relative permeability Kro')
plt.plot(SS,fg(SS,0.1185,0.2448),'-r',label='fg à 275.79 BARSG ECLIPSE SCAL')
#plt.plot(SS,fg(SS,0.1185,0.2165),'-b',label='fg à 275.79 BARSG khaled')
plt.plot(SS,FG(SS,0.1185,0.2448),'-b',label='fg à 275.79 BARSG EXP SCAL')
plt.xlabel('Sg')
plt.ylabel('fg')
plt.title("débit fractionnaire de gaz")
plt.legend()
plt.axis([0, 1., 0, 1.3])
plt.show()

#######################################################################
#                             Fractional Flux of C1-2
#######################################################################
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
"""
#########################################################################
"""
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
ax1.set_title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
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
ax3.plot(XD,C1_2(XD,0.5),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.5),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.5),'--b',label='C1_2huil')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de concentration à TD=0.5")
#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.925472561,0.986890975],[0,1/v2,1],'-y' ,label='huil produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huil")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huil")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.text(0.65, 0.7, "2 phases huil + gaz", va="center", ha="center")
ax6.text(0.3, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.4, "huil en place", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 12% GPL à 220 BARG (point de mélange en M)")
#format_axes(fig)

plt.show()

##############################################################################
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])

# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax1.plot(cc1TD(SS,0.82,0.635),FC1_2(SS,0.1185,0.233,0.82,0.635),'-b',label='ligne de raccordement initiale ')
#ax1.plot(cc1TD(SS,0.77,0.66),FC1_2(SS,0.1185,0.233,0.77,0.66),'-y',label='ligne de raccordement passant par M')


#YM1=FC1_2v(Sgv(0.74,0.77,0.66),0.1185,0.233,0.77,0.66)
#YM6=fC1_2v(Sgv(0.69,0.8,0.68),0.1185,0.2448,0.8,0.68)
ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
ax1.plot([0.88,0.7,0.4],[0.88,0.7,0.4],'-r',label='chemin de solution ' )
ax1.plot(0.4,0.4,'*g',label='I ')
ax1.plot(0.88,0.88,'*k',label='J ')
ax1.plot([0.7],[0.7],'*b',label='PP' )

v1=(0.88-0.7)/(0.88-0.7)
v2=(0.7-0.4)/(0.7-0.4)
#d=v1*t  t=d/v1

#plt.plot([0.68, 2], [0.8, 2],'-k',linewidth=1) #,clip_on=False
#plt.plot([0.785, 2], [YM3, 2],'-k',linewidth=1) #,clip_on=False
ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('fc1-2')
ax1.set_title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
ax1.legend()
ax1.axis([0., 1.,0., 1.])
ax2 = fig.add_subplot(gs[0, -3])
#ax2.set_size_inches(5, 5)
img = mpimg.imread('GPLINJECTIONPP_PY.png')
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
ax3.plot(XD,C1_2(XD,0.5),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.5),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.5),'--b',label='C1_2huil')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de concentration à TD=0.5")
#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,1],[0,1],'-y' ,label='huil produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huil")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huil")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.text(0.3, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.4, "huil en place", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection 12% GPL à 220 BARG (point de mélange en P)")
#format_axes(fig)

plt.show()
"""
"""
fig = plt.figure(constrained_layout=False)
#fig.figsize=(10,10)
fig.set_size_inches(20, 12.8)
gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, -4])

# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax1.plot(cc1TD(SS,0.82,0.635),FC1_2(SS,0.1185,0.233,0.82,0.635),'-b',label='ligne de raccordement initiale ')
ax1.plot(cc1TD(SS,0.91,0.62),FC1_2(SS,0.1185,0.233,0.91,0.62),'-y',label="ligne de raccordement d'injaction")


#YM1=FC1_2v(Sgv(0.74,0.77,0.66),0.1185,0.233,0.77,0.66)
#YM6=fC1_2v(Sgv(0.69,0.8,0.68),0.1185,0.2448,0.8,0.68)
ax1.plot([0.0,2],[0.0,2],'-k' )#,clip_on=False)
plt.plot([0.68, 2], [0.77, 2],'-k',linewidth=1) #,clip_on=False
ax1.plot([0.98,0.83,0.735,0.4],[0.98,0.91,0.82,0.4],'-r',label='chemin de solution ' )
ax1.plot(0.4,0.4,'*g',label='I ')
ax1.plot(0.98,0.98,'*k',label='J ')


v1=(0.98-0.91)/(0.98-0.83)
v2=(0.91-0.82)/(0.83-0.735)
v3=(0.82-0.4)/(0.735-0.4)
#d=v1*t  t=d/v1


#plt.plot([0.785, 2], [YM3, 2],'-k',linewidth=1) #,clip_on=False
ax1.set_xlabel('Cc1-2')
ax1.set_ylabel('fc1-2')
ax1.set_title("flux fractionnaire de psudocomposé C1-2 à 220 BARSG")
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
            a.append(0.735)
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
ax3.plot(XD,C1_2(XD,0.5),'-g',label='C1_2')    
ax3.plot(XD,C1_2gas(XD,0.5),'--r',label='C1_2gas') 
ax3.plot(XD,C1_2huil(XD,0.5),'--b',label='C1_2huil')
ax3.plot(XD,So(XD,0.5),'--y',label='So')    
ax3.legend()
ax3.axis([0., 1.,0., 1.0])
ax3.set_xlabel('Position adimentionel XD')
ax3.set_ylabel('profile')
ax3.set_title("Profile de concentration à TD=0.5")
#ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax4 = fig.add_subplot(gs[1:, -3])
ax4.plot([0,0.782356,0.8391],[0,1/v3,1],'-y' ,label='huil produit')
ax4.legend()
ax4.axis([0., 1.,0., 1.])
ax4.invert_xaxis()
ax4.set_xlabel("Récuperation d'huil")
ax4.set_ylabel('temps adimentionel TD')
ax4.set_title("production d'huil")
#ax5 = fig.add_subplot(gs[1:, -3])
ax6 = fig.add_subplot(gs[-2:, -2:])
ax6.plot([0,1],[0,1/v1],'-k' ,label='v1')
ax6.plot([0,1],[0,1/v2],'--k' ,label='v2')
ax6.plot([0,1],[0,1/v3],'-k' ,label='v3',linewidth=3)
ax6.text(0.2, 0.8, "gaz injecté", va="center", ha="center")
ax6.text(0.8, 0.3, "huil en place", va="center", ha="center")
ax6.text(0.65, 0.7, "2 phases huil + gaz", va="center", ha="center")
ax6.text(0.5, 0.98, "diagramme distance-temps", va="center", ha="center")
ax6.legend()
ax6.axis([0., 1.,0., 1.])
ax6.set_xlabel("position adimentionel XD")
ax6.set_ylabel('temps adimentionel TD')
#ax6.set_title("diagramme distance-temps ")
fig.suptitle("Injection gaz associé à 220 BARG ")
#format_axes(fig)

plt.show()
"""