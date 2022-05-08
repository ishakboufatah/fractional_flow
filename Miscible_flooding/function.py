# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 17:40:43 2021

@author: ishak
"""

import numpy as np

##############################################################################
##############################################################################
#                               ECLIPSE SCAL
##############################################################################
##############################################################################
def Kr_oil_w(Sw):
    function=1*((1-Sw-0.44)/(1-0.44))**1.5
    return function
"""
def Kr_oil_g(Sg):
    function=1*((1-Sg-0.39)/(1-0.39))**1.5
    return function
"""
def Kr_oil_g(Sg):
    a=[]
    for value in Sg:
        if value<=0.61:
            a.append(1*((1-value-0.39)/(1-0.39))**1.5)
        elif value>0.61:
            a.append(0)
    return a

def Kr_oil_gv(Sg):  
    if Sg<=0.61:
        a=(1*((1-Sg-0.39)/(1-0.39))**1.5)
    elif Sg>0.61:
        a=(0)
    return a

def Kr_gas(Sg):
    a=[]
    for value in Sg:
        #print(value)
        if value<=0.1:
            a.append(0)
        elif 0.1<value<=0.61:
            a.append(0.55*((value-0.1)/(1-0.1-0.39))**1.9)
        elif value>0.61:
            a.append(((0.95-0.55)/(1-0.61))*(value-0.61)+0.55) 
        #print(a)
    return a

def Kr_gasv(Sg):
    if Sg<=0.1:
        a=(0)
    elif 0.1<Sg<=0.61:
        a=(0.55*((Sg-0.1)/(1-0.1-0.39))**1.9)
    elif Sg>0.61:
        a=(((0.95-0.55)/(1-0.61))*(Sg-0.61)+0.55) 
    return a

#print(Kr_gas(SS))
#####################################################################
#                           Fractional Flow
#####################################################################

def fg(Sg,vg,vo):
    A=[]
    for i in range(len(Sg)):
        A.append(1/(1+((Kr_oil_g(Sg)[i]*vg)/(Kr_gas(Sg)[i]*vo))))
    return A

def fgv(Sg,vg,vo):
    A=(1/(1+((Kr_oil_gv(Sg)*vg)/(Kr_gasv(Sg)*vo))))
    return A
#######################################################################
#                             Fractional Flux of CH4
#######################################################################
def cc1TD(Sg,c1g,c1o):
    A=[]
    for i in range(len(Sg)):
        #A.append(Sg[i]*c1g+c1o-Sg[i]*c1o)
        A.append(Sg[i]*(c1g-c1o)+c1o)
    return A
def Sgv(C1_2,c1g,c1o):
    A=((C1_2-c1o)/(c1g-c1o))
    return A

def fC1_2(sg,vg,vo,cg,co):
    A=[]
    for i in range(len(sg)):
        #A.append(fg(sg,vg,vo)[i]*cg+(1-fg(sg,vg,vo)[i])*co)
        #A.append(F(so,sg,vg,vo,k)[i]*cg+co-F(so,sg,vg,vo,k)[i]*co)
        A.append(fg(sg,vg,vo)[i]*(cg-co)+co)
    return A

def fC1_2v(sg,vg,vo,cg,co):
    A=(fgv(sg,vg,vo)*(cg-co)+co)
    return A

##############################################################################
##############################################################################
#                               EPIRIMENT SCAL
##############################################################################
       
"""
#Gas-Oil OMJ-323 Sample 4
ng=3.5
no=5.7
Sgr=0.0
Krg0=0.7274
Sg0=0.789
Sr=0.211
Sor=0.121
Swc=0.09


#  Gas-Oil OMG-832 Sample 3
ng=3.4
no=10.5
Sgr=0.00588367
Krg0=0.2571
Sg0=0.2883
Sr=0.71758367
Sor=0.4877
Swc=0.224

