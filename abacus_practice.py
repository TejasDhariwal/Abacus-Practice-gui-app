# Python program to generate a random abacus practice sheet which will be different everytime.

import customtkinter
from random import randint, choice
import pyttsx3
import time

# Setting the theme and color of the window
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()

class Func():
    # FUNCTION FOR SPEAKING THE QUESTIONS   
    def speak(text):
        engine = pyttsx3.init('sapi5')
        speaking_rate = engine.setProperty('rate', 150) # decreasing the rate of speaking

        print(text)
        engine.say(text)
        engine.runAndWait()


    # FUNCTIONS FOR APPEARANCE
    def changeAppearance(choice1):
        if choice1=="Dark":
            customtkinter.set_appearance_mode("dark")
        elif choice1=="Light":
            customtkinter.set_appearance_mode("light")
        elif choice1=="System":
            customtkinter.set_appearance_mode("system")
        else:
            pass

    
    # FUNCTIONS FOR DISPLAYING QUESTIONS   
    def multiplicationQuestions():
        """ This function will display multiplication questions. """
        for widget in frame1.winfo_children():
            widget.destroy()

        heading1 = customtkinter.CTkLabel(frame1, text="Multiplication :- ", font=("Dosis", 20))
        heading1.place(x=10, y=5)

        multiplication_question_btn = customtkinter.CTkButton(frame1, text="Display question and answers", font=('Dosis', 15), command=Func.multiplicationQuestions, width=100)
        multiplication_question_btn.place(x=140, y=8)

        # This function will always display 6 random questions of multiplication.
        a = 0
        for m_question_no in range(1, 7):
            # abstracting the no. of digits of value from settings
            z = mvalue1_digit_option.get()
            z = z.replace('-', '')
            z = z.replace('digit', '')
            z = int(z)

            # then setting the no. of digit as per the selected option
            if z==1:
                m_question_value1 = randint(1, 9)
            elif z==2:
                m_question_value1 = randint(10, 99)
            elif z==3:
                m_question_value1 = randint(100, 999)
            elif z==4:
                m_question_value1 = randint(1000, 9999)
            elif z==5:
                m_question_value1 = randint(10000, 99999)
            elif z==6:
                m_question_value1 = randint(100000, 999999)

            # abstracting the no. of digits of value from settings
            y = mvalue2_digit_option.get()
            y = y.replace('-', '')
            y = y.replace('digit', '')
            y = int(y)
            
            # then setting the no. of digit as per the selected option
            if y==1:
                m_question_value2 = randint(1, 9)
            elif y==2:
                m_question_value2 = randint(10, 99)
            elif y==3:
                m_question_value2 = randint(100, 999)
            elif y==4:
                m_question_value2 = randint(1000, 9999)

            value_of_answer = m_question_value1 * m_question_value2
            m_answer = str(value_of_answer)

            m_question = f"{str(m_question_value1)} X {str(m_question_value2)} = "
            m_complete_question = f"{m_question_no}.  {m_question}"
        
            questionLabel1 = customtkinter.CTkLabel(frame1, text=m_complete_question, font=("Dosis", 20))
            questionLabel1.place(x=30, y=60+a)

            answerLabel1 = customtkinter.CTkLabel(frame1, text=m_answer, font=("Dosis", 20))
            answerLabel1.place(x=200, y=60+a)

            a += 30

    def divisionQuestions():
        """ This function will display division questions. """
        for widget in frame2.winfo_children():
            widget.destroy()

        heading2 = customtkinter.CTkLabel(frame2, text="Division :-", font=("Dosis", 20))
        heading2.place(x=10, y=5)

        division_question_btn = customtkinter.CTkButton(frame2, text="Display question and answers", font=("Dosis", 15), command=Func.divisionQuestions, width=100)
        division_question_btn.place(x=140, y=8)

        division_description = customtkinter.CTkLabel(frame2, text="NOTE:- You have to calculate the answer and leave the decimal.\nJust write the answer and remainder.")
        division_description.place(x=10, y=245)

        # This function will always display 6 random questions of division.
        b = 0
        for d_question_no in range(1, 7):
            # abstracting the no. of digits from the settings
            digit_for_value1 = dvalue1_digit_option.get()
            digit_for_value1 = digit_for_value1.replace('-', '')
            digit_for_value1 = digit_for_value1.replace('digit', '')

            if digit_for_value1=='4':
                d_question_value1 = randint(1000, 9999)
            elif digit_for_value1=='5':
                d_question_value1 = randint(10000, 99999)
            elif digit_for_value1=='6':
                d_question_value1 = randint(100000, 999999)
            elif digit_for_value1=='7':
                d_question_value1 = randint(1000000, 9999999)
            elif digit_for_value1=='8':
                d_question_value1 = randint(10000000, 99999999)
            
            digit_for_value2 = dvalue2_digit_option.get()
            digit_for_value2 = digit_for_value2.replace('-', '')
            digit_for_value2 = digit_for_value2.replace('digit', '')

            if digit_for_value2=='1':
                d_question_value2 = randint(1, 9)
            elif digit_for_value2=='2':
                d_question_value2 = randint(10, 99)
            elif digit_for_value2=='3':
                d_question_value2 = randint(100, 999)
            elif digit_for_value2=='4':
                d_question_value2 = randint(1000, 9999)
            elif digit_for_value2=='5':
                d_question_value2 = randint(10000, 99999)

            complete_dquestion = f"{d_question_no}. {d_question_value1} / {d_question_value2} ="

            # calculating the answer
            answer = str(d_question_value1 / d_question_value2)
            i = answer.index('.')
            d_answer = answer[:i]

            # displaying the question and answers.
            questionLabel2 = customtkinter.CTkLabel(frame2, text=complete_dquestion, font=("Dosis", 20))
            questionLabel2.place(x=50, y=60+b)

            answerLabel2 = customtkinter.CTkLabel(frame2, text=d_answer, font=("Dosis", 20))
            answerLabel2.place(x=200, y=60+b)

            b += 30

    def calculationQuestions():
        """ This function will display calculation questions. """ 

        # destroying all the widgets in the frame so that the widgets do not overlap each other.
        for widget in frame3.winfo_children():
            widget.destroy()

        # creating the same widgets again so that the widgets do not disappear
        heading3 = customtkinter.CTkLabel(frame3, text="Calculation :-", font=("Dosis", 20))
        heading3.place(x=10, y=5)

        calculation_question_btn = customtkinter.CTkButton(frame3, text="Display question and answers", font=("Dosis", 15), command=Func.calculationQuestions, width=150)
        calculation_question_btn.place(x=200, y=8)

        answerLabel4 = customtkinter.CTkLabel(frame3, text="Ans :-", font=("Dosis", 20))
        answerLabel4.place(x=10, y=220)

        # generating the question
        new_value_of_x = 80
        new_value_of_x2 = 80
        c = 150
        for question in range(1, 6):
            d = 0
            answer = 0
            for value in range(1, 6):
                # fetching the information about the no. of digits in each value of the question.
                digits_for_value = cvalue_digit_option.get()
                digits_for_value = digits_for_value.replace('-', '')
                digits_for_value = digits_for_value.replace('digit', '')
                # generating the values
                signs = ['-', '  ']
                sign = choice(signs)
                cquestion_digit_value = 0

                if digits_for_value=='4':
                    cquestion_digit_value = randint(1000, 9999)
                
                elif digits_for_value=='5':
                    cquestion_digit_value = randint(10000, 99999)
                
                elif digits_for_value=='6':
                    cquestion_digit_value = randint(100000, 999999)
                
                elif digits_for_value=='7':
                    cquestion_digit_value = randint(1000000, 9999999)
                
                elif digits_for_value=='8':
                    cquestion_digit_value = randint(10000000, 99999999)

                complete_cquestion_value = f"{sign}{cquestion_digit_value}"

                # generating the answer
                if '-' in complete_cquestion_value:
                    answer -= int(cquestion_digit_value)
                else:
                    answer += int(cquestion_digit_value)

                # displaying the values on the screen
                questionLabel3 = customtkinter.CTkLabel(frame3, text=complete_cquestion_value, font=("Dosis", 20))
                questionLabel3.place(x=new_value_of_x, y=60+d)
                
                d += 30
            
            # displaying the answer
            answerLabel3 = customtkinter.CTkLabel(frame3, text=str(answer), font=("Dosis", 20))
            answerLabel3.place(x=new_value_of_x2, y=220)

            # changing the value of x of question and answer label in order to change the column
            coordinates = questionLabel3.place_info()
            value_of_x = int(coordinates['x'])
            new_value_of_x = value_of_x + c

            coordinates2 = answerLabel3.place_info()
            value_of_x2 = int(coordinates2['x'])
            new_value_of_x2 = value_of_x2 + c

    def decimalCalculationQuestions():
        """ This function will display decimal calculation questions. """

        # destroying the widgets so that they don't overlap each other.
        for widget in frame4.winfo_children():
            widget.destroy()

        # then again generating all those widgets.
        heading8 = customtkinter.CTkLabel(frame4, text="Decimal calculation", font=("Dosis", 20))
        heading8.place(x=10, y=10)

        decimal_calculation_question_btn = customtkinter.CTkButton(frame4, text="Display question and answers", font=("Dosis", 15), command=Func.decimalCalculationQuestions)
        decimal_calculation_question_btn.place(x=200, y=10)

        ans_label = customtkinter.CTkLabel(frame4, text="Ans:-", font=("Dosis", 20))
        ans_label.place(x=10, y=220)

        ans_label2 = customtkinter.CTkLabel(frame4, text="Ans:-", font=("Dosis", 20))
        ans_label2.place(x=10, y=470)

        # GENERATING THE QUESTIONS
        b = 100
        signs = ['  ', '-']
        new_value_of_x = 70
        new_value_of_x2 = 70
        for question in range(1, 9):
            a = 0
            answer = 0
            for digit in range(1, 6):
                # generating the question values
                question_digit = randint(1000, 9999)
                
                question_digit = str(question_digit)
                actual_question_digit = f"{question_digit[:-2]}.{question_digit[-2:]}"
                
                sign = choice(signs)

                complete_question_digit = f"{sign} {actual_question_digit}"

                # generating the answer
                if '-' in complete_question_digit:
                    answer -= int(question_digit)
                else:
                    answer += int(question_digit)

                # displaying the question values

                question_label = customtkinter.CTkLabel(frame4, text=complete_question_digit, font=("Dosis", 20))
                
                if question > 4:
                    if question == 5:
                        new_value_of_x = 70
                    question_label.place(x=new_value_of_x, y=300+a)

                else:
                    question_label.place(x=new_value_of_x, y=60+a)
                
                a += 30

            # displaying the answer
            answer = str(answer)
            complete_answer = f"{answer[:-2]}.{answer[-2:]}"
            answer = int(answer)
            answerLabel = customtkinter.CTkLabel(frame4, text=complete_answer, font=("Dosis", 20))

            if question > 4:
                if question == 5:
                    new_value_of_x2 = 70
                answerLabel.place(x=new_value_of_x2, y=470)

            else:
                answerLabel.place(x=new_value_of_x2, y=220)

            # changing the values of the x coordinate in order to print the next question seperately.
            coordinates = question_label.place_info()
            value_of_x = int(coordinates['x'])
            new_value_of_x = value_of_x + b

            coordinates2 = answerLabel.place_info()
            value_of_x2 = int(coordinates2['x'])
            new_value_of_x2 = value_of_x2 + b


    # FUNCTIONS FOR ORAL QUESTIONS
    def oralMultiplicationQuestions():
        """ This function will speak multiplication questions. """
        # destroying all the widgets of the frame everytime the button is being pressed so that the widgets do not overlap each other.
        for widget in frame5.winfo_children():
            widget.destroy()

        # creating the same the widgets again as they are destroyed.
        heading5 = customtkinter.CTkLabel(frame5, text="Multiplication :-", font=("Dosis", 20))
        heading5.place(x=10, y=10)

        oral_multiplication_question_btn = customtkinter.CTkButton(frame5, text="Start", width=80, font=("Dosis", 15), command=Func.oralMultiplicationQuestions)
        oral_multiplication_question_btn.place(x=270, y=10)        

        a = 0
        for i in range(1, 7):
            # fetching the information about the no. of digits in each value
            digits_for_value1 = oral_mvalue1_digit_option.get()
            digits_for_value1 = digits_for_value1.replace('-', '')
            digits_for_value1 = digits_for_value1.replace('digit', '')

            digits_for_value2 = oral_mvalue2_digit_option.get()
            digits_for_value2 = digits_for_value2.replace('-', '')
            digits_for_value2 = digits_for_value2.replace('digit', '')

            # generating the question values and answer
            oral_mquestion_value1 = 0
            oral_mquestion_value2 = 0

            if digits_for_value1=='1':
                oral_mquestion_value1 = randint(1, 9)
            
            elif digits_for_value1=='2':
                oral_mquestion_value1 = randint(10, 99)
            
            elif digits_for_value1=='3':
                oral_mquestion_value1 = randint(100, 999)
            
            elif digits_for_value1=='4':
                oral_mquestion_value1 = randint(1000, 9999)
            
            elif digits_for_value1=='5':
                oral_mquestion_value1 = randint(10000, 99999)
            
            elif digits_for_value1=='6':
                oral_mquestion_value1 = randint(100000, 999999)


            if digits_for_value2=='1':
                oral_mquestion_value2 = randint(1, 9)
            
            elif digits_for_value2=='2':
                oral_mquestion_value2 = randint(10, 99)
            
            elif digits_for_value2=='3':
                oral_mquestion_value2 = randint(100, 999)
            
            elif digits_for_value2=='4':
                oral_mquestion_value2 = randint(1000, 9999)

            oral_manswer = oral_mquestion_value1 * oral_mquestion_value2

            oral_mquestion = f"{i}.  {oral_mquestion_value1} X {oral_mquestion_value2} ="

            # displaying the question and answers on the window.
            oral_questionLabel1 = customtkinter.CTkLabel(frame5, text=oral_mquestion, font=("Dosis", 20))
            oral_questionLabel1.place(x=50, y=60+a)

            oral_answerLabel1 = customtkinter.CTkLabel(frame5, text=str(oral_manswer), font=("Dosis", 20))
            oral_answerLabel1.place(x=200, y=60+a)

            a += 30
        
            # speaking the question so as to let the user do oral practice.
            text_to_speak = f"{oral_mquestion_value1} multiplied by {oral_mquestion_value2}"
            Func.speak(text_to_speak)

            # fetching the information about the time period for break between the question.
            sec_info = oral_mtime_gap_option.get()
            sec_info = sec_info.replace(' ', '')
            sec_info = sec_info.replace('sec', '')
        
            # giving a break of some seconds so that the user can calculate the answer and note it down.
            time.sleep(int(sec_info))

    def oralDivisionQuestions():
        """ This function will speak division questions. """
        # destroying all the widgets of the frame everytime the button is being pressed so that the widgets do not overlap each other.
        for widget in frame6.winfo_children():
            widget.destroy()

        # creating the same the widgets again as they are destroyed.
        heading6 = customtkinter.CTkLabel(frame6, text="Division :-", font=("Dosis", 20))
        heading6.place(x=10, y=10)

        oral_division_question_btn = customtkinter.CTkButton(frame6, text="Start", font=("Dosis", 15), width=80, command=Func.oralDivisionQuestions)
        oral_division_question_btn.place(x=270, y=10)        

        b = 0
        for j in range(1, 7):

            # fetching the information about the no. of digits in the values of the question
            digits_for_value1 = oral_dvalue1_digit_option.get()
            digits_for_value1 = digits_for_value1.replace('-', '')
            digits_for_value1 = digits_for_value1.replace('digit', '')

            digits_for_value2 = oral_dvalue2_digit_option.get()
            digits_for_value2 = digits_for_value2.replace('-', '')
            digits_for_value2 = digits_for_value2.replace('digit', '')

            print(digits_for_value1)
            print(digits_for_value2)

            # generating the question values and answer as per the information
            oral_dquestion_value1 = 0

            if digits_for_value1=='3':
                oral_dquestion_value1 = randint(100, 999)
            
            elif digits_for_value1=='4':
                oral_dquestion_value1 = randint(1000, 9999)
            
            elif digits_for_value1=='5':
                oral_dquestion_value1 = randint(10000, 99999)
            
            elif digits_for_value1=='6':
                oral_dquestion_value1 = randint(100000, 999999)
            
            elif digits_for_value1=='7':
                oral_dquestion_value1 = randint(1000000, 9999999)
            
            elif digits_for_value1=='8':
                oral_dquestion_value1 = randint(10000000, 99999999)

            oral_dquestion_value2 = 0
            
            if digits_for_value2=='1':
                oral_dquestion_value2 = randint(1, 9)
            
            elif digits_for_value2=='2':
                oral_dquestion_value2 = randint(10, 99)
            
            elif digits_for_value2=='3':
                oral_dquestion_value2 = randint(100, 999)
            
            elif digits_for_value2=='4':
                oral_dquestion_value2 = randint(1000, 9999)
            
            elif digits_for_value2=='5':
                oral_dquestion_value2 = randint(10000, 99999)

            complete_oral_dquestion = f"{j}.  {oral_dquestion_value1} / {oral_dquestion_value2} ="

            # calculating the answer
            answer = str(oral_dquestion_value1 / oral_dquestion_value2)
            i = answer.index('.')
            oral_danswer = answer[:i]

            # displaying the question and answer
            oral_questionLabel2 = customtkinter.CTkLabel(frame6, text=complete_oral_dquestion, font=("Dosis", 20))
            oral_questionLabel2.place(x=50, y=60+b)

            oral_answerLabel2 = customtkinter.CTkLabel(frame6, text=str(oral_danswer), font=("Dosis", 20))
            oral_answerLabel2.place(x=200, y=60+b)

            b += 30

            # speaking the question
            question_to_speak = f"{oral_dquestion_value1} divided by {oral_dquestion_value2}"
            Func.speak(question_to_speak)

            # fetching the information about the break between the questions.
            waiting_time = oral_dtime_gap_option.get()
            waiting_time = waiting_time.replace(' ', '')
            waiting_time = waiting_time.replace('sec', '')

            # waiting for a few seconds so that the user can calculate the answer
            time.sleep(int(waiting_time))

    def oralCalculationQuestions():
        """ This function will speak calculation questions. """
        # destroying all the widgets of the frame everytime the button is being pressed so that the widgets do not overlap each other.
        for widget in frame7.winfo_children():
            widget.destroy()

        # creating the same the widgets again as they are destroyed.
        heading7 = customtkinter.CTkLabel(frame7, text="Calculation :-", font=("Dosis", 20))
        heading7.place(x=10, y=10)

        oral_calculation_question_btn = customtkinter.CTkButton(frame7, text="Start", font=("Dosis", 15), width=80, command=Func.oralCalculationQuestions)
        oral_calculation_question_btn.place(x=200, y=10)

        # generating the questions and answers
        c = 150
        new_value_of_x = 80
        new_value_of_x2 = 80
        for e in range(1, 6):
            d = 0
            answer = 0
            for f in range(1, 6):
                # fetching the information for the no. of digits in the value of the question
                digits_for_value = oral_cvalue_digit_option.get()
                digits_for_value = digits_for_value.replace('-', '')
                digits_for_value = digits_for_value.replace('digit', '')

                # generating the values for the question
                oral_cquestion_value = 0

                if digits_for_value=='3':
                    oral_cquestion_value = randint(100, 999)

                elif digits_for_value=='4':
                    oral_cquestion_value = randint(1000, 9999)
                
                elif digits_for_value=='5':
                    oral_cquestion_value = randint(10000, 99999)

                elif digits_for_value=='6':
                    oral_cquestion_value = randint(100000, 999999)

                elif digits_for_value=='7':
                    oral_cquestion_value = randint(1000000, 9999999)

                elif digits_for_value=='8':
                    oral_cquestion_value = randint(10000000, 99999999)
                
                signs = [' ', '-']
                sign = choice(signs)

                complete_oral_cquestion_value = f"{sign}{oral_cquestion_value}"

                # displaying the values of the question
                oral_questionLabel3 = customtkinter.CTkLabel(frame7, text=complete_oral_cquestion_value, font=("Dosis", 20))
                oral_questionLabel3.place(x=new_value_of_x, y=60+d)
                d += 30

                # calculating the answer and speaking the value
                if '-' in complete_oral_cquestion_value:
                    answer -= oral_cquestion_value
                    value_to_speak = f"minus {oral_cquestion_value}"
                    Func.speak(value_to_speak)

                else:
                    answer += oral_cquestion_value
                    value_to_speak = f"{oral_cquestion_value}"
                    Func.speak(value_to_speak)

                # fetching the information about the break between the questions
                waiting_time = oral_ctime_gap_option.get()
                waiting_time = waiting_time.replace(' ', '')
                waiting_time = waiting_time.replace('sec', '')

                # waiting for a few seconds so that the user can calculate the answer and note it down.
                if f==5:
                    Func.speak("\nNext question\n")
                    time.sleep(int(waiting_time))
                else:
                    time.sleep(1)

            # displaying the answer
            oral_answerLabel3 = customtkinter.CTkLabel(frame7, text=str(answer), font=("Dosis", 20))
            oral_answerLabel3.place(x=new_value_of_x2, y=220)

            # changing the value of x each time in order to change the column of the new question.
            coordinates = oral_questionLabel3.place_info()
            value_of_x = int(coordinates['x'])
            new_value_of_x = value_of_x + c

            coordinates2 = oral_answerLabel3.place_info()
            value_of_x2 = int(coordinates2['x'])
            new_value_of_x2 = value_of_x2 + c

    def oralDecimalCalculationQuestions():
        """ This function will speak decimal calculation questions. """

        # destroying all the widgets so that they do not overlap each other.
        for widget in frame8.winfo_children():
            widget.destroy()

        # then generating all the widgets again so that they do not disappear permanentally.
        heading8 = customtkinter.CTkLabel(frame8, text="Decimal calculation", font=("Dosis", 20))
        heading8.place(x=10, y=10)

        oral_decimal_calculation_question_btn = customtkinter.CTkButton(frame8, text="Start", font=("Dosis", 15), command=Func.oralDecimalCalculationQuestions)
        oral_decimal_calculation_question_btn.place(x=200, y=10)

        # generating the questions
        
        signs = [' ', '-']
        new_value_of_x = 70
        new_value_of_x2 = 70
        b = 100
        for question in range(9):
            a = 0
            answer = 0
            for digit in range(5):
                # generating the values
                question_digit = str(randint(100, 999))
                actual_digit = f"{question_digit[:-2]}.{question_digit[-2:]}"
                sign = choice(signs)
                complete_question_digit = f"{sign} {actual_digit}"

                # calculating the answer
                if '-' in complete_question_digit:
                    answer -= int(question_digit)
                    value_to_speak = f"minus {actual_digit}"
                else:
                    answer += int(question_digit)
                    value_to_speak = actual_digit

                # speaking the values

                if digit < 4:
                    Func.speak(value_to_speak)
                    time.sleep(1)
                else:
                    Func.speak(value_to_speak)
                    Func.speak("Next Question")
                    time.sleep(2)

                # displaying the values
                questionLabel = customtkinter.CTkLabel(frame8, text=complete_question_digit, font=("Dosis", 20))

                if question > 4:
                    if question == 5:
                        new_value_of_x = 70
                    questionLabel.place(x=new_value_of_x, y=300+a)
                else:
                    questionLabel.place(x=new_value_of_x, y=60+a)
                    
                a += 30

            # displaying the answer
            answer = str(answer)
            actual_answer = f"{answer[:-2]}.{answer[-2:]}"
            answer = int(answer)
            answerLabel = customtkinter.CTkLabel(frame8, text=actual_answer, font=("Dosis", 20))
            
            if question > 4:
                if question == 5:
                    new_value_of_x2 = 70
                answerLabel.place(x=new_value_of_x2, y=470)
            else:
                answerLabel.place(x=new_value_of_x2, y=220)

            # changing the value of x coordinate each time the question changes.

            # for the question
            coordinates = questionLabel.place_info()
            value_of_x = int(coordinates['x'])          
            new_value_of_x = value_of_x + b

            # for the answer
            coordinates2 = answerLabel.place_info()
            value_of_x2 = int(coordinates2['x'])
            new_value_of_x2 = value_of_x2 + b

                

