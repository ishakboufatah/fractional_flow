# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 12:48:27 2020

@author: ishak
"""
import numpy as np
import openpyxl  as xl
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.lines as lines
F=xl.load_workbook('F.xlsx',data_only=True)

#DATA= F['CO2_177_509m']
DATA= F['REINJ_80per_509m']
SOO= DATA['B']    #on a pris la colomn O dans Test comme input 1
SGG= DATA['C']    #on a pris la colomn M dans Test comme input 2
SWW= DATA['D']    #on a pris la colomn M dans Test comme input 2
C1G= DATA['E']    #on a pris la colomn G dans Test comme input 3
C1O= DATA['F']    #on a pris la colomn G dans Test comme input 3
CC1= DATA['G']    #on a pris la colomn G dans Test comme input 3
MUO= DATA['H']    #on a pris la colomn N dans Test comme input 4
MUG= DATA['I']
MOBW= DATA['J']
KROO= DATA['K']
KRGG= DATA['L']
FGG= DATA['M']
KM= DATA['N']

SOO20= DATA['Q']    #on a pris la colomn O dans Test comme input 1
SGG20= DATA['R']    #on a pris la colomn M dans Test comme input 2
SWW20= DATA['S']    #on a pris la colomn M dans Test comme input 2
C1G20= DATA['T']    #on a pris la colomn G dans Test comme input 3
C1O20= DATA['U']    #on a pris la colomn G dans Test comme input 3
CC120= DATA['V']    #on a pris la colomn G dans Test comme input 3
MUO20= DATA['W']    #on a pris la colomn N dans Test comme input 4
MUG20= DATA['X']
MOBW20= DATA['Y']
KROO20= DATA['Z']
KRGG20= DATA['AA']
FGG20= DATA['AB']
KM20= DATA['AC']

sgg=[]
soo=[]
sww=[]
muo=[]
mug=[]
mobw=[]
kroo=[]
krgg=[]
fgg=[]
km=[]
kmmis=[]
c1o=[]
c1g=[]
cc1=[]
sgg20=[]
soo20=[]
sww20=[]
muo20=[]
mug20=[]
mobw20=[]
kroo20=[]
krgg20=[]
fgg20=[]
km20=[]
kmmis20=[]
c1o20=[]
c1g20=[]
cc120=[]

#len(SOO)
for i in range(1,len(SOO)):
    soo.append(SOO[i].value)
    sgg.append(SGG[i].value)
    sww.append(SWW[i].value)
    muo.append(MUO[i].value)
    mug.append(MUG[i].value)
    mobw.append(MOBW[i].value)
    kroo.append(KROO[i].value)
    krgg.append(KRGG[i].value)
    fgg.append(FGG[i].value)
    km.append(KM[i].value)
    kmmis.append(1)
    soo20.append(SOO20[i].value)
    sgg20.append(SGG20[i].value)
    sww20.append(SWW20[i].value)
    muo20.append(MUO20[i].value)
    mug20.append(MUG20[i].value)
    mobw20.append(MOBW20[i].value)
    kroo20.append(KROO20[i].value)
    krgg20.append(KRGG20[i].value)
    fgg20.append(FGG20[i].value)
    km20.append(KM20[i].value)
    kmmis20.append(0)
    c1o.append(C1O[i].value)
    c1g.append(C1G[i].value)
    cc1.append(CC1[i].value)
    c1o20.append(C1O20[i].value)
    c1g20.append(C1G20[i].value)
    cc120.append(CC120[i].value)
          
soo=np.array(soo)
sgg=np.array(sgg)
sww=np.array(sww)
muo=np.array(muo)
mug=np.array(mug)
mobw=np.array(mobw)
kroo=np.array(kroo)
krgg=np.array(krgg)
fgg=np.array(fgg)
km=np.array(km)
kmmis=np.array(kmmis)
soo20=np.array(soo20)
sgg20=np.array(sgg20)
sww20=np.array(sww20)
muo20=np.array(muo20)
mug20=np.array(mug20)
mobw20=np.array(mobw20)
kroo20=np.array(kroo20)
krgg20=np.array(krgg20)
fgg20=np.array(fgg20)
km20=np.array(km20)
kmmis20=np.array(kmmis20)
c1o=np.array(c1o)
c1g=np.array(c1g)
cc1=np.array(cc1)
c1o20=np.array(c1o20)
c1g20=np.array(c1g20)
cc120=np.array(cc120)




def print_rows():
     for row in DATA.iter_rows(values_only=True):
         print(row)
Sog1=[0.84,0.8,0.76,0.72,0.68,0.6,0.56,0.52,0.48,0.44,0.4,0.28,0.24,0.2,0.16]
Kro1=[0,0,0,0.005,0.012,0.06,0.082,0.112,0.112,0.15,0.196,0.4,0.513,0.65,0.8]
Kro11=[0.8,0.65,0.513,0.4,0.196,0.15,0.112,0.112,0.082,0.06,0.012,0.005,0,0,0]

Sg1=[0.16,0.2,0.24,0.28,0.4,0.44,0.48,0.52,0.56,0.6,0.68,0.72,0.76,0.8,0.84]
Krg1=[0.04,0.058,0.078,0.1,0.187,0.222,0.26,0.3,0.349,0.4,0.505,0.562,0.62,0.68,0.74]
Krg11=[0.74,0.68,0.62,0.562,0.505,0.4,0.349,0.3,0.26,0.222,0.187,0.1,0.078,0.058,0.04]





So=[0.28,0.32,0.36,0.4,0.44,0.48,0.52,0.56,0.6,0.68,0.72,0.76,0.8,0.84]
Kro=[0.005,0.012,0.024,0.06,0.082,0.112,0.112,0.15,0.196,0.315,0.4,0.513,0.65,0.8]

#So=[0,0.04,0.08,0.12,0.16,0.2,0.24,0.28,0.32,0.36,0.4,0.44,0.48,0.52,0.56,0.6,0.68,0.72,0.76,0.8,0.84]
#Kro=[0,0,0,0,0,0,0,0.005,0.012,0.024,0.06,0.082,0.112,0.112,0.15,0.196,0.315,0.4,0.513,0.65,0.8]

Sg=[0,0.04,0.08,0.12,0.16,0.2,0.24,0.28,0.32,0.36,0.4,0.44,0.48,0.52,0.56,0.6,0.68,0.72,0.76,0.8,0.84]
Krg=[0,0.005,0.013,0.026,0.04,0.058,0.078,0.1,0.126,0.156,0.187,0.222,0.26,0.3,0.349,0.4,0.505,0.562,0.62,0.68,0.74]

Sw=[0.16,0.2,0.24,0.28,0.32,0.36,0.4,0.44,0.48,0.52,0.56,0.6,0.64,0.68,0.72,0.76,0.8,0.84,0.88,0.92,0.96,1]
Krw=[0,0.002,0.01,0.02,0.033,0.049,0.066,0.09,0.119,0.15,0.186,0.227,0.277,0.33,0.39,0.462,0.54,0.62,0.71,0.8,0.9,1]

SS = np.arange(0., 1., 0.07)
CC=[1]*len(SS)
CC05=[0.5]*len(SS)
CC0=[0]*len(SS)

M01=[1]*len(SS)
M10=[10]*len(SS)

CCmuo=[0.1]*len(SS)
CCmuo=np.array(CCmuo)
CCmug=[0.05]*len(SS)
CCmug=np.array(CCmug)
CCmobw=[0]*len(SS)
CCmobw=np.array(CCmobw)
CC=np.array(CC)
CC0=np.array(CC0)
CC05=np.array(CC05)





Sog=[]
for i in range(len(So)):
    Sog.append(1-So[i])



def perm_w(x):
    perm_w=((x-0.16)/(1-0.16))**2.3
    return perm_w   

#def SRO(x):
 #   return 0.26*x
    



SOR20=[]
for k in range(len(km20)):
    SOR20.append(km20[k]*0.26)
SOR20=np.array(SOR20)
print(SOR20)
print(len(SOR20))
print(len(soo20))



KOR20=[]
for k in range(len(km20)):
    KOR20.append((1-km20[k])*1+km20[k]*0.8)
KOR20=np.array(KOR20)
print('KOR20')
print(KOR20)
print(len(KOR20))
print(len(soo20))

def perm_o(x,K):
    SOR=[]

    for a in range(len(K)):
        SOR.append(K[a]*0.24)
    SOR=np.array(SOR)
    KOR=[]

    for a in range(len(K)):
        KOR.append((1-K[a])*1+K[a]*0.8)
    KOR=np.array(KOR)
    
    perm=[]
    for c in range(len(x)):
        if x[c] < SOR[c]:
            perm_o=0
            #perm_o=0.8*((x[c]-y[c])/(1-y[c]-0.16))**2.8
            #perm_o=nan
            #♠perm_o=0.8*((c-0.26)/(1-0.26-0.16))**1
            perm.append(perm_o)
        elif x[c] >= SOR[c]:
            #perm_o=0.8*((x[c]-0.24)/(1-0.24-0.16))**2.8
            perm_o=0.8*((x[c]-SOR[c])/(1-SOR[c]-0.16))**2.4
            perm.append(perm_o)
            #if  np.isnan(perm_o):
             #   perm.append(0)
            #else:
             #   perm.append(perm_o)
    return perm
                
                #8perm_o=np.power(0.81*((x-0.24)/(1-0.24-0.16)),1)  
    
"""
def perm_om(x,k):
    SOR=[]
    for a in range(len(k)):
        SOR.append(k[a]*0.24)
        
   #perm_om=perm_o(x)*(k)+(1-k)*x
    
    perm_om=perm_o(x,k)*(k)+(1-k)*(x-SOR)    
    
    #perm_om=perm_o(x)*(k)+(0.64-k)*(x-0.04)*2
    
      
            
    #perm_om=(x-0.23)*k+(1-k)*x*0.81
    return perm_om

