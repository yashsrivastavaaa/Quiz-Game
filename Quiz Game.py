import tkinter.messagebox
import customtkinter
from tkinter import *
from tkinter import messagebox
import pygame

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("1000x450")
app.title("Quiz Game")
app.config(padx=20,pady=20)
app.resizable(False, False)

count = []

pygame.mixer.init()

pygame.mixer.music.load("data/audio.mp3")
pygame.mixer.music.play(loops=1000)

sound = []

def stop_music():
    if (len(sound) %2==0):
        pygame.mixer.music.set_volume(0)
        sound.append(1)
    else:
        pygame.mixer.music.set_volume(100)
        sound.append(1)  

def answer1_correct():
    tkinter.messagebox.showinfo("Correct","Great! Your Answer is Correct")
    count.append(1)
    question2()
    
def answer1_incorrect():
    tkinter.messagebox.showerror("Wrong","Oops! Your Answer is Incorrect")
    question2()

def answer2_correct():
    count.append(1)
    tkinter.messagebox.showinfo("Correct","Great! Your Answer is Correct")
    question3()

def answer2_incorrect():
    tkinter.messagebox.showerror("Wrong","Oops! Your Answer is Incorrect")
    question3()

def answer3_correct():
    count.append(1)
    tkinter.messagebox.showinfo("Correct","Great! Your Answer is Correct")
    question4()

def answer3_incorrect():
    tkinter.messagebox.showerror("Wrong","Oops! Your Answer is Incorrect")
    question4()

def answer4_correct():
    count.append(1)
    tkinter.messagebox.showinfo("Correct","Great! Your Answer is Correct")
    question5()

def answer4_incorrect():
    tkinter.messagebox.showerror("Wrong","Oops! Your Answer is Incorrect")
    question5()

def answer5_correct():
    count.append(1)
    tkinter.messagebox.showinfo("Correct","Great! Your Answer is Correct")
    question6()

def answer5_incorrect():
    tkinter.messagebox.showerror("Wrong","Oops! Your Answer is Incorrect")
    question6()

def answer6_correct():
    count.append(1)
    tkinter.messagebox.showinfo("Correct","Great! Your Answer is Correct")
    question7()

def answer6_incorrect():
    tkinter.messagebox.showerror("Wrong","Oops! Your Answer is Incorrect")
    question7()

def answer7_correct():
    count.append(1)
    tkinter.messagebox.showinfo("Correct","Great! Your Answer is Correct")
    question8()

def answer7_incorrect():
    tkinter.messagebox.showerror("Wrong","Oops! Your Answer is Incorrect")
    question8()

def answer8_correct():
    count.append(1)
    tkinter.messagebox.showinfo("Correct","Great! Your Answer is Correct")
    question9()

def answer8_incorrect():
    tkinter.messagebox.showerror("Wrong","Oops! Your Answer is Incorrect")
    question9()

def answer9_correct():
    count.append(1)
    tkinter.messagebox.showinfo("Correct","Great! Your Answer is Correct")
    question10()

def answer9_incorrect():
    tkinter.messagebox.showerror("Wrong","Oops! Your Answer is Incorrect")
    question10()

def answer10_correct():
    count.append(1)
    tkinter.messagebox.showinfo("Correct","Great! Your Answer is Correct")
    score_card()

def answer10_incorrect():
    tkinter.messagebox.showerror("Wrong","Oops! Your Answer is Incorrect")
    score_card()

def score_card():
    score = len(count)
    
    if(score>=8):
        messagebox.showinfo('Result', f'You Got {score} / 10 \n Remark : Good')

    elif(8>score>=5):
        messagebox.showinfo('Result', f'You Got {score} / 10 \n Remark : Average')

    else:
        messagebox.showinfo('Result', f'You Got {score} / 10 \n Remark : Poor')
    