# screen settings
root.geometry("1300x700")
root.title("Abacus Practice Sheet Generator")

# The main code for abacus practice sheet generator.

tab1 = customtkinter.CTkTabview(root, width=1280, height=680)
tab1.pack(padx=10, pady=10)

tab1.add("Settings")
tab1.add("Worksheet")
tab1.add("Oral Worksheet")
tab1.set("Worksheet")

# CONTENT OF SETTINGS TAB

# Appearance
customize_frame1 = customtkinter.CTkFrame(tab1.tab('Settings'), width=1240, height=100)
customize_frame1.place(x=10, y=10)

customize_label1 = customtkinter.CTkLabel(customize_frame1, text="Display :-", font=("Dosis", 25))
customize_label1.place(x=10, y=10)

customize_label2 = customtkinter.CTkLabel(customize_frame1, text="Appearance Mode :-", font=('Dosis', 20))
customize_label2.place(x=10, y=50)

appearance_options = customtkinter.CTkComboBox(customize_frame1, values=["Dark", "Light", "System"], font=('Dosis', 15), command=Func.changeAppearance)
appearance_options.place(x=230, y=54)
appearance_options.set("Dark")

# Settings of worksheet tab

customize_frame2 = customtkinter.CTkFrame(tab1.tab('Settings'), width=1240, height=200)
customize_frame2.place(x=10, y=120)