"""
def perm_om(x,k):
    SOR=[]
    perm=[]
    for a in range(len(k)):
        SOR.append(k[a]*0.24)
    #perm_om=perm_o(x)*(k)+(1-k)*x
    for i in range(len(x)):
        #perm_om=perm_o(x,k)[i]*(k[i])+(1-k[i])*(x[i]-SOR[i])   *1.06
        perm_om=perm_o(x,k)[i]*(k[i])+(1-k[i])*((x[i]-SOR[i]))
    
    #perm_om=perm_o(x)*(k)+(0.64-k)*(x-0.04)*2
    
        if perm_om >=0:
            perm.append(perm_om)
        elif perm_om<0:
            perm.append(0)
            
    #perm_om=(x-0.23)*k+(1-k)*x*0.81
    return perm



#æ=[]
def perm_g1(x,K):
    SGR=[]
    for a in range(len(K)):
        SGR.append(K[a]*0.04)
    SGR=np.array(SGR)
    perm=[]
    for c in range(len(K)):
        if x[c] < SGR[c]:
            perm.append(0)
        elif x[c] >= SGR[c]:
            #perm_g=0.74*((x[c]-SGR[c])/(1-SGR[c]-0.16))**1.7
            perm_g=0.74*((x[c]-0.04)/(1-0.04-0.16))**1.7
            if  np.isnan(perm_g):
                perm.append(0)
            else:
                perm.append(perm_g)
   
    return perm
"""
æ=perm_g1(SS,CC)
print('æ')
print(æ)
print(len(æ))
"""
def perm_gm1(x,k):
    SGR=[]
    perm=[]
    for a in range(len(k)):
        SGR.append(k[a]*0.04)
    SGR=np.array(SGR)
    for i in range(len(x)):
        perm_gm=perm_g1(x,k)[i]*(k[i])+(1-k[i])*(x[i]*0.881) 
        if perm_gm >=0:
            perm.append(perm_gm)
        elif perm_gm<0:
            perm.append(0)
    return perm

def perm_g(x):
    
    f=(0.74*((x-0.04)/(1-0.16-0.04))**1.7)
    
    return f
def perm_gm(x,k):
    fm=perm_g(x)*k+(1-k)*x*0.881
    #fm=perm_g(x)*k+(1-k)*(x-0.881)
    return fm

#f=(0.95*((x-0.04)/(1-0.28-0.2-0.04))**0.6)
 
def perm_oil(x):
    f2=0.8*np.power(((1-x-0.24)/(1-0.24-0.16)),2.4)
    #f2=np.power(0.8*((1-x-0.24)/(1-0.24-0.16)),1)
    return f2









"""
SG=[0]*len(So)
for i in range(len(So)):
    SG[i]=1-So[i]

