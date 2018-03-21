"module helps to fill great amount of Google form (with only multiple choice questions) automatically (randomly or according to the user)"

import keyboard
import random
import time


def fill_questionnaire(num_of_ans_for_each_question:list,ans_num_to_fill:list=[]):

    '''function fills single Google forms with the given data about it and about how it should be fille
    num_of_ans_for_each_question -- list of integers containing the num of possible answers for each question in form
    ans_num_to_fill -- list of integers containing the numbers of answers to fill (1 means first answer)
    optional if not given form will be filled randomly if object is -1 the matching question will be filled randomly
    '''
    if len(ans_num_to_fill)==0: # fill all randomly?
        # sets ans_num_to_fill to -1 so it will be fill completely randomly
        ans_num_to_fill = [-1] * len(num_of_ans_for_each_question)
    # for all the questions in form
    for i in range(len(num_of_ans_for_each_question)):
        # tab to the current question
        keyboard.press_and_release('tab')
        # presses is the amount of presses on the 'down' button
        # this question should be filled randomly?
        if ans_num_to_fill[i] ==-1:
            # generates random answer to fill
            presses = random.randint(1, num_of_ans_for_each_question[i])
        else:
            # presses is the num of presses to be fill -1 since it start in the 2nd question
            presses = ans_num_to_fill[i]-1
            # user wants the first question to be filled?
            if presses == 0:
                # presses is the num of presses to this question since it start on the 2nd question
                presses = num_of_ans_for_each_question[i]
        # for the amount of pressing needed to be hit
        for x in range(presses):
            # press 'down'
            keyboard.press_and_release('down')

    keyboard.press_and_release('tab') # goes to submit button
    keyboard.press_and_release('enter') # hit submit


def auto_filling(refresh_time:int,times, num_of_ans_for_each_question, ans_num_to_fill:list=[]):
    '''function fill the given amount of same google form according to the given parameters
    refresh_time -- the time which takes your browser to pass from 2 different pages (not heavy pages)
    times -- the amount of forms to fill
    num_of_ans_for_each_question -- list of integers containing the num of possible answers for each question in form
    ans_num_to_fill -- list of integers containing the numbers of answers to fill (1 means first answer)
    optional if not given form will be filled randomly if object is -1 the matching question will be filled randomly
    '''
    for i in range(times):
        fill_questionnaire(num_of_ans_for_each_question, ans_num_to_fill) # fill a form
        time.sleep(refresh_time) # gives time for refresh
        keyboard.press_and_release('tab') # goes to 'send another respond button
        keyboard.press_and_release('enter') # sends another respond
        time.sleep(refresh_time) # gives time for refresh