customize_label3 = customtkinter.CTkLabel(customize_frame2, text="Worksheet :-", font=("Dosis", 25))
customize_label3.place(x=10, y=10)

# setting the multiplication digits
customize_label4 = customtkinter.CTkLabel(customize_frame2, text="Multiplication :-", font=("Dosis", 20))
customize_label4.place(x=10, y=60)

mvalue1_digit_option = customtkinter.CTkComboBox(customize_frame2, values=['1-digit', '2-digit', '3-digit', '4-digit', '5-digit', '6-digit'], font=("Dosis", 15))
mvalue1_digit_option.place(x=230, y=64)
mvalue1_digit_option.set('4-digit')

customize_label5 = customtkinter.CTkLabel(customize_frame2, text="multiplied by", font=("Dosis", 20))
customize_label5.place(x=390, y=64)

mvalue2_digit_option = customtkinter.CTkComboBox(customize_frame2, values=['1-digit', '2-digit', '3-digit', '4-digit'], font=("Dosis", 15))
mvalue2_digit_option.place(x=510, y=64)
mvalue2_digit_option.set('2-digit')

# setting the division digits
customize_label6 = customtkinter.CTkLabel(customize_frame2, text="Division :-", font=("Dosis", 20))
customize_label6.place(x=10, y=100)