def question2():
    ques1.destroy()
    option1 = customtkinter.CTkButton(master=app, command=lambda:answer2_incorrect(),text="China",font=('Century Gothic', 15))
    option1.place(relx=0.20, rely=0.65, relheight=0.07, relwidth=0.21)
    option2 = customtkinter.CTkButton(master=app, command=lambda:answer2_incorrect(), text="Japan", font=('Century Gothic', 15))
    option2.place(relx=0.60, rely=0.65, relheight=0.07, relwidth=0.21)
    option3 = customtkinter.CTkButton(master=app, command=lambda:answer2_correct(), text="India", font=('Century Gothic', 15))
    option3.place(relx=0.20, rely=0.83, relheight=0.07, relwidth=0.21)
    option4 = customtkinter.CTkButton(master=app, command=lambda:answer2_incorrect(), text="Bangladesh",  font=('Century Gothic', 15))
    option4.place(relx=0.60, rely=0.83, relheight=0.07, relwidth=0.21)
    ques2.pack()

def question3():
    ques2.destroy()
    option1 = customtkinter.CTkButton(master=app, command=lambda:answer3_correct(),text="Switzerland",font=('Century Gothic', 15))
    option1.place(relx=0.20, rely=0.65, relheight=0.07, relwidth=0.21)
    option2 = customtkinter.CTkButton(master=app, command=lambda:answer3_incorrect(), text="Italy", font=('Century Gothic', 15))
    option2.place(relx=0.60, rely=0.65, relheight=0.07, relwidth=0.21)
    option3 = customtkinter.CTkButton(master=app, command=lambda:answer3_incorrect(), text="France", font=('Century Gothic', 15))
    option3.place(relx=0.20, rely=0.83, relheight=0.07, relwidth=0.21)
    option4 = customtkinter.CTkButton(master=app, command=lambda:answer3_incorrect(), text="Belgium",  font=('Century Gothic', 15))
    option4.place(relx=0.60, rely=0.83, relheight=0.07, relwidth=0.21)
    ques3.pack()

def question4():
    ques3.destroy()
    option1 = customtkinter.CTkButton(master=app, command=lambda:answer4_correct(),text="Basketball",font=('Century Gothic', 15))
    option1.place(relx=0.20, rely=0.65, relheight=0.07, relwidth=0.21)
    option2 = customtkinter.CTkButton(master=app, command=lambda:answer4_incorrect(), text="Hockey", font=('Century Gothic', 15))
    option2.place(relx=0.60, rely=0.65, relheight=0.07, relwidth=0.21)
    option3 = customtkinter.CTkButton(master=app, command=lambda:answer4_incorrect(), text="Volleyball", font=('Century Gothic', 15))
    option3.place(relx=0.20, rely=0.83, relheight=0.07, relwidth=0.21)
    option4 = customtkinter.CTkButton(master=app, command=lambda:answer4_incorrect(), text="Football",  font=('Century Gothic', 15))
    option4.place(relx=0.60, rely=0.83, relheight=0.07, relwidth=0.21)
    ques4.pack()

def question5():
    ques4.destroy()
    option1 = customtkinter.CTkButton(master=app, command=lambda:answer5_incorrect(),text="USA",font=('Century Gothic', 15))
    option1.place(relx=0.20, rely=0.65, relheight=0.07, relwidth=0.21)
    option2 = customtkinter.CTkButton(master=app, command=lambda:answer5_incorrect(), text="Germany", font=('Century Gothic', 15))
    option2.place(relx=0.60, rely=0.65, relheight=0.07, relwidth=0.21)
    option3 = customtkinter.CTkButton(master=app, command=lambda:answer5_incorrect(), text="China", font=('Century Gothic', 15))
    option3.place(relx=0.20, rely=0.83, relheight=0.07, relwidth=0.21)
    option4 = customtkinter.CTkButton(master=app, command=lambda:answer5_correct(), text="India",  font=('Century Gothic', 15))
    option4.place(relx=0.60, rely=0.83, relheight=0.07, relwidth=0.21)
    ques5.pack()

