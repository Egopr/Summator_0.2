from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QIODevice
import func_sum as fs

app = QtWidgets.QApplication([])
ui = uic.loadUi('summator_0.1.ui')


ui.setWindowTitle('Summator')


def get_num():
    ui.num.selectAll()
    num = ui.num.selectedText()
    num = int(num)
    return num


def get_sum():
    ui.sum.selectAll()
    sum = ui.sum.selectedText()
    sum = int(sum)
    return sum

def get_befor():
    ui.befor.selectAll()
    befor = ui.befor.selectedText()
    befor = int(befor)
    return befor


def get_after():
    ui.after.selectAll()
    after = ui.after.selectedText()
    after = int(after)
    return after


def write_list():
    ui.listWidget.clear()
    cur_row = ui.listWidget.currentRow()
    mas = fs.random_summ(get_num(), get_sum(), get_befor(), get_after())
    str_mas = fs.str_mas(mas)
    for i in str_mas:
        ui.listWidget.insertItem(cur_row+1, i)


ui.pushButton.clicked.connect(write_list)
#ui.pushButton.clicked.connect(get_num)





ui.show()
app.exec()