from memo___card_layout import (
    app, layout_card,
    lb_Question, lb_Correct, lb_Result,
    rbtn_1, rbtn_2, rbtn_3, rbtn_4,
    btn_OK, show_question, show_result)
from PyQt5.QtWidgets import QWidget
from random import shuffle # команда для перемішування списку

card_width, card_height = 600, 500
text_wrong = 'Неправильно'
text_correct = 'Правильно'

# Пишемо одне запитання і відповіді до нього
# Відповідні змінні це, по суті, майбутні поля нашої "form" (тобто анкети)
frm_question = 'Яблуко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'building'
frm_wrong3 = 'caterpillar'


# перемішуєм відповіді і запам'ятовуєм місце привильної
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)
# ми не знаємо, який це з радіобатонів, але покладем сюди правильну відповідь і запам'ятовуємо це
answer = radio_list[0]
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]


def show_data():
    ''' показує на екрані потрібну інфу '''
    # об'єднаємо в функцію схожі дії
    lb_Question.setText(frm_question)
    lb_Correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)


def check_result():
    ''' перевірка, чи правильна віпдовідь обрана '''
    correct = answer.isChecked() # У цьому радіобатоні лежить відповідь
    if correct:
        # відповідь правильна
        lb_Result.setText(text_correct) # напис "правильно" або "неправильно"
        show_result()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
        if incorrect:
            # якщо обрано не правильний радіобатон
            lb_Result.setText(text_wrong) # надпис "неправильно"
            show_result()


def click_OK(self):
    if btn_OK.text() != 'Следующий':
        check_result()


win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

win_card.setLayout(layout_card)
show_data()
show_question()
btn_OK.clicked.connect(click_OK)

win_card.show()
app.exec_()