#  Gas-Oil OMG-832 Sample 14
ng=2.5
no=7
Sgr=0.0267816
Krg0=0.5
Sg0=0.3523
Sr=0.6744816
Sor=0.24
Swc=0.4077
"""
#  Gas-Oil OMG-832 MOY
ng=2.95
no=8.75
Sgr=0.016332635
Krg0=0.37855
Sg0=0.3203
Sr=0.696032635
Sor=0.36385
Swc=0.31585

def Kr_oil_G(Sg):
    a=[]
    for value in Sg:
        if value<(Sg0):
            a.append(1*((1-value-Sor)/(1-Sor-Sgr))**no) #0.0483
        elif value>=(Sg0):
            a.append(0)
    return a

def Kr_oil_(Sg):
    a=[]
    for value in Sg:
        a.append(1*((value-Sor)/(1-Sor-Sgr))**no) #0.0483
        #if value<(1-Sg0):
         #   a.append(1*((value-Sor)/(1-Sor-Sgr))**no) #0.0483
        #elif value>=(1-Sg0):
        #    a.append(0)
    return a

def Kr_oil_GV(Sg):     #So=1-Sg-Swr-Sgr
    if Sg<Sg0:
        a=(1*((1-Sg-Sor)/(1-Sor))**no)
    elif Sg>=Sg0:
        a=(0)
    return a




def Kr_GAS(Sg):
    a=[]
    for value in Sg:
        #print(value)
        if value<=Sgr:
            a.append(0)
        elif Sgr<value<=Sg0:
            a.append(Krg0*((value-Sgr)/(1-Sr))**ng) #0.7274
        elif value>Sg0:
            a.append(np.nan)
        #print(a)
    return a

def Kr_GASV(Sg):
    if Sg<=Sgr:
        a=(0)
    elif Sgr<Sg<=Sg0:
        a=(Krg0*((Sg-Sgr)/(1-Sr))**ng)
    elif Sg>Sg0:
        a=np.nan 
    return a
#####################################################################
#                           Fractional Flow
#####################################################################

def FG(Sg,vg,vo):
    A=[]
    for i in range(len(Sg)):
        if Sg[i]<=Sg0:
            A.append(1/(1+((Kr_oil_G(Sg)[i]*vg)/(Kr_GAS(Sg)[i]*vo))))
        elif Sg[i]>Sg0:
            A.append(1)
    return A

def FGv(Sg,vg,vo):
    if Sg<=Sg0:
        A=(1/(1+((Kr_oil_GV(Sg)*vg)/(Kr_GASV(Sg)*vo))))
    elif Sg>Sg0:
        A=(1)
    return A
#######################################################################
#                             Fractional Flux of CH4
#######################################################################
#Sg*c1g+So*c1o=cc1........Sg*c1g+(1-Sg-Swc)*c1o=cc1.......Sg*c1g+c1o-Sg*c1o-Swc*c1o=cc1
#Sg(c1g-c1o)=cc1-c1o+Swc*c1o.........Sg=(cc1-c1o+Swc*c1o)/(c1g-c1o)
def CC1TD(Sg,c1g,c1o):
    A=[]
    for i in range(len(Sg)):
        #A.append(Sg[i]*c1g+c1o-Sg[i]*c1o)
        #A.append(Sg[i]*(c1g-c1o)+c1o)
        A.append(Sg[i]*(c1g-c1o)+c1o+c1o*Swc)
    return A
def SGv(C1_2,c1g,c1o):
    A=((C1_2-c1o+Swc*c1o)/(c1g-c1o))
    return A

def FC1_2(sg,vg,vo,cg,co):
    A=[]
    for i in range(len(sg)):
        #A.append(fg(sg,vg,vo)[i]*cg+(1-fg(sg,vg,vo)[i])*co)
        #A.append(F(so,sg,vg,vo,k)[i]*cg+co-F(so,sg,vg,vo,k)[i]*co)
        A.append(FG(sg,vg,vo)[i]*(cg-co)+co)
    return A

def FC1_2v(sg,vg,vo,cg,co):
    A=(FGv(sg,vg,vo)*(cg-co)+co)
    return A