dvalue1_digit_option = customtkinter.CTkComboBox(customize_frame2, values=['4-digit', '5-digit', '6-digit', '7-digit', '8-digit'], font=("Dosis", 15))
dvalue1_digit_option.place(x=230, y=104)
dvalue1_digit_option.set('5-digit')

customize_label7 = customtkinter.CTkLabel(customize_frame2, text="divided by", font=("Dosis", 20))
customize_label7.place(x=390, y=104)

dvalue2_digit_option = customtkinter.CTkComboBox(customize_frame2, values=['1-digit', '2-digit', '3-digit', '4-digit', '5-digit'], font=("Dosis", 15))
dvalue2_digit_option.place(x=510, y=104)
dvalue2_digit_option.set('2-digit')

# setting the calculation digits
customize_label8 = customtkinter.CTkLabel(customize_frame2, text="Calculation :-", font=("Dosis", 20))
customize_label8.place(x=10, y=140)

cvalue_digit_option = customtkinter.CTkComboBox(customize_frame2, values=['4-digit', '5-digit', '6-digit', '7-digit', '8-digit'])
cvalue_digit_option.place(x=230, y=144)
cvalue_digit_option.set('5-digit')

# Settings of oral worksheet tab
customize_frame3 = customtkinter.CTkFrame(tab1.tab('Settings'), width=1240, height=300)
customize_frame3.place(x=10, y=330)

