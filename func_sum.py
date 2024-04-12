import random

''' Генерирует список с нулями длинной - 'n' '''
def zero_list(n):
    j=0
    zero_l = [j for i in range(n)]
    return zero_l

''' Генерирует список со случайным расположением порядковых чисел до - "num" 
    Косяк генерирует с ошибкой диапазон болше чем количество элементов в списке'''
def ran_num(num):
    rand = []
    con = True
    while con:
       rand_num = random.randint(0, num)
       if len(rand) != num:
           if rand_num not in rand:
               rand.append(rand_num)
       else:
           con = False
    return rand

'''r1- нижня граница размытия r2 - верхня граница   '''
def balans_sum(mas, r1, r2):
    num_r = ran_num(len(mas))
    for j in num_r:
        j = int(j) - 1
        rand = random.randint(r1, r2)
        i = mas.pop(j)
        ref = i - rand
        mas.insert(j, ref)
        if j == (len(mas)+1) or j == (len(mas)-1) or j == (len(mas)):
            k = j-1
            i = mas.pop(k)
            ref = i + rand
            mas.insert(k, ref)
        else:
            k = j+1
            i = mas.pop(k)
            ref = i + rand
            mas.insert(k, ref)
    return mas

''' Генерация массива, нужной длинны - "count" из требуемой суммы суммы - "t_sum" '''
def rasp_sum(count, t_sum):
    ishod = []
    num = t_sum / count
    for i in range(count):
        ishod.append(int(num))
    return ishod

''' Получение диапазона размытия значений '''
def zero_blur(t_sum, level): # распреление от нуля до масимального допустимого значения
    t2_sum = t_sum/2
    lev = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

''' Распределения с промежуточного значени до максимального '''
def sum_blur():
    pass

''' Из суммы с количеством элементов делает значение для дробной части'''
def drob_num(cou, t_s):
    ishod = []
    num = t_s / cou
    for i in range(cou):
        ishod.append(int(num))
    k = 0
    for i in ishod:
        k += i
    itog = int(((t_s-k)*100)/cou)

    return itog


''' Соединение целой и дробнйо части '''
def soedinenie(cel, drob1):
    mas = []
    for i in cel:
        soe = i+(drob1/100)
        mas.append(soe)
    return mas


''' Генерирует список с итоговой суммы 't', распределённый по - 'с' '''
def random_summ(c, t, r1, r2):
    ishod_mas = rasp_sum(c, t)
    finish_mas = balans_sum(ishod_mas, r1, r2)
    return finish_mas


def test_sum(s):
    print (s)
    t=0
    for i in s:
        t += i
        print(round(t, 2))
    return t


def str_mas(list):
    str_list = []
    for i in list:
        str_list.append(str(i))
    return str_list

''' Возвращает автомотичски массив с максимальным размытием значни'''
def auto_random_sum(num, summ):
    react = summ/num
    full = react/2
    ars = random_summ(num, summ, 0, int(full))
    return ars

