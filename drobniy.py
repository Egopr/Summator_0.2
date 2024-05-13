import func_sum as fs
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


print(drob_num(7, 132))
print(fs.zero_blur(1, 8))








