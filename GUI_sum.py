from PyQt5 import QtWidgets, uic
import func_sum as fs

app = QtWidgets.QApplication([])
#app.setStyle('Fusion') # 'Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion'
ui = uic.loadUi('summator_0.1.ui')
ui.setWindowTitle('Summator')


def get_num():
    num = ui.num.displayText()
    if num != "":
        num = int(num)
        ui.num.end(0)
    else:
        num = -1
    return num


def get_sum():
    sum = ui.sum.displayText()
    if sum != "":
        sum = int(sum)
        ui.sum.end(0)
    else:
        sum = 0
    return sum


def get_before():
    before = ui.before.displayText()
    before = int(before)
    ui.before.end(0)
    return before


def get_after():
    after = ui.after.displayText()
    after = int(after)
    ui.after.end(0)
    return after


def check_sum():
    summ = 0
    if (get_num() != "") and (get_sum() != ""):
        summ = round(get_sum()/get_num(), 2)
    return summ #частное для контроля ручного режима размытия случайного порядка

def check_test():
    soe = fs.soedinenie(get_num(), get_sum())
    test = round(fs.test_sum(soe), 2)
    return test


def auto_rez():
    mas = fs.auto_random_sum(get_num(), get_sum())
    return mas


def hand_rez():
    mas = fs.random_summ(get_num(), get_sum(), get_before(), get_after())
    return mas


'''Устарела функция'''
def write_list():
    ui.listWidget.clear()
    cur_row = ui.listWidget.currentRow()
    '''
        if
            mass = auto_rez()
            mass = hand_rez()
    '''
    mass = fs.auto_random_sum(get_num(), get_sum())
    str_mas = fs.str_mas(mass)
    for i in str_mas:
        ui.listWidget.insertItem(cur_row + 1, i)

    ui.info.setText('Completed')


def text_edit():
    ui.textEdit.clear()
    mass = fs.soedinenie(get_num(), get_sum())
    str_mas = fs.str_mas(mass)
    for i in str_mas:
        ui.textEdit.append(i)
    ui.info.setText('Completed')



def clear_box():
    ui.textEdit.clear()
    ui.info.setText('Clear')


def main():
    if check_sum() > 0:
        ui.labe_control.setText(str(check_sum()))
        ui.sum_leb.setText(str(check_test()))
        text_edit()
    else:
        ui.labe_control.setText("Error write")



ui.pushButton.clicked.connect(main)
ui.clear.clicked.connect(clear_box)

#ui.num.createStandardContextMenu()
#ui.pushButton.clicked.connect(ccc)


ui.show()
app.exec()