customize_label9 = customtkinter.CTkLabel(customize_frame3, text="Oral Worksheet :-", font=("Dosis", 25))
customize_label9.place(x=10, y=10)

# setting the multiplication digits
customize_label10 = customtkinter.CTkLabel(customize_frame3, text="Multiplication :-", font=("Dosis", 20))
customize_label10.place(x=10, y=60)

oral_mvalue1_digit_option = customtkinter.CTkComboBox(customize_frame3, values=['1-digit', '2-digit', '3-digit', '4-digit', '5-digit', '6-digit'], font=("Dosis", 15))
oral_mvalue1_digit_option.place(x=30, y=100)
oral_mvalue1_digit_option.set('2-digit')

customize_label11 = customtkinter.CTkLabel(customize_frame3, text="multiplied by", font=("Dosis", 20))
customize_label11.place(x=190, y=100)

oral_mvalue2_digit_option = customtkinter.CTkComboBox(customize_frame3, values=['1-digit', '2-digit', '3-digit', '4-digit'], font=("Dosis", 15))
oral_mvalue2_digit_option.place(x=310, y=100)
oral_mvalue2_digit_option.set('2-digit')

oral_mtime_gap = customtkinter.CTkLabel(customize_frame3, text="Time gap :-", font=("Dosis", 20))
oral_mtime_gap.place(x=30, y=150)

