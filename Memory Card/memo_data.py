new_quest_templ = 'Нове питання'
new_answer_templ ='Нове відповідь'

class Form():
#Зберігає інформацію про одну анкету
def __init__(self, question=new_quest_templ, answer = new_answer_temp, answer = new_answer_temp1'', wrong_answer2='', wrong_answer3=''):
    self.question = question #Питання
    self.answer = answer #правильна відповідь
    self.wrong_answer1 = wrong_answer1
    self.wrong_answer2 = wrong_answer2
    self.wrong_answer3 = wrong_answer3
    self.is_active = True #чи продовжуєм ставити питання 
    self.attempts = 0 #
    self.correct = 0 #
def god_right(self):
    self.attempts += 1
    self.correct += 1
    def god_wrong(self):
        self.attempts += 1

class ForView():
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        #
        self.frm_model = frm_model #
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
    def change(self.frm_model) :
        #
        self.frm_model = frm_model
    def show (self):
        #
        self.question.setText(self.frm_model.question)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)