plt.plot(Sw,Krw, 'bo',label='Krw expérimentale')
plt.plot(SS,perm_w(SS),'-b',label='fonction Krw')
plt.axis([0, 1., 0, 1.])
plt.xlabel(' Sw')
plt.ylabel('Krw')
plt.legend()
plt.show()



plt.plot(So,Kro, 'ro',label='Kro expérimentale')
plt.plot(SS,perm_o(SS,CC),'-r',label='fonction Kro')
plt.xlabel('So')
plt.ylabel('Kro')
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()

plt.plot(Sg,Krg, 'go',label='Krg expérimentale')
plt.plot(SS,perm_g(SS),'-g',label='fonction Krg')
plt.xlabel('Sg')
plt.ylabel('Krg')
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()

#############################################################################
#-------------------------comparaison eclips Krg -------------------------

plt.plot(sgg,krgg, '-b',label='Krg eclips')
#plt.plot(sgg20,sgg20,'-k',label='Krg miscible')
plt.plot(sgg,perm_gm(sgg,kmmis20),'-k',label='Krg miscible')
plt.plot(sgg,perm_gm1(sgg,kmmis20),'--k',label='Krg miscible nv')
plt.plot(sgg,perm_g(sgg),'-g',label='Krg immiscible')
plt.plot(sgg,perm_gm1(sgg,kmmis),'--g',label='Krg immiscible nv')
plt.plot(sgg,perm_gm(sgg,km),'-r',label='fonction Krg')
plt.plot(sgg,perm_gm1(sgg,km),'--r',label='fonction Krg nv')
plt.plot(sgg[51],krgg[51], '*k',label='Krg à 6323 psi')
plt.plot(sgg[80],krgg[80], '*r',label='Krg à 5897 psi')
plt.xlabel('Sg')
plt.ylabel('Krg')
plt.title("424m du puits d'injection")
plt.legend()
#plt.axis([0, 1., 0, 1.])
plt.show()


