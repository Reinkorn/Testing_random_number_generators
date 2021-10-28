# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:55:04 2021

@author: gorod
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def cor_test(buf):
    
    bufer = buf.copy()
    key = []
    for i in range(0, len(bufer)):
        key.append(bin(i))
    key = ''.join(key)
    key = key.replace('b', '')
    #print(key)  
    sum_key = 0
    sum_key_1 = 0
    key_1= str(key[-1]+key[:(len(key)-1)])
    
    for i in range(len(key)):
        sum_key+=int(key[i])
    for i in range(len(key_1)):
        sum_key_1+=int(key_1[i])
    
    top_sum_1=0
    low_sum_1=0
    low_sum_2=0
    
    for i in range(len(key)):
        top_sum_1+=(int(key[i])*int(key_1[i]))
    for i in range(len(key)):
        low_sum_1+=(int(key[i])**2)
    for i in range(len(key)):
        low_sum_2+=(int(key_1[i])**2) 
        
    R= ((len(key)*top_sum_1) - (sum_key*sum_key_1))/pow(((len(key)*low_sum_1 - sum_key**2)*((len(key)*low_sum_2) - sum_key_1**2)), 0.5)
    R_mod =(1/(len(key)-1))+(2/(len(key)-2))*pow(((len(key))*((len(key))-3))/(len(key)+1) , 0.5)
    print(f'Коэффициент автокорреляции при k=1:{R}')
    print(f'Модульное значение (8):{R_mod}') 

def interval_dov(buf):

    bufer = buf.copy()
    #print(bufer)
    for i in range(0, len(bufer)):
        bufer[i] = (bufer[i] / 63)
    
    middle = sum(bufer)/len(bufer)
    alpha = 0.05
    M_teor = 0.5
    d_pr = M_teor - middle 
    d_cr = np.sqrt(np.var(bufer)/(len(bufer) * alpha))
    
    print(f"Практическое значение интервала {d_pr}")
    print(f"Критическое значение значение интервала {d_cr}")
    
    bufer_normal = np.random.normal(loc=0.0, scale=1.0, size=len(bufer))
    minik = min(bufer_normal)
    #print(minik)
    for i in range(0, len(bufer_normal)):
        bufer_normal[i] = (bufer_normal[i] + np.abs(minik))
                           
    maxik = max(bufer_normal)
    for i in range(0, len(bufer_normal)):
        bufer_normal[i] = (bufer_normal[i])/maxik
    
    middle_normal = sum(bufer_normal)/len(bufer_normal)
    
    x_2 = 3.84
    d_pr_normal = M_teor - middle_normal 
    d_cr_normal = np.sqrt(x_2 * np.var(bufer_normal)/(len(bufer_normal)))
    
    print(f"Практическое значение интервала для нормальных чисел {d_pr_normal}")
    print(f"Критическое значение значение интервала для нормальных чисел {d_cr_normal}")

def fric_test(buf):#Частотный тест
    bufer = buf.copy()
    
    m = max(bufer)
    for i in range(0, len(bufer)):
        bufer[i] = bufer[i]/m
    
    plt.plot(bufer)
    plt.show()
    
    drob = 0.1
    #P_teor = len(buf)/10
    x_1 = x_2 = x_3 = x_4 = x_5 = x_6 = x_7 = x_8 = x_9 = x_10 = 0
    for i in range(0, len(bufer)):
        if bufer[i] <= drob:
            x_1 += 1
        elif (bufer[i] > drob and bufer[i] <= (drob * 2)):
            x_2 += 1
        elif (bufer[i] > drob * 2 and bufer[i] <= (drob * 3)):
            x_3 += 1
        elif (bufer[i] > drob * 3 and bufer[i] <= (drob * 4)):
            x_4 += 1
        elif (bufer[i] > drob * 4 and bufer[i] <= (drob * 5)):
            x_5 += 1
        elif (bufer[i] > drob * 5 and bufer[i] <= (drob * 6)):
            x_6 += 1
        elif (bufer[i] > drob * 6 and bufer[i] <= (drob * 7)):
            x_7 += 1
        elif (bufer[i] > drob * 7 and bufer[i] <= (drob * 8)):
            x_8 += 1
        elif (bufer[i] > drob * 8 and bufer[i] <= (drob * 9)):
            x_9 += 1
        elif (bufer[i] > drob * 9 and bufer[i] <= (drob * 10)):
            x_10 += 1
         
    P_teor = len(bufer) / 10
    x_1 = x_1/len(buf)
    x_2 = x_2/len(buf)
    x_3 = x_3/len(buf)
    x_4 = x_4/len(buf)
    x_5 = x_5/len(buf)
    x_6 = x_6/len(buf)
    x_7 = x_7/len(buf)
    x_8 = x_8/len(buf)
    x_9 = x_9/len(buf)
    x_10 = x_10/len(buf)
        
    X_2 = (((x_1 - P_teor) ** 2)/P_teor) + (((x_2 - P_teor) ** 2)/P_teor) + (((x_3 - P_teor) ** 2)/P_teor) + (((x_4 - P_teor) ** 2)/P_teor) + (((x_5 - P_teor) ** 2)/P_teor) + (((x_6 - P_teor) ** 2)/P_teor) + (((x_7 - P_teor) ** 2)/P_teor) + (((x_8 - P_teor) ** 2)/P_teor) + (((x_9 - P_teor) ** 2)/P_teor)  + (((x_10 - P_teor) ** 2)/P_teor)
        
    return X_2
      
N = 500
z1 = []
for i in range(0, N):    
    z1.append(-2 * np.log(random.random()) * np.cos(2*np.pi*random.random()))
    z1.append(-2 * np.log(random.random()) * np.sin(2*np.pi*random.random()))
z1= sorted(z1)
#-------------- Средняя величина---------------------
mz = sum(z1)/(2*N)
print(mz)
#-------------- Стандартное отклонение ------------
difference = [(x - mz)**2 for x in z1]
stz = np.sqrt(sum(difference)/(len(z1) - 1))
print(stz)
#--------------- Нормализованные данные ----------
zz = (difference)/stz
mzN = sum(zz)/(2*N)
print(mzN)
difference_1 = [(x - mzN)**2 for x in zz]
stzN = np.sqrt(sum(difference_1)/(2 * (N-1)))
print(stzN)

maxik = max(z1)
z1 = [x/max(z1) for x in z1]

print(f'Значение Хи квадрат из частотного теста:{z1}')
cor_test(z1)
interval_dov(z1)