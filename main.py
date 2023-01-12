from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import spacy
nlp = spacy.load("en_core_web_sm")

engine = pp.init()
voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voices', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")
convo = [

    'Hello',
    'hi there',
    'what is your name ?',
    'My name is Bot,i am created by Pankaj',
    'how are you',
    'I am doing great these days',
    'In which city do live?',
    'I live in Jalandhar',
    'What is your langauage',
    'I talk English,if you Traine me i can talk any language'
    'what is date today',
    '10 jan 2023',
    'what you can do for me',
    'i can help you to find your answer',
    'can you bring water',
    'no,i can only direct you to the watercooler'
]

trainer = ListTrainer(bot)
trainer.train(convo)
#answer = bot.get_response("what is your name ?")
#print(answer)

#print("Talk to bot")
#while True:
    #query = input()
    #if query == 'exit':
        #break
    #answer = bot.get_response(query)
    #print("bot :", answer)

main = Tk()
main.geometry("600x600")
main.title("My chat bot")
img = PhotoImage(file="icons8-chatbot-94.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)

#take query as voice form

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, END)
            Ask_Your_Query()
        except Exception as e:
            print(e)
            print("not recognized")


def Ask_Your_Query(*args):
    query = textF.get()
    Ask_Your_Query = bot.get_response(query)
    msg.insert(END, "you : " + query)
    msg.insert(END, "bot : " + str(Ask_Your_Query))
    speak(Ask_Your_Query)
    textF.delete(0, END)
    msg.yview(END)



frame = Frame(main)
sc = Scrollbar(frame)
msg = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
#creating text field
textF = Entry(main, font=("verdana", 15))
textF.pack(fill=X, pady=10)
btn = Button(main, text="Ask Your Query", font=("verdana", 15), command=Ask_Your_Query)
btn.pack()

#creating function

def enter_function(event):
    btn.invoke()

#going to bind mian window with enter key

main.bind('<Return>', enter_function)

def repeatL():
    while True:
        takeQuery()
t = threading.Thread(target=repeatL)
t.start()

main.mainloop()