def question6():
    ques5.destroy()
    option1 = customtkinter.CTkButton(master=app, command=lambda:answer6_incorrect(),text="Serbia",font=('Century Gothic', 15))
    option1.place(relx=0.20, rely=0.65, relheight=0.07, relwidth=0.21)
    option2 = customtkinter.CTkButton(master=app, command=lambda:answer6_incorrect(), text="Mexico", font=('Century Gothic', 15))
    option2.place(relx=0.60, rely=0.65, relheight=0.07, relwidth=0.21)
    option3 = customtkinter.CTkButton(master=app, command=lambda:answer6_incorrect(), text="India", font=('Century Gothic', 15))
    option3.place(relx=0.20, rely=0.83, relheight=0.07, relwidth=0.21)
    option4 = customtkinter.CTkButton(master=app, command=lambda:answer6_correct(), text="Brazil",  font=('Century Gothic', 15))
    option4.place(relx=0.60, rely=0.83, relheight=0.07, relwidth=0.21)
    ques6.pack()

def question7():
    ques6.destroy()
    option1 = customtkinter.CTkButton(master=app, command=lambda:answer7_incorrect(),text="Haryanvi",font=('Century Gothic', 15))
    option1.place(relx=0.20, rely=0.65, relheight=0.07, relwidth=0.21)
    option2 = customtkinter.CTkButton(master=app, command=lambda:answer7_correct(), text="Hindi", font=('Century Gothic', 15))
    option2.place(relx=0.60, rely=0.65, relheight=0.07, relwidth=0.21)
    option3 = customtkinter.CTkButton(master=app, command=lambda:answer7_incorrect(), text="Engish", font=('Century Gothic', 15))
    option3.place(relx=0.20, rely=0.83, relheight=0.07, relwidth=0.21)
    option4 = customtkinter.CTkButton(master=app, command=lambda:answer7_incorrect(), text="Mewati",  font=('Century Gothic', 15))
    option4.place(relx=0.60, rely=0.83, relheight=0.07, relwidth=0.21)
    ques7.pack()

def question8():
    ques7.destroy()
    option1 = customtkinter.CTkButton(master=app, command=lambda:answer8_incorrect(),text="Uzbekistan",font=('Century Gothic', 15))
    option1.place(relx=0.20, rely=0.65, relheight=0.07, relwidth=0.21)
    option2 = customtkinter.CTkButton(master=app, command=lambda:answer8_incorrect(), text="Russia", font=('Century Gothic', 15))
    option2.place(relx=0.60, rely=0.65, relheight=0.07, relwidth=0.21)
    option3 = customtkinter.CTkButton(master=app, command=lambda:answer8_correct(), text="Kazakhstan", font=('Century Gothic', 15))
    option3.place(relx=0.20, rely=0.83, relheight=0.07, relwidth=0.21)
    option4 = customtkinter.CTkButton(master=app, command=lambda:answer8_incorrect(), text="North Korea",  font=('Century Gothic', 15))
    option4.place(relx=0.60, rely=0.83, relheight=0.07, relwidth=0.21)
    ques8.pack()

def question9():
    ques8.destroy()
    option1 = customtkinter.CTkButton(master=app, command=lambda:answer9_incorrect(),text="Lhotse",font=('Century Gothic', 15))
    option1.place(relx=0.20, rely=0.65, relheight=0.07, relwidth=0.21)
    option2 = customtkinter.CTkButton(master=app, command=lambda:answer9_incorrect(), text="Mount Everest", font=('Century Gothic', 15))
    option2.place(relx=0.60, rely=0.65, relheight=0.07, relwidth=0.21)
    option3 = customtkinter.CTkButton(master=app, command=lambda:answer9_incorrect(), text="Annapurna", font=('Century Gothic', 15))
    option3.place(relx=0.20, rely=0.83, relheight=0.07, relwidth=0.21)
    option4 = customtkinter.CTkButton(master=app, command=lambda:answer9_correct(), text="Kamet",  font=('Century Gothic', 15))
    option4.place(relx=0.60, rely=0.83, relheight=0.07, relwidth=0.21)
    ques9.pack()