plt.plot(sgg20,krgg20, '-b',label='Krg eclips')
#plt.plot(sgg20,sgg20,'-k',label='Krg miscible')
plt.plot(sgg20,perm_gm(sgg20,kmmis20),'-k',label='Krg miscible')
plt.plot(sgg20,perm_gm1(sgg20,kmmis20),'--k',label='Krg miscible nv')
plt.plot(sgg20,perm_g(sgg20),'-g',label='Krg immiscible')
plt.plot(sgg20,perm_g1(sgg20,kmmis),'--g',label='Krg immiscible nv')
plt.plot(sgg20,perm_gm(sgg20,km20),'-r',label='fonction Krg')
plt.plot(sgg20,perm_gm1(sgg20,km20),'--r',label='fonction Krg nv')
plt.plot(sgg20[51],krgg20[51], '*k',label='Krg à 6323 psi')
plt.plot(sgg20[153],krgg20[153], '*r',label='Krg à 4947 psi')
plt.xlabel('Sg')
plt.ylabel('Krg')
plt.title("565m du puits d'injection")
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()

#-------------------------comparaison eclips Kro -------------------------

plt.plot(soo,kroo, '-b',label='Kro eclips')
plt.plot(soo,perm_om(soo,km),'-y',label='fonction Kro')
plt.plot(soo,perm_om(soo,kmmis20),'-k',label='Kro miscible')
plt.plot(soo,perm_om(soo,kmmis),'-g',label='Kro immiscible')


