import speech_recognition as sr
from gtts import gTTS
from tkinter import *
from tkinter import filedialog
import os
root=Tk()

def calc():
    filename=filedialog.askopenfilename(initialdir='D:/apana', title= "select item")
    my_lable=Label(text=filename).grid()
    file=print(filename)
    with open ("ac.txt","r") as fh:
        
        myText = fh.read().replace("\n", " ")

    # Language we want to use 
        language = 'en'

        output = gTTS(text=myText, lang=language, slow=False)

        output.save("output.mp3")
        fh.close()

    # Play the converted file 
        os.system("start output.mp3")  
        
    
       
        
    
def mic():

    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        audio = r.listen(source) 
        try:
            print("Recognizing....")
            text = r.recognize_google(audio)
            print(f"You said : {text}")
            with open("voice.txt","a") as f:
               f.write(f"        {text}::   ")
        except:
            print("sorry recognize your voice ")


    
root.geometry("550x500")
root.title("speech to text")
Label(root,text="Welcome TO speech to text convertor.....",font="30",bg="orange",fg="green",relief=SUNKEN,padx=150,pady=20).grid(row=1,column=10)
Label(root,text="Select your file to convert",font="25",padx=15,pady=15).grid(row=5,column=10)
Button(root,text="Start",command=calc,pady=6,padx=20).grid(row=10,column=10)
Label(root,text="Convert your Voic in to text...",font="30",padx=10,pady=20).grid(row=15,column=10)
Button(text="Start Microphone",command=mic,pady=6,padx=20).grid(row=20,column=10)
Label(text="Made By Ankit Singh",font="10",pady=200).grid(row=150,column=10)
root.mainloop()
input("press key to exit")
