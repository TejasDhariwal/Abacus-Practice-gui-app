import customtkinter
import threading
import winsound
import pyttsx3
import time
from time import sleep
from database.labels import *
from questions import *

class AbacusPracticeApp:

    def __init__(self) -> None:
        # Setting the theme and color of the window
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        self.root = customtkinter.CTk()
        self.root.geometry("1300x700")
        self.root.title("Abacus Practice Sheet Generator")

        # variables for storing the values of settings tab
        self.settingsVariable = []
        self.worksheet_frames = []
        self.oral_worksheet_frames = []

        self.createMenu()
        self.settingsTab()
        self.worksheetTab()
        self.oralWorksheetTab()

        

        self.root.mainloop()

    def createMenu(self):
        # Create the tab to switch between different sections.
        tabs = ['Settings', 'Worksheet', 'Oral Worksheet']
        self.tab = customtkinter.CTkTabview(self.root, width=1280, height=680)
        self.tab.pack(padx=10, pady=10)

        for i in tabs:
            self.tab.add(i)

    def settingsTab(self):
        # Content of the settings tab
        a, b = 1, 0

        for i in SettingsData:
            # Frame
            settings_frame = customtkinter.CTkFrame(self.tab.tab('Settings'), width=1240, height=180)
            settings_frame.place(x=10, y=10*a + 180*b)

            # Its heading
            head = customtkinter.CTkLabel(settings_frame, text=list(i.keys())[0], font=("Dosis", 25))
            head.place(x=10, y=10)

            # Labels and Values
            c, d, e = 1, 1, 1
            for label in i.values():

                if type(label) is list:
                    for item in label:
                        l = customtkinter.CTkLabel(settings_frame, text=f"{list(item.keys())[0]}:", font=("Dosis", 20))
                        l.place(x = 10*d, y = 45*c)

                        var = customtkinter.StringVar()
                        var.set(list(item.values())[0][0])
                        self.settingsVariable.append(var)

                        v = customtkinter.CTkComboBox(settings_frame, values=list(item.values())[0], font=('Dosis', 15), variable=var)
                        v.place(x = 300*e, y = 45*c)   
                        

                        c += 1
                        if c > 3:
                            c = 1
                            d = 60
                            e = 3   

                else:  
            
                    l = customtkinter.CTkLabel(settings_frame, text=f"{list(label.keys())[0]}:", font=("Dosis", 20))
                    l.place(x = 10*d, y = 45*c)

                    var = customtkinter.StringVar()
                    var.set(list(label.values())[0][0])
                    self.settingsVariable.append(var)

                    v = customtkinter.CTkComboBox(settings_frame, values=list(label.values())[0], font=('Dosis', 15), variable=var, command=self.changeBackground)
                    v.place(x = 300*e, y = 45*c)

                    c += 1
                
            a += 1
            b += 1
     

    def worksheetTab(self):
        # Content of the worksheet tab
        
        incx, incy = 1, 1
        
        # for questions
        for heading in WorksheetData:

            self.worksheet_frame = customtkinter.CTkFrame(self.tab.tab('Worksheet'), height=300, width=400)
            self.worksheet_frame.place(x=10*incx, y=10*incy)

            if heading == "Calculation":
                self.worksheet_frame.configure(width=820)
                incx = 43
                # for stopwatch and timer

                btn1 = customtkinter.CTkButton(self.worksheet_frame, text="Stopwatch", font=("Dosis", 20), command = self.createStopwatch)
                btn1.place(x = 400, y=260)

                btn2 = customtkinter.CTkButton(self.worksheet_frame, text="Timer", font=("Dosis", 20), command = self.createTimer)
                btn2.place(x = 600, y=260)
                

            self.worksheet_frames.append(self.worksheet_frame)

            label = customtkinter.CTkLabel(self.worksheet_frame, text = heading, font=("Dosis", 23))
            label.place(x=10, y=10)

            btn1 = customtkinter.CTkButton(self.worksheet_frame, text="Display questions", font=("Dosis", 15), width=80, command=lambda x = heading: self.displayQuestions(x))
            btn1.place(x=150, y=10)

            btn2 = customtkinter.CTkButton(self.worksheet_frame, text="Display answers", font=("Dosis", 15), width=80, command=lambda x = heading: self.displayAnswers(x))
            btn2.place(x=265, y=10)

            if heading == "Division":
                additionalInfo = customtkinter.CTkLabel(self.worksheet_frame, text="NOTE: Perform floor division only.", font=("Dosis", 15))
                additionalInfo.place(x=10, y=260)

            incx += 42

            if incx == 127:
                incx = 1
                incy += 32

    def changeBackground(self, choice):
        customtkinter.set_appearance_mode(choice)

    def oralWorksheetTab(self):
        # Content of the oral worksheet tab
        incx, incy = 1, 1

        for heading in OralWorksheetData:

            self.oral_worksheet_frame = customtkinter.CTkFrame(self.tab.tab('Oral Worksheet'), height=300, width=400)
            self.oral_worksheet_frame.place(x=10*incx, y=10*incy)

            if heading == "Calculation":
                self.oral_worksheet_frame.configure(width=820)

            label = customtkinter.CTkLabel(self.oral_worksheet_frame, text = heading, font=("Dosis", 23))
            label.place(x=10, y=10)
                

            btn1 = customtkinter.CTkButton(self.oral_worksheet_frame, text="Start", font=("Dosis", 15), command = lambda x = heading: self.speakQuestions(x))
            btn1.place(x=150, y=10)
            self.oral_worksheet_frames.append(self.oral_worksheet_frame)

            incx += 42

            if incx == 127:
                incx = 1
                incy += 32
        

    def displayQuestions(self, cat):
        
        for i in WorksheetData:
            if cat == i:          
                for widget in self.worksheet_frames[WorksheetData.index(cat)].winfo_children(): 
                    if isinstance(widget, customtkinter.CTkLabel):
                        font = widget.cget("font")     
                        fontSize = font[1]

                        if fontSize == 20:
                            widget.destroy()

                if cat == "Multiplication":

                    output = MultipyQuesGen(6, int(self.settingsVariable[1].get()))

                    questions = output[0]
                    self.multiplyAnswers = output[1]

                    a = 0
                    for question in questions:
                        q = customtkinter.CTkLabel(self.worksheet_frames[0], text = question, font = ("Dosis", 20))
                        q.place(x=30, y = 60+a)
                        a += 30
                
                elif cat == "Division":
                    output = DivisionQuesGen(6, int(self.settingsVariable[2].get()))
                    questions = output[0]
                    self.divisionAnswers = output[1]
                    a = 0
                    for question in questions:
                        q = customtkinter.CTkLabel(self.worksheet_frames[1], text = question, font = ("Dosis", 20))
                        q.place(x=30, y = 60+a)
                        a += 30
                
                elif cat == "Decimal":
                    output = DecimalQuesGen(4, int(self.settingsVariable[3].get()))
                    questions = output[0]
                    self.decimalAnswers = output[1]
                    
                    b = 0
                    for question in questions:
                        a = 0
                        for value in question:
                            q = customtkinter.CTkLabel(self.worksheet_frames[2], text = value, font = ("Dosis", 20))
                            q.place(x=30+b, y = 60+a)
                            a += 30
                        b += 85
                        
                elif cat == "Calculation":
                    output = CalcQuesGen(5, int(self.settingsVariable[4].get()))
                    questions = output[0]
                    self.calcAnswers = output[1]
                    
                    b = 0
                    for question in questions:
                        a = 0
                        for value in question:
                            q = customtkinter.CTkLabel(self.worksheet_frames[3], text = value, font = ("Dosis", 20))
                            q.place(x=70+b, y = 60+a)
                            a += 30
                        b += 150

                elif cat == "Basics Practice":
                    questions = BasicsQuesGen(int(self.settingsVariable[5].get()), int(self.settingsVariable[6].get()))
                    a = 0
                    b = 0
                    self.BasicsAnswers = []
                    self.BasicsQuesions = []
                    count = 1
                    for question in questions:
                        q = customtkinter.CTkLabel(self.worksheet_frames[4], text = f"{count}. {question}", font = ("Dosis", 20))
                        q.place(x=20+b, y = 60+a)
                        count += 1

                        answer = customtkinter.CTkEntry(self.worksheet_frames[4], width=80, placeholder_text="Answer", font=("Dosis", 20))
                        answer.place(x = 100+b, y = 60+a)

                        self.BasicsAnswers.append(answer)
                        self.BasicsQuesions.append(question)

                        a += 40
                        if a == 160:
                            b += 190
                            a = 0
                    
    def displayAnswers(self, cat):
        if cat == "Multiplication":
            a = 0
            for answer in self.multiplyAnswers:
                q = customtkinter.CTkLabel(self.worksheet_frames[0], text = answer, font = ("Dosis", 20))
                q.place(x=180, y = 60+a)
                a += 30

        elif cat == "Division":
            a = 0
            for answer in self.divisionAnswers:
                q = customtkinter.CTkLabel(self.worksheet_frames[1], text = answer, font = ("Dosis", 20))
                q.place(x=180, y = 60+a)
                a += 30
        
        elif cat == "Decimal":
            a = 0
            for answer in self.decimalAnswers:
                q = customtkinter.CTkLabel(self.worksheet_frames[2], text = answer, font = ("Dosis", 20))
                q.place(x=35+a, y = 220)    
                a += 85
        
        elif cat == "Calculation":
            a = 0
            for answer in self.calcAnswers:
                q = customtkinter.CTkLabel(self.worksheet_frames[3], text = answer, font = ("Dosis", 20))
                q.place(x=75+a, y = 220)    
                a += 150
        
        elif cat == "Basics Practice":
            self.BasicsAnswers = [ans.get() for ans in self.BasicsAnswers]

            for widget in self.worksheet_frames[4].winfo_children(): 
                if isinstance(widget, customtkinter.CTkEntry):
                    widget.destroy()
                    
            answers = []
            a = 0
            b = 0
            for question in self.BasicsQuesions:
                
                if int(self.BasicsAnswers[self.BasicsQuesions.index(question)]) % int(question) == 0:
                    answer = int(self.BasicsAnswers[self.BasicsQuesions.index(question)]) // int(question)

                    if '-' in question:
                        answer += 100
                    
                    answer = str(answer) + " Steps"
                    
                else:
                    answer = "Wrong"

                answers.append(answer)
            
                ans = customtkinter.CTkLabel(self.worksheet_frames[4], text = answer, font=("Dosis", 20))
                ans.place(x = 100+b, y = 60+a)
                a+= 40
                if a == 160:
                    b += 190
                    a = 0

    def say(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()

    def speakQuestions(self, cat):
        
        for i in OralWorksheetData:
            if cat == i:          
                for widget in self.oral_worksheet_frames[OralWorksheetData.index(cat)].winfo_children(): 
                    if isinstance(widget, customtkinter.CTkLabel):
                        font = widget.cget("font")     
                        fontSize = font[1]

                        if fontSize == 20:
                            widget.destroy()

                if cat == "Multiplication":

                    output = MultipyQuesGen(6, int(self.settingsVariable[7].get()))

                    questions = output[0]
                    answers = output[1]

                    a = 0
                    count = 0
                    for question in questions:
                        q = customtkinter.CTkLabel(self.oral_worksheet_frames[0], text = question+str(answers[count]), font = ("Dosis", 20))
                        q.place(x=30, y = 60+a)
                        a += 30
                        self.say(question[2:-2].replace("X", "multiplied by"))
                        count += 1
                        sleep(3)
                    self.say("Completed")
                        
                
                elif cat == "Division":
                    output = DivisionQuesGen(6, int(self.settingsVariable[8].get()))
                    questions = output[0]
                    answers = output[1]
                    self.oraldivisionAnswers = output[1]
                    a = 0
                    count = 0
                    for question in questions:
                        q = customtkinter.CTkLabel(self.oral_worksheet_frames[1], text = question+str(answers[count]), font = ("Dosis", 20))
                        q.place(x=30, y = 60+a)
                        a += 30
                        self.say(question[2:-2].replace("/", "divided by"))
                        count += 1
                        sleep(5)
                    self.say("Completed")
                
                elif cat == "Decimal":
                    output = DecimalQuesGen(4, int(self.settingsVariable[10].get()))
                    questions = output[0]
                    answers = output[1]
                    
                    b = 0
                    count = 0
                    for question in questions:
                        a = 0
                        
                        for value in question:
                            q = customtkinter.CTkLabel(self.oral_worksheet_frames[2], text = value, font = ("Dosis", 20))
                            q.place(x=30+b, y = 60+a)
                            a += 30
                            
                            self.say(value)
                            sleep(1)
                        ans = customtkinter.CTkLabel(self.oral_worksheet_frames[2], text = str(answers[count]), font = ("Dosis", 20))
                        ans.place(x=35+b, y = 220)

                        b += 85
                        count += 1
                        if count == 4:
                            self.say("Completed")
                        else:
                            self.say("next question")
                            sleep(2)
                        
                elif cat == "Calculation":
                    output = CalcQuesGen(5, int(self.settingsVariable[9].get()))
                    questions = output[0]
                    answers = output[1]
                    
                    b = 0
                    count = 0
                    for question in questions:
                        a = 0
                        
                        for value in question:
                            q = customtkinter.CTkLabel(self.oral_worksheet_frames[3], text = value, font = ("Dosis", 20))
                            q.place(x=70+b, y = 60+a)
                            a += 30
                            self.say(value)
                            sleep(1)

                        ans = customtkinter.CTkLabel(self.oral_worksheet_frames[3], text = str(answers[count]), font = ("Dosis", 20))
                        ans.place(x=70+b, y = 220)

                        b += 150
                        count += 1
                        if count == 5:
                            self.say("Completed")
                        else:
                            self.say("next question")
                            sleep(2)

    # Stopwatch
    def createStopwatch(self):
        """ This function will create a top-level window for stopwatch. """

        # creating a top-level window for stopwatch
        
        self.stopwatch_wn = customtkinter.CTkToplevel(self.root)
        
        # top-level window settings
        self.stopwatch_wn.geometry("400x300")
        self.stopwatch_wn.minsize(400, 300)
        self.stopwatch_wn.resizable = False
        self.stopwatch_wn.title("Stopwatch") 
        # Initialize variables
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        
        # Time label
        self.time_label = customtkinter.CTkLabel(self.stopwatch_wn, text="00:00:00", font=("Dosis", 40))
        self.time_label.pack(pady=20)
        
        # Start/Stop and Reset buttons
        self.start_button = customtkinter.CTkButton(self.stopwatch_wn, text="Start", command=self.start)
        self.start_button.pack(pady=10)
        
        self.reset_button = customtkinter.CTkButton(self.stopwatch_wn, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)
        
        # Update the time display
        self.update_time_display()

    def start(self):
        if not self.running:
            # Start the stopwatch
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.start_button.configure(text="Stop", command=self.stop)
            self.update_time_display()
    
    def stop(self):
        if self.running:
            # Stop the stopwatch
            self.running = False
            self.elapsed_time = time.time() - self.start_time
            self.start_button.configure(text="Start", command=self.start)
    
    def reset(self):
        # Reset the stopwatch
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.time_label.configure(text="00:00:00")
        self.start_button.configure(text="Start", command=self.start)
    
    def update_time_display(self):
        if self.running:
            # Calculate the elapsed time
            self.elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(self.elapsed_time, 60)
            hours, minutes = divmod(minutes, 60)
            
            # Update time label
            self.time_label.configure(text=f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")
        
        # Schedule the next update
        self.stopwatch_wn.after(100, self.update_time_display)


    # Timer
    def createTimer(self):
        """ This function will create a top-level window for stopwatch. """

        # creating a top-level window for stopwatch
        
        self.timerWn = customtkinter.CTkToplevel(self.root)
        
        # top-level window settings
        self.timerWn.geometry("400x300")
        self.timerWn.minsize(400, 300)
        self.timerWn.resizable = False
        self.timerWn.title("Timer") 
        # Initialize variables
        self.TimerRunning = False
        self.remaining_time = 0  # Time in seconds

        # Input for setting timer
        self.minute_input = customtkinter.CTkEntry(self.timerWn, width=50, justify="center")
        self.minute_input.insert(0, "MM")
        self.minute_input.pack(pady=5)

        self.second_input = customtkinter.CTkEntry(self.timerWn, width=50, justify="center")
        self.second_input.insert(0, "SS")
        self.second_input.pack(pady=5)

        # Timer display label
        self.Time_label = customtkinter.CTkLabel(self.timerWn, text="00:00", font=("Dosis", 40))
        self.Time_label.pack(pady=20)
        
        # Start/Stop and Reset buttons
        self.start_timer_button = customtkinter.CTkButton(self.timerWn, text="Start", command=self.start_timer)
        self.start_timer_button.pack(pady=10)
        
        self.reset_timer_button = customtkinter.CTkButton(self.timerWn, text="Reset", command=self.reset_timer)
        self.reset_timer_button.pack(pady=10)
       

    def start_timer(self):
        if not self.TimerRunning:
            try:
                # Parse minutes and seconds from input
                minutes = int(self.minute_input.get())
                seconds = int(self.second_input.get())
                self.remaining_time = minutes * 60 + seconds
                
                # Start countdown if time is valid
                if self.remaining_time > 0:
                    self.TimerRunning = True
                    self.start_timer_button.configure(text="Pause", command=self.pause_timer)
                    self.update_timer_display()
            except ValueError:
                self.Time_label.configure(text="Invalid Input")

    def pause_timer(self):
        # Pause the timer
        self.TimerRunning = False
        self.start_timer_button.configure(text="Start", command=self.start_timer)

    def reset_timer(self):
        # Reset the timer
        self.TimerRunning = False
        self.remaining_time = 0
        self.Time_label.configure(text="00:00")
        self.start_timer_button.configure(text="Start", command=self.start_timer)
        
    def update_timer_display(self):
        if self.TimerRunning and self.remaining_time > 0:
            minutes, seconds = divmod(self.remaining_time, 60)
            self.Time_label.configure(text=f"{int(minutes):02}:{int(seconds):02}")
            self.remaining_time -= 1
            
            # Schedule the next update
            self.timerWn.after(1000, self.update_timer_display)
        elif self.remaining_time == 0:
            # Timer reached zero
            self.Time_label.configure(text="Time's Up!")
            self.TimerRunning = False
            self.start_timer_button.configure(text="Start", command=self.start_timer)
            
            # Play beep sound in a separate thread
            threading.Thread(target=self.play_beep_sound).start()

    def play_beep_sound(self):
        # Play a beep sound (frequency=1000 Hz, duration=500 ms)
        winsound.Beep(1000, 1000)


AbacusPracticeApp()
