import func_sum as fs
def drob_num(cou, t_s):
    ishod = []
    sum_kop = 0
    num = t_s / cou
    for i in range(cou):
        ishod.append(int(num))
    k = 0
    for i in ishod:
        k += i
    itog = int(((t_s-k)*100)/cou)
    for i in range(cou):
        sum_kop += itog
    return sum_kop


def sliyanie(cel, drob):
    mas = []
    for i in range(len(cel)):
        soe = cel[i] + (drob[i] / 100)
        mas.append(soe)
    return mas


resalt = fs.soedinenie(64,303000)
#print(resalt)
print(fs.test_sum(resalt))

