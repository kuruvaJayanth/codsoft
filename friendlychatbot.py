from tkinter import *

root = Tk()
root.title(" Friendly Chatbot ")

def input():
    input = "You -> "+e.get()
    txt.insert(END, "\n"+input)
    user = e.get().lower()
    if(user == "hi"):
        txt.insert(END, "\n" + "Bot -> Hello")
    elif(user == "hello" or user == "Hello" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hi")
    elif(e.get() == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good" or user == "good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")
    elif(user == "tell me some things to do in free time" or user == "things to do in free time"):
        txt.insert(END, "\n" + "Bot -> You could try painting,drawing,dancing,writing in your free time!")
    elif(user == "thanks" or user == "ok"):
        txt.insert(END, "\n" + "Bot -> Welcome!Do you have any more questions?")
    elif(user == "No" or user == "no"):
        txt.insert(END, "\n" + "Bot -> Alright!")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't get you")
    e.delete(0, END)

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
input = Button(root, text="input", command=input).grid(row=2, column=2)
root.mainloop()