oral_mtime_gap_option = customtkinter.CTkComboBox(customize_frame3, values=['2 sec', '4 sec', '6 sec', '8 sec', '10 sec'], font=("Dosis", 15))
oral_mtime_gap_option.place(x=150, y=150)

# setting the division digits
customize_label12 = customtkinter.CTkLabel(customize_frame3, text="Division :-", font=("Dosis", 20))
customize_label12.place(x=500, y=60)

oral_dvalue1_digit_option = customtkinter.CTkComboBox(customize_frame3, values=['3-digit', '4-digit', '5-digit', '6-digit', '7-digit', '8-digit'], font=("Dosis", 15))
oral_dvalue1_digit_option.place(x=520, y=100)
oral_dvalue1_digit_option.set('5-digit')

customize_label13 = customtkinter.CTkLabel(customize_frame3, text="divided by", font=("Dosis", 20))
customize_label13.place(x=680, y=100)

oral_dvalue2_digit_option = customtkinter.CTkComboBox(customize_frame3, values=['1-digit', '2-digit', '3-digit', '4-digit', '5-digit'], font=("Dosis", 15))
oral_dvalue2_digit_option.place(x=780, y=100)
oral_dvalue2_digit_option.set('2-digit')

oral_dtime_gap = customtkinter.CTkLabel(customize_frame3, text="Time gap :-", font=("Dosis", 20))
oral_dtime_gap.place(x=520, y=150)

