from tkinter.messagebox import QUESTION
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import choice , shuffle
app = QApplication([]) #сторюємо віконний додаток

from window import *
class Qustion():
    Question.current=None
    def __init__(self, text, right_ans, ans2, ans3, ans4):
        self.text = text
        self.right_ans = right_ans
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4

questions = [
    Question("вісім", "eight", "eit", "твоя мама"),
    Question("bez_papu", "niger", "chomu_denusa_nema", "dayte_logiki"),
    Question("最後に死んだ", "glo glo glo", "siiiii", "infyb"),
    Question("@KINDREVILLE_LIVE", "insta", "sibscribe", "pls"),
    Question("kto ne", "podpisalsa", "bez piski", "ostalsa"),

]
radio_list = [btn1,btn2,btn3,btn4]
win = QWidget() # створємо вікно
win.resize(600, 600)
win.setWindowTitle("Memory Card")
win.setLayout(main_line)


def next_question():
    Question.current=choice(questions)
    question_lb.setText(Question.current.text)
    shuffle(radio_list)
    radio_list[0].setText(Question.current.right_ans)
    radio_list[1].setText(Question.current.ans2)
    radio_list[2].setText(Question.current.ans3)
    radio_list[3].setText(Question.current.ans4)

def asnwer_click():
    if answer_btn.text() == "Відповісти":
        group_box.hide()
        result_box.show()
        answer_btn.setText("Наступне питання")
    else:
        group_box.show()
        result_box.hide()
        answer_btn.setText("Відповісти")
        answer_btn.settext("Відповісти")

answer_btn.clicked.connect(asnwer_click)

# вкінці
next_question()
win.show() #показує вікно
app.exec_() # запускаємо додаток