plt.plot(soo[51],kroo[51], '*k',label='Kro à 6323 psi')
plt.plot(soo[80],kroo[80], '*r',label='Kro à 5897 psi')
plt.xlabel('So')
plt.ylabel('Kro')
plt.title("424m du puits d'injection")
plt.legend()
#plt.axis([0, 0.25, 0, 0.25])
plt.show()



plt.plot(soo20,kroo20, '-b',label='Kro eclips')
plt.plot(soo20,perm_om(soo20,km20),'-y',label='fonction Kro')
plt.plot(soo20,perm_om(soo20,kmmis20),'-k',label='Kro miscible')
plt.plot(soo20,perm_om(soo20,kmmis),'-g',label='Kro immiscible')


plt.plot(soo20[51],kroo20[51], '*k',label='Kro à 6323 psi')
plt.plot(soo20[153],kroo20[153], '*r',label='Kro à 4947 psi')
plt.xlabel('So')
plt.ylabel('Kro')
plt.title("565m du puits d'injection")
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()
"""

"""
##############################################################################
#-------------------------RELATIVE PERMIABILITY CURVE-------------------------
##############################################################################

fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.plot(Sog,Kro, 'bo',label='Kro expérimentale ')
#ax1.plot(Sog1,Kro1, 'bo')
xx=[0]*len(SS)
ax1.plot(SS,perm_oil(SS), '-b',label='fonction Kro')
ax1.set_ylabel('Kro', color=color)
ax1.set_xlabel('Sg' )
ax1.axis([0, 1., 0, 1.])
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend()
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Krg', color=color)
ax2.axis([0, 1., 0, 1.])
ax2.plot(Sg,Krg, 'ro',label='fonction Krg')
#ax2.plot(Sg1,Krg1,'ro')
ax2.plot(SS,perm_g(SS),'-r',label='Krg expérimentale ')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend()
plt.show()