oral_dtime_gap_option = customtkinter.CTkComboBox(customize_frame3, values=['5 sec', '10 sec', '15 sec', '20 sec'], font=("Dosis", 15))
oral_dtime_gap_option.place(x=670, y=150)
oral_dtime_gap_option.set('10 sec')

# setting the calculation digits
customize_label14 = customtkinter.CTkLabel(customize_frame3, text="Calculation :-", font=("Dosis", 20))
customize_label14.place(x=10, y=200)

oral_cvalue_digit_option = customtkinter.CTkComboBox(customize_frame3, values=['3-digit', '4-digit', '5-digit', '6-digit', '7-digit', '8-digit'])
oral_cvalue_digit_option.place(x=30, y=240)
oral_cvalue_digit_option.set('3-digit')

oral_ctime_gap = customtkinter.CTkLabel(customize_frame3, text="Time gap :-", font=("Dosis", 20))
oral_ctime_gap.place(x=430, y=240)

oral_ctime_gap_option = customtkinter.CTkComboBox(customize_frame3, values=['2 sec', '3 sec', '4 sec', '5 sec'])
oral_ctime_gap_option.place(x=560, y=240)
oral_ctime_gap_option.set('2 sec')


# CONTENT OF WORKSHEET TAB
# Heading
heading = customtkinter.CTkLabel(tab1.tab("Worksheet"), text="Abacus Practice Sheet", font=("Dosis", 25))
heading.place(x=520, y=10)

