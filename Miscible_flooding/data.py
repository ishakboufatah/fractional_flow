# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 17:54:52 2021

@author: ishak
"""

import numpy as np
import openpyxl  as xl
ws=xl.load_workbook('OIL.xlsx',data_only=True)
SCAL= ws['SCAL'] 

Kr=xl.load_workbook('Relative Permeability Results Dead-Oil with Injection Water.xlsx',data_only=True)
SCAL2=Kr['Gas-Oil OMJ-323 Sample 4']
def get_value(ws,a):
    result=[]
    for cell in ws[a:]:
        result.append(cell.value)
    return result

########################################################################
#---------------------relative permeability data from ECLIPSE------------------------
 
Sw=get_value(SCAL['B'],1)     ;Sg=get_value(SCAL['H'],1) 
Krw=get_value(SCAL['C'],1)    ;Krg=get_value(SCAL['I'],1)
Krow=get_value(SCAL['D'],1)   ;Krog=get_value(SCAL['J'],1)

########################################################################



########################################################################
#---------------------relative permeability data from EXPIRIMRNT------------------------
 
SG=get_value(SCAL2['D'],10) 
KrG=get_value(SCAL2['F'],10)
KrO=get_value(SCAL2['E'],10)

print(SG)
########################################################################
#print(Sw)
