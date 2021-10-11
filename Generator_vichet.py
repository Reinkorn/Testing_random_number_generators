# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:40:51 2021

@author: gorod
"""
import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd


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
        
def Normolaze(buf, x):
    x = x/int(len(buf)/5) 
    return x

def poker_test(buf):#Покер тест
    min_ch = 0
    while (len(buf) % 10) != 0:
        max_ch = len(buf) + 1
        buf.append(int((max_ch - min_ch) * np.random.random(1)[0] + min_ch))
    drob =  len(buf) / 10
    
    d = 10
    
    x_1_pheory = 1/(d ** 4)
    x_2_pheory = (5 * (d - 1))/(d ** 4)
    x_3_pheory = (10 * (d - 1))/(d ** 4)
    #x_4_pheory = 10/(d ** 5)
    x_5_pheory = (10 * (d - 1) * (d - 2))/(d ** 4)
    x_6_pheory = (15 * (d - 1) * (d - 2))/(d ** 4)
    x_7_pheory = (10 * (d - 1) * (d - 2) * (d - 3))/(d ** 4)
    x_8_pheory = ((d - 1) * (d - 2) * (d - 3) * (d - 4))/(d ** 4)
    
    for i in range(0, len(buf)):
        if buf[i] <= drob:
            buf[i] = 0
        elif (buf[i] > drob and buf[i] <= (drob * 2)):
            buf[i] = 1
        elif (buf[i] > drob * 2 and buf[i] <= (drob * 3)):
            buf[i] = 2
        elif (buf[i] > drob * 3 and buf[i] <= (drob * 4)):
            buf[i] = 3
        elif (buf[i] > drob * 4 and buf[i] <= (drob * 5)):
            buf[i] = 4
        elif (buf[i] > drob * 5 and buf[i] <= (drob * 6)):
            buf[i] = 5
        elif (buf[i] > drob * 6 and buf[i] <= (drob * 7)):
            buf[i] = 6
        elif (buf[i] > drob * 7 and buf[i] <= (drob * 8)):
            buf[i] = 7
        elif (buf[i] > drob * 8 and buf[i] <= (drob * 9)):
            buf[i] = 8
        elif (buf[i] > drob * 9 and buf[i] <= (drob * 10)):
            buf[i] = 9
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
    for i in range(0, int(len(buf)/5)):
        cards = buf[(5 * i):((5 * i) + 5)]
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
    x_1 = Normolaze(buf, x_1)
    x_2 = Normolaze(buf, x_2)
    x_3 = Normolaze(buf, x_3)
    x_4 = Normolaze(buf, x_4)
    x_5 = Normolaze(buf, x_5)
    x_6 = Normolaze(buf, x_6)
    x_7 = Normolaze(buf, x_7)
    x_8 = Normolaze(buf, x_8)
    print(x_8)
    print(x_8_pheory)
    X_2 = (((x_1 - x_1_pheory) ** 2)/x_1_pheory) + (((x_2 - x_2_pheory) ** 2)/x_2_pheory) + (((x_3 - x_3_pheory) ** 2)/x_3_pheory) + (((x_5 - x_5_pheory) ** 2)/x_5_pheory) + (((x_6 - x_6_pheory) ** 2)/x_6_pheory) + (((x_7 - x_7_pheory) ** 2)/x_7_pheory) + (((x_8 - x_8_pheory) ** 2)/x_8_pheory)
    
    return X_2
   
def fric_test(buf):#Частотный тест
    
    for i in range(0, len(buf)):
        buf[i] = buf[i]/m
    
    plt.plot(buf)
    plt.show()
    
    P_teor = 0.1
    drob = 0.1
    #P_teor = len(buf)/10
    x_1 = x_2 = x_3 = x_4 = x_5 = x_6 = x_7 = x_8 = x_9 = x_10 = 0
    for i in range(0, len(buf)):
        if buf[i] <= drob:
            x_1 += 1
        elif (buf[i] > drob and buf[i] <= (drob * 2)):
            x_2 += 1
        elif (buf[i] > drob * 2 and buf[i] <= (drob * 3)):
            x_3 += 1
        elif (buf[i] > drob * 3 and buf[i] <= (drob * 4)):
            x_4 += 1
        elif (buf[i] > drob * 4 and buf[i] <= (drob * 5)):
            x_5 += 1
        elif (buf[i] > drob * 5 and buf[i] <= (drob * 6)):
            x_6 += 1
        elif (buf[i] > drob * 6 and buf[i] <= (drob * 7)):
            x_7 += 1
        elif (buf[i] > drob * 7 and buf[i] <= (drob * 8)):
            x_8 += 1
        elif (buf[i] > drob * 8 and buf[i] <= (drob * 9)):
            x_9 += 1
        elif (buf[i] > drob * 9 and buf[i] <= (drob * 10)):
            x_10 += 1
            
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

def CountFrequency(my_list):

    # Создание пустого словаря

    freq = {}

    for item in my_list:

        if (item in freq):

            freq[item] += 1

        else:

            freq[item] = 1

  

    for key, value in freq.items():

        print ("% s : % d"%(key, value))
  
def serial_test(buf):#Cериальный тест
    
    drob = m / 10 
    
    buf_new = []
    
    for i in range(0, len(buf)):
        if buf[i] <= drob:
            buf[i] = 0
        elif (buf[i] > drob and buf[i] <= (drob * 2)):
            buf[i] = 1
        elif (buf[i] > drob * 2 and buf[i] <= (drob * 3)):
            buf[i] = 2
        elif (buf[i] > drob * 3 and buf[i] <= (drob * 4)):
            buf[i] = 3
        elif (buf[i] > drob * 4 and buf[i] <= (drob * 5)):
            buf[i] = 4
        elif (buf[i] > drob * 5 and buf[i] <= (drob * 6)):
            buf[i] = 5
        elif (buf[i] > drob * 6 and buf[i] <= (drob * 7)):
            buf[i] = 6
        elif (buf[i] > drob * 7 and buf[i] <= (drob * 8)):
            buf[i] = 7
        elif (buf[i] > drob * 8 and buf[i] <= (drob * 9)):
            buf[i] = 8
        elif (buf[i] > drob * 9 and buf[i] <= (drob * 10)):
            buf[i] = 9
    for i in range(0, len(buf)):
        buf[i] = str(buf[i])
    for i in range(0, len(buf), 2):
        buf_new.append(buf[i] + buf[i + 1])
    
    
    CountFrequency(buf_new)
#    return buf_new

x_0 = 19
#a = 52#a- 1 кратно p для любого простого p# равенство длинны последовательности достигается при а = 1, а = 270, a= 539  
m = (2 ** 31) - 1#269
c = int(m / 5) #53
a = (7 ** 5)#270 

counter = 0
buf = []
while (x_0 not in buf) and (counter != 10000):# ограничение по набору тестируемых данных
    buf.append(x_0)
    x =  ((a * x_0) + c) % m
    x_0 = x
    counter += 1
#print(counter_2)
#print(buf)
#print(poker_test(buf))
#print(f'Значение Хи квадрат из частотного теста:{fric_test(buf)}')
#print(f'Значение Хи квадрат из покер теста:{poker_test(buf)}')
#print(f'Значение Хи квадрат из сериального теста теста:{serial_test(buf)}')



