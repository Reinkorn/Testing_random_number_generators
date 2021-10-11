import matplotlib.pyplot as plt

def zero_full(n, ch):
    string = str(ch)
    while len(string) < n:
        string = "0" + string
    return string

period = {}
for i in range(0, 9999):
    counter = 0
    x = i
    buf = []
    while (x not in buf) and (counter != 1000):
        x_2 = x ** 2
        x_2_str = zero_full(8, x_2)
        buf.append(x)
        #print(x)
        x = (int(x_2_str[2:6]))
        counter += 1
    period[i] = counter
#print(period)
max_val = max(period.values())
final_dict = {k:v for k, v in period.items() if v == max_val}
print(final_dict)# Ответ на максимальный период

#Построим распределение длинныпериода генератора
plt.plot(period.keys(),period.values())



    
       