questions_and_answers = {}
the_end = ''
while the_end != 'n':
    que = input('Вопрос: ')
    questions_and_answers[que] = input('Ответ: ')
    the_end = input('Продолжить?' 'y/n ')
print(questions_and_answers)