# Frame 1 for multiplication questions
frame1 = customtkinter.CTkFrame(tab1.tab("Worksheet"), width=380, height=280)
frame1.place(x=30, y=50)

heading1 = customtkinter.CTkLabel(frame1, text="Multiplication :- ", font=("Dosis", 20))
heading1.place(x=10, y=5)

multiplication_question_btn = customtkinter.CTkButton(frame1, text="Display question and answers", font=('Dosis', 15), command=Func.multiplicationQuestions, width=100)
multiplication_question_btn.place(x=140, y=8)

# Frame 2 for division questions.
frame2 = customtkinter.CTkFrame(tab1.tab("Worksheet"), width=380, height=280)
frame2.place(x=420, y=50)

heading2 = customtkinter.CTkLabel(frame2, text="Division :-", font=("Dosis", 20))
heading2.place(x=10, y=5)

division_question_btn = customtkinter.CTkButton(frame2, text="Display question and answers", font=("Dosis", 15), command=Func.divisionQuestions, width=100)
division_question_btn.place(x=140, y=8)

division_description = customtkinter.CTkLabel(frame2, text="NOTE:- You have to calculate the answer and leave the decimal.\nJust write the answer and remainder.")
division_description.place(x=10, y=245)

# Frame 3 for calculation questions.
frame3 = customtkinter.CTkFrame(tab1.tab("Worksheet"), width=770, height=260)
frame3.place(x=30, y=340)

heading3 = customtkinter.CTkLabel(frame3, text="Calculation :-", font=("Dosis", 20))
heading3.place(x=10, y=5)

calculation_question_btn = customtkinter.CTkButton(frame3, text="Display question and answers", font=("Dosis", 15), command=Func.calculationQuestions, width=150)
calculation_question_btn.place(x=200, y=8)

# Frame 4 calculation questions
frame4 = customtkinter.CTkFrame(tab1.tab('Worksheet'), width=450, height=550)
frame4.place(x=810, y=50)

heading8 = customtkinter.CTkLabel(frame4, text="Decimal calculation", font=("Dosis", 20))
heading8.place(x=10, y=10)

decimal_calculation_question_btn = customtkinter.CTkButton(frame4, text="Display question and answers", font=("Dosis", 15), command=Func.decimalCalculationQuestions)
decimal_calculation_question_btn.place(x=200, y=10)


# CONTENT OF ORAL WORKSHEET TAB
heading4 = customtkinter.CTkLabel(tab1.tab("Oral Worksheet"), text="Oral Practice Worksheet", font=("Dosis", 25))
heading4.place(x=520, y=10)

# oral multiplication questions
frame5 = customtkinter.CTkFrame(tab1.tab("Oral Worksheet"), width=380, height=280)
frame5.place(x=30, y=50)

heading5 = customtkinter.CTkLabel(frame5, text="Multiplication :-", font=("Dosis", 20))
heading5.place(x=10, y=10)

oral_multiplication_question_btn = customtkinter.CTkButton(frame5, text="Start", width=80, font=("Dosis", 15), command=Func.oralMultiplicationQuestions)
oral_multiplication_question_btn.place(x=270, y=10)

# oral division questions
frame6 = customtkinter.CTkFrame(tab1.tab("Oral Worksheet"), width=380, height=280)
frame6.place(x=420, y=50)

heading6 = customtkinter.CTkLabel(frame6, text="Division :-", font=("Dosis", 20))
heading6.place(x=10, y=10)

oral_division_question_btn = customtkinter.CTkButton(frame6, text="Start", font=("Dosis", 15), width=80, command=Func.oralDivisionQuestions)
oral_division_question_btn.place(x=270, y=10)

# oral calculation questions
frame7 = customtkinter.CTkFrame(tab1.tab("Oral Worksheet"), width=770, height=260)
frame7.place(x=30, y=340)

heading7 = customtkinter.CTkLabel(frame7, text="Calculation :-", font=("Dosis", 20))
heading7.place(x=10, y=10)

oral_calculation_question_btn = customtkinter.CTkButton(frame7, text="Start", font=("Dosis", 15), width=80, command=Func.oralCalculationQuestions)
oral_calculation_question_btn.place(x=200, y=10)

# Frame 8 for oral decimal calculation questions
frame8 = customtkinter.CTkFrame(tab1.tab('Oral Worksheet'), width=450, height=550)
frame8.place(x=810, y=50)

heading8 = customtkinter.CTkLabel(frame8, text="Decimal calculation", font=("Dosis", 20))
heading8.place(x=10, y=10)

oral_decimal_calculation_question_btn = customtkinter.CTkButton(frame8, text="Start", font=("Dosis", 15), command=Func.oralDecimalCalculationQuestions)
oral_decimal_calculation_question_btn.place(x=200, y=10)


root.mainloop()

