# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:36:18 2021

@author: gorod
"""
import random
import numpy as np
import matplotlib.pyplot as plt
from random import gauss
from pandas import Series
from matplotlib import *

def resultOfTurn(results, cards):
        
        #Функция resultOfTurn() — возвращает результат хода игрока. В качестве параметров функции resultOfTurn() используются results  и cards. Где results — словарь возможных результатов, а cards — список из 5-ти случайных целочисленных значений. 
        #print(cards, '\n')

        if 3 in [cards.count(c) for c in cards] and 2 in [cards.count(c) for c in cards]:
            #Если одинаковы 3 и 2.
            return results['3,2']
        elif len([c for c in [cards.count(c) for c in cards] if c == 2]) == 4:
            #Если одинаковы 2 и 2.
            return results['2,2']
        elif cards == sorted(cards):
            #Если есть 5 последовательных.
            return results['sequence']
        else:
            #Наибольший результат.
            return results[max([cards.count(c) for c in cards])]
        
def nor_plt(buf):
    series = buf.copy()
    # create white noise series
    series = Series(series)
    print(series.describe())
    series.plot()
    pyplot.show()
    
    # histogram plot
    series.hist()
    pyplot.show()

def Normolaze(buf, x):
    x = x/int(len(buf)/5) 
    return x

def poker_test(buf):#Покер тест
    bufer = buf.copy()
    min_ch = 0
    while (len(bufer) % 10) != 0:
        max_ch = len(bufer) + 1
        bufer.append(int((max_ch - min_ch) * np.random.random(1)[0] + min_ch))
    drob =  len(bufer) / 10
    
    d = 10
    
    x_1_pheory = 1/(d ** 4)
    x_2_pheory = (5 * (d - 1))/(d ** 4)
    x_3_pheory = (10 * (d - 1))/(d ** 4)
    x_4_pheory = 0.04
    x_5_pheory = (10 * (d - 1) * (d - 2))/(d ** 4)
    x_6_pheory = (15 * (d - 1) * (d - 2))/(d ** 4)
    x_7_pheory = (10 * (d - 1) * (d - 2) * (d - 3))/(d ** 4)
    x_8_pheory = ((d - 1) * (d - 2) * (d - 3) * (d - 4))/(d ** 4)
    
    for i in range(0, len(bufer)):
        if bufer[i] <= drob:
            bufer[i] = 0
        elif (bufer[i] > drob and bufer[i] <= (drob * 2)):
            bufer[i] = 1
        elif (bufer[i] > drob * 2 and bufer[i] <= (drob * 3)):
            bufer[i] = 2
        elif (bufer[i] > drob * 3 and bufer[i] <= (drob * 4)):
            bufer[i] = 3
        elif (bufer[i] > drob * 4 and bufer[i] <= (drob * 5)):
            bufer[i] = 4
        elif (bufer[i] > drob * 5 and bufer[i] <= (drob * 6)):
            bufer[i] = 5
        elif (bufer[i] > drob * 6 and bufer[i] <= (drob * 7)):
            bufer[i] = 6
        elif (bufer[i] > drob * 7 and bufer[i] <= (drob * 8)):
            bufer[i] = 7
        elif (bufer[i] > drob * 8 and bufer[i] <= (drob * 9)):
            bufer[i] = 8
        elif (bufer[i] > drob * 9 and bufer[i] <= (drob * 10)):
            bufer[i] = 9
    #если одинаковы 5, то вывести "Impossible", иначе
    #если одинаковы 4, то вывести "Four of a Kind", иначе
    #если одинаковы 3 и 2, то вывести "Full House", иначе
    #если есть 5 последовательных, то вывести "Straight", иначе
    #если одинаковы 3, то вывести "Three of a Kind", иначе
    #если одинаковы 2 и 2, то вывести "Two Pairs", иначе
    #если одинаковы 2, то вывести "One Pair", иначе
    #вывести "Nothing".
    dictionaryOfResults = {'sequence': 'Straight', 5: 'Impossible', 4: 'Four of a Kind', '3,2': 'Full House', 3: 'Three of a Kind', '2,2': 'Two Pairs', 2: 'One Pair', 1: 'Nothing'}
    x_1 = x_2 = x_3 = x_4 = x_5 = x_6 = x_7 = x_8= 0
    for i in range(0, int(len(bufer)/5)):
        cards = bufer[(5 * i):((5 * i) + 5)]
        if resultOfTurn(dictionaryOfResults, cards) == "Impossible": 
           x_1 += 1 
        elif resultOfTurn(dictionaryOfResults, cards) == "Four of a Kind":
            x_2 += 1
        elif resultOfTurn(dictionaryOfResults, cards) == "Full House": 
            x_3 += 1 
        elif resultOfTurn(dictionaryOfResults, cards) == "Straight":
            x_4 += 1
        elif resultOfTurn(dictionaryOfResults, cards) == "Three of a Kind": 
            x_5 += 1 
        elif resultOfTurn(dictionaryOfResults, cards) == "Two Pairs":
            x_6 += 1
        elif resultOfTurn(dictionaryOfResults, cards) == "One Pair":
            x_7 += 1
        elif resultOfTurn(dictionaryOfResults, cards) == "Nothing":
            x_8 += 1
    #print(x_4)
    x_1 = Normolaze(bufer, x_1)
    x_2 = Normolaze(bufer, x_2)
    x_3 = Normolaze(bufer, x_3)
    x_4 = Normolaze(bufer, x_4)
    x_5 = Normolaze(bufer, x_5)
    x_6 = Normolaze(bufer, x_6)
    x_7 = Normolaze(bufer, x_7)
    x_8 = Normolaze(bufer, x_8)
    #print(x_8)
    #print(x_8_pheory)
    X_2 = (((x_1 - x_1_pheory) ** 2)/x_1_pheory) + (((x_2 - x_2_pheory) ** 2)/x_2_pheory) + (((x_3 - x_3_pheory) ** 2)/x_3_pheory) + (((x_4 - x_4_pheory) ** 2)/x_4_pheory) +(((x_5 - x_5_pheory) ** 2)/x_5_pheory) + (((x_6 - x_6_pheory) ** 2)/x_6_pheory) + (((x_7 - x_7_pheory) ** 2)/x_7_pheory) + (((x_8 - x_8_pheory) ** 2)/x_8_pheory)
    
    return X_2

def fric_test(buf):#Частотный тест
    bufer = buf.copy()
    #print(bufer)
    maxik = max(bufer)
    
    for i in range(0, len(bufer)):
        bufer[i] = bufer[i]/maxik
    
    
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
         
    P_teor = len(bufer) / (len(bufer)*(10))
    print(P_teor)
    x_1 = x_1/len(bufer)
    x_2 = x_2/len(bufer)
    x_3 = x_3/len(bufer)
    x_4 = x_4/len(bufer)
    x_5 = x_5/len(bufer)
    x_6 = x_6/len(bufer)
    x_7 = x_7/len(bufer)
    x_8 = x_8/len(bufer)
    x_9 = x_9/len(bufer)
    x_10 = x_10/len(bufer)
        
    X_2 = (((x_1 - P_teor) ** 2)/P_teor) + (((x_2 - P_teor) ** 2)/P_teor) + (((x_3 - P_teor) ** 2)/P_teor) + (((x_4 - P_teor) ** 2)/P_teor) + (((x_5 - P_teor) ** 2)/P_teor) + (((x_6 - P_teor) ** 2)/P_teor) + (((x_7 - P_teor) ** 2)/P_teor) + (((x_8 - P_teor) ** 2)/P_teor) + (((x_9 - P_teor) ** 2)/P_teor)  + (((x_10 - P_teor) ** 2)/P_teor)
        
    return X_2

def CountFrequency(my_list):

    # Создание пустого словаря

    freq = {}

    for item in my_list:

        if (item in freq):

            freq[item] += 1

        else:

            freq[item] = 1

  

    #for key, value in freq.items():

     #   print ("% s : % d"%(key, value))
        
    return freq
  
def serial_test(buf):#Cериальный тест
    bufer = buf.copy()

    drob = max(bufer) / 10 
    #print(len(bufer))
    buf_new = []
    
    for i in range(0, len(buf)):
        if bufer[i] <= drob:
            bufer[i] = 0
        elif (bufer[i] > drob and bufer[i] <= (drob * 2)):
            bufer[i] = 1
        elif (bufer[i] > drob * 2 and bufer[i] <= (drob * 3)):
            bufer[i] = 2
        elif (bufer[i] > drob * 3 and bufer[i] <= (drob * 4)):
            bufer[i] = 3
        elif (bufer[i] > drob * 4 and bufer[i] <= (drob * 5)):
            bufer[i] = 4
        elif (bufer[i] > drob * 5 and bufer[i] <= (drob * 6)):
            bufer[i] = 5
        elif (bufer[i] > drob * 6 and bufer[i] <= (drob * 7)):
            bufer[i] = 6
        elif (bufer[i] > drob * 7 and bufer[i] <= (drob * 8)):
            bufer[i] = 7
        elif (bufer[i] > drob * 8 and bufer[i] <= (drob * 9)):
            bufer[i] = 8
        elif (bufer[i] > drob * 9 and bufer[i] <= (drob * 10)):
            bufer[i] = 9
    for i in range(0, len(bufer)):
        bufer[i] = str(bufer[i])
    for i in range(0, len(bufer), 2):
        buf_new.append(bufer[i] + bufer[i + 1])

    X_2 = 0
    freq = CountFrequency(buf_new)
    P_teorp = len(bufer)/(2 * 100)
    for key, value in freq.items():
        X_2 += (((value - P_teorp) ** 2) / P_teorp)
    
    return X_2

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
        bufer[i] = (bufer[i] / max(bufer))
    
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
    
def key_generation(len_message_binary):
    k = int(127)
    key_list_10 = []
    key_list = []
    registor = []
    #input_file_key = (open('File/key.txt','w+',encoding='utf-8'))
    #input_file_key_1 = (open('File/key_1.txt','w+',encoding='utf-8'))
    condition=["0", "1"]
    
    v = str(input(f'Загрузить начальные значения регистра из файла?(y/n):'))
    if (v == "y"):        
        input_file_registor = (open('D:/Ysceba/Карпов Иммитационное моделирование/registor.txt','r',encoding='utf-8'))
        registor_str = input_file_registor.read()
        registor = list(registor_str)
        #print(f'Начальное состояние регистра:{registor}')
        input_file_registor.close()
    else:
        input_file_registor = (open('D:/Ysceba/Карпов Иммитационное моделирование/registor.txt','w+',encoding='utf-8'))
        registor = random.choices(condition, k= 127)
        registor_str ="".join(registor)
        input_file_registor.write(registor_str)
        #print(f'Начальное состояние регистра:{registor}')
    for i in range(len_message_binary+k):#формирование ключевой последовательности
        key_list.append(registor[-1])
        x1_param = str(int(registor[-1])^int(registor[14]))#P(x)=X^33+x^13+1=0
        registor.insert(0, x1_param)
        del registor[-1]
    #del key_list[-66:-1]#Чтобы убрать значения начальные
    key_list_str="".join(key_list)
    
    #print(f"Ключ:{key_list_str}")
    key_list_str = key_list_str[k:]
    print(f"Длинна ключа:{len(key_list_str)}")
    input_file_registor.close()
    count = 0
    str_param = ''
    for i in range(len(key_list)):
        count += 1
        str_param += key_list[i]
        if count == 32:
            key_list_10.append(int(str_param, base=2))
            count = 0   
            str_param = ''
    #print(key_list_10)
    #input_file_key.close()
    return key_list_10[:10000]

buf = key_generation(64000)

print(f'Значение Хи квадрат из частотного теста:{fric_test(buf)}')
print(f'Значение Хи квадрат из покер теста:{poker_test(buf)}')
#print(f'Значение Хи квадрат из сериального теста теста:{serial_test(buf)}')
cor_test(buf)
interval_dov(buf)
#print(key)
nor_plt(buf)
#https://life-prog.ru/1_13822_chastotniy-test.html