def question10():
    ques9.destroy()
    option1 = customtkinter.CTkButton(master=app, command=lambda:answer10_incorrect(),text="Glucose",font=('Century Gothic', 15))
    option1.place(relx=0.20, rely=0.65, relheight=0.07, relwidth=0.21)
    option2 = customtkinter.CTkButton(master=app, command=lambda:answer10_incorrect(), text="Chlorophyll", font=('Century Gothic', 15))
    option2.place(relx=0.60, rely=0.65, relheight=0.07, relwidth=0.21)
    option3 = customtkinter.CTkButton(master=app, command=lambda:answer10_correct(), text="Water", font=('Century Gothic', 15))
    option3.place(relx=0.20, rely=0.83, relheight=0.07, relwidth=0.21)
    option4 = customtkinter.CTkButton(master=app, command=lambda:answer10_incorrect(), text="Carbon Dioxide",  font=('Century Gothic', 15))
    option4.place(relx=0.60, rely=0.83, relheight=0.07, relwidth=0.21)
    ques10.pack()

text = customtkinter.CTkLabel(app, text="Quiz Game",font=('Century Gothic',35))
text.place(relx=0.398, rely=0.01)

frame=customtkinter.CTkFrame(master=app, width=920, height=120, corner_radius=15,border_width=5)
frame.place(relx=0.5, rely=0.30, anchor=customtkinter.CENTER)

ques1 = customtkinter.CTkLabel(master=frame,text="Which among the following is the National Sports of USA?", font=('Century Gothic', 25))
ques1.pack()

option1 = customtkinter.CTkButton(master=app,text="Bowling", command=lambda:answer1_incorrect(),font=('Century Gothic', 15))
option1.place(relx=0.20, rely=0.65, relheight=0.07, relwidth=0.21)
option2 = customtkinter.CTkButton(master=app, command=lambda:answer1_correct(), text="Baseball", font=('Century Gothic', 15))
option2.place(relx=0.60, rely=0.65, relheight=0.07, relwidth=0.21)
option3 = customtkinter.CTkButton(master=app, command=lambda:answer1_incorrect(), text="Table Tennis", font=('Century Gothic', 15))
option3.place(relx=0.20, rely=0.83, relheight=0.07, relwidth=0.21)
option4 = customtkinter.CTkButton(master=app, command=lambda:answer1_incorrect(), text="Rugby",  font=('Century Gothic', 15))
option4.place(relx=0.60, rely=0.83, relheight=0.07, relwidth=0.21)

ques2 = customtkinter.CTkLabel(master=frame,text="Which was the first country to host the Asian Games?", font=('Century Gothic', 25))
ques3 = customtkinter.CTkLabel(master=frame,text="Where is the headquarters of the International Olympic Committee located?", font=('Century Gothic', 25))
ques4 = customtkinter.CTkLabel(master=frame,text="'Free throw' is associated with:", font=('Century Gothic', 25))
ques5 = customtkinter.CTkLabel(master=frame,text="Which Country Hosted G20 Submit in 2023?", font=('Century Gothic', 25))
ques6 = customtkinter.CTkLabel(master=frame,text="Which country is called the 'Coffee Bowl of the World' ?", font=('Century Gothic', 25))
ques7 = customtkinter.CTkLabel(master=frame,text="What is the official language of Haryana?", font=('Century Gothic', 25))
ques8 = customtkinter.CTkLabel(master=frame,text="Which is the largest uranium producing country in the world ?", font=('Century Gothic', 25))
ques9 = customtkinter.CTkLabel(master=frame,text="Which among the following peaks is NOT located in Nepal Himalayas ?", font=('Century Gothic', 25))
ques10 = customtkinter.CTkLabel(master=frame,text="Oxygen liberated during photosynthesis comes from ?", font=('Century Gothic', 25))

mute = customtkinter.CTkButton(master=app, command=lambda:stop_music(), text="Mute",  font=('Century Gothic', 15))
mute.place(relx=0.95, rely=0.93, relheight=0.07, relwidth=0.06)

app.mainloop()