"""
##############################################################################    
def FFF(x,xx,vg,vo,MOBW,k):
    A=[]
    for i in range(len(x)):
        A.append(1/(1+((perm_om(x,k)[i]*vg[i])/(perm_gm(xx,k)[i]*vo[i]))+(MOBW[i])*(vg[i]/perm_gm(xx,k)[i])))
    return A

def fg(krg,kro,vg,vo,MOBW,k):
    A=[]
    for i in range(len(krg)):
        A.append(1/(1+((kro[i]*vg[i])/(krg[i]*vo[i]))+(MOBW[i])*(vg[i]/krg[i])))
    return A

def F(x,xx,vg,vo,k):
    A=[]
    for i in range(len(x)):
        A.append(1/(1+((perm_om(x,k)[i]*vg)/(perm_gm1(xx,k)[i]*vo))))
    return A

def FC1(krg,kro,vg,vo,MOBW,k,cg,co):
    A=[]
    for i in range(len(krg)):
        A.append(fg(krg,kro,vg,vo,MOBW,k)[i]*cg[i]+(1-fg(krg,kro,vg,vo,MOBW,k)[i])*co[i])
    return A
def fC1(so,sg,vg,vo,k,cg,co):
    A=[]
    for i in range(len(so)):
        #A.append(F(so,sg,vg,vo,k)[i]*cg+(1-F(so,sg,vg,vo,k)[i])*co)
        #A.append(F(so,sg,vg,vo,k)[i]*cg+co-F(so,sg,vg,vo,k)[i]*co)
        A.append(F(so,sg,vg,vo,k)[i]*(cg-co)+co)
    return A


#############################################################################
#---------------------------Larry fractionel flow----------------------------
#############################################################################
def S(x):
    a=(x-0.04)/(1-0.04-0.16)
    return a

def M0(mo,mg):
    a=(mo*(0.74*k+(1-k)))/(mg*(0.8*k+(1-k)))
    return a
def fractionl_flow_f(x,k,mo,mg):
    a=1/(1+((1-S(x,k)-0.16)**2.4/(M0(mo,mg,k)*S(x,k)**1.7)))
    return a

"""
#############################################################################
plt.plot(sgg,fg(krgg,kroo,mug,muo,mobw,km),'-r',label='fg 3 phase (eclips perméabilité) ')
plt.plot(sgg,FFF(soo,sgg,mug,muo,mobw,km),'-b',label='fonction fg 3 phases')
#plt.plot(SS,FFF(1-SS,SS,CCmug,CCmuo,CCmobw,CC),'-k',label='fonction fg 3 phases**')
#plt.plot(SS,FFF(1-SS,SS,CCmug,CCmuo,CCmobw,CC0),'-y',label='fonction fg 3 phases00')
#plt.plot(sgg,fractionl_flow_f(sgg,km,muo,mug),'-g',label='fonction fg Larry')
plt.xlabel('Sg')
plt.ylabel('fg')
plt.title("424m du puits d'injection")
plt.legend()
#plt.axis([0.55, 0.85, 0.7, 1.])
plt.axis([0., 1, 0., 1.])
plt.show()


plt.plot(sgg,FFF(soo,sgg,mug,muo,mobw,km),'-b',label='fonction fg 3 phases')
##plt.plot(sgg,F(soo,sgg,mug,muo,km),'-g',label='fonction fg 2 phases')
##plt.plot(sgg[51],F(soo,sgg,mug,muo,km)[51],'*k',label='fg à 6323 psi')
##plt.plot(sgg[80],F(soo,sgg,mug,muo,km)[80],'*r',label='fg à 5897 psi')
plt.xlabel('Sg')
plt.ylabel('fg')
plt.title("424m du puits d'injection")
plt.legend()
plt.axis([0.55, 0.85, 0.7, 1.])
plt.show()


#############################################################################
plt.plot(sgg20,fg(krgg20,kroo20,mug20,muo20,mobw20,km20),'-r',label='fg 3 phase (eclips perméabilité) ')
plt.plot(sgg20,FFF(soo20,sgg20,mug20,muo20,mobw20,km20),'-b',label='fonction fg 3 phases')
#plt.plot(sgg20,fractionl_flow_f(sgg20,km20,muo20,mug20),'-g',label='fonction fg Larry')
#plt.plot(sgg20,fractionl_flow_fsgg20,M10),'-y',label='fonction fg Larry')
plt.xlabel('Sg')
plt.ylabel('fg')
plt.title("565m du puits d'injection")
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()

plt.plot(sgg20,FFF(soo20,sgg20,mug20,muo20,mobw20,km20),'-b',label='fonction fg 3 phases')
##plt.plot(sgg20,F(soo20,sgg20,mug20,muo20,km20),'-g',label='fonction fg 2 phases')
##plt.plot(sgg20[51],F(soo20,sgg20,mug20,muo20,km20)[51],'*k',label='fg à 6323 psi')
##plt.plot(sgg20[153],F(soo20,sgg20,mug20,muo20,km20)[153],'*r',label='fg à 4947 psi')
plt.xlabel('Sg')
plt.ylabel('fg')
plt.title("565m du puits d'injection")
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()


"""
##############################################################################
##---------------------------fg-----------------------------------------------

"""
print(CC)
print(CC05)
print(CC0)

plt.plot(SS,F(1-SS,SS,0.0396,0.1150,CC),'-g',label='fonction fg 2 phases k=1')
plt.plot(SS,F(1-SS,SS,0.0396,0.1150,CC05),'-b',label='fonction fg 2 phases k=0.5')
plt.plot(SS,F(1-SS,SS,0.0396,0.1150,CC0),'-y',label='fonction fg 2 phases k=0')
plt.xlabel('Sg')
plt.ylabel('fg')
plt.title("debit fractionnaire   k=1  k=0.5")
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()

"""
#############################################################################
#----------------------------------FC1---------------------------------------

#Sg*c1g+So*c1o=cc1........Sg*c1g+(1-Sg)*c1o=cc1.......Sg*c1g+c1o-Sg*c1o=cc1
#Sg(c1g-c1o)=cc1-c1o.........Sg=(cc1-c1o)/(c1g-c1o)
#plt.plot(cc1,FC1(krgg,kroo,mug,muo,mobw,km,c1g,c1o),'-b',label='fonction Fco2 424m')
c1gTD=[0.82]*len(SS)
c1gTD=np.array(c1gTD)
c1oTD=[0.73]*len(SS)
c1oTD=np.array(c1oTD)
#SgTD=(cc1TD-c1oTD)/(c1gTD-c1oTD)    fC1(so,sg,vg,vo,MOBW,k,cg,co)
#FFF(1-SS,SS,CCmug,CCmuo,CCmobw,CC)
def cc1TD(Sg,c1g,c1o):
    A=[]
    for i in range(len(SS)):
        A.append(Sg[i]*c1g+c1o-Sg[i]*c1o)
    return A
#plt.rcParams["figure.figsize"] = (20,3)
plt.figure(figsize=(7,7))
plt.plot(cc1TD(SS,0.82,0.73),fC1(1-SS,SS,0.0396,0.115,CC,0.82,0.73),'-b',label="ligne de racordement d'injection")
plt.plot(cc1TD(SS,0.91,0.7),fC1(1-SS,SS,0.0396,0.115,CC,0.91,0.7),'-y',label="ligne de racordement initial")
plt.plot(cc1TD(SS,0.91,0.7),fC1(1-SS,SS,0.0396,0.115,CC0,0.91,0.7),'--y',label="ligne de racordement initial")
plt.plot(cc1TD(SS,0.91,0.7),fC1(1-SS,SS,0.0396,0.115,CC05,0.91,0.7),'*y',label="ligne de racordement initial")

#plt.plot(cc120,FC1(krgg20,kroo20,mug20,muo20,mobw20,km20,c1g20,c1o20),'-g',label='fonction Fco2 565m')
plt.plot([0,2],[0,2],'-k')
plt.plot([0.68, 1.5], [0.725, 1.5],'-k',clip_on=False,linewidth=1)
v1=(1.5-0.725)/(1.5-0.68)
plt.plot([0.75, 1.5], [0.89, 1.5],'-k',clip_on=False,linewidth=1)
v2=(1.5-0.89)/(1.5-0.75)
#plt.plot(cc120[51],FC1(soo20,sgg20,mug20,muo20,km20,c1o20,c1g20)[51],'*k',label='FC1 à 6323 psi')
#plt.plot(cc120[153],FC1(soo20,sgg20,mug20,muo20,km20,c1o20,c1g20)[153],'*r',label='FC1 à 4947 psi')
plt.xlabel('CCH4')
plt.ylabel('Fc1')
plt.title("debit fractionnaire de CH4")
plt.legend()
plt.axis([0, 1., 0, 1.])
plt.show()

################################################################################
"""
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure(constrained_layout=True)

gs = GridSpec(3, 3, figure=fig)
ax1 = fig.add_subplot(gs[0, :])
# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax2 = fig.add_subplot(gs[1, :-1])
ax2 = fig.add_artist(lines.Line2D([0, 1], [0, 1]))
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])

fig.suptitle("GridSpec")
format_axes(fig)

plt.show()
"""