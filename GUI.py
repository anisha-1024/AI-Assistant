from tkinter import *
import action
import speech_to_text
from PIL import Image, ImageTk

root = Tk()
root.title("AI Assistant")
root.geometry("550x685")
root.config(bg="#6F8FAF")

#ask func
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'User--->' + user_val+"\n")
    if bot_val != None:
        text.insert(END, "BOT <---"+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

def send():
    user_val = entry.get()
    bot_val = action.Action(user_val)
    text.insert(END, 'User--->' + user_val+"\n")
    if bot_val != None:
        text.insert(END, "BOT <---"+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

def del_text():
    text.delete('1.0', "end")

#FRAME
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.pack(pady=(20,10))

#TEXT LABEL
text_label = Label(frame, text="Anisha's AI Assistant", font=("Comic Sans MS", 14, "bold"), background="#356696", fg="white")
text_label.pack(pady=(0,20))

#Image 
pil_image = Image.open("Image/me.jpeg")
pil_image = pil_image.resize((250,250))
pil_image = pil_image.rotate(90,expand=True)
photo = ImageTk.PhotoImage(pil_image)

image_label = Label(frame, image=photo)
image_label.image = photo
image_label.pack(pady=10)

#adding a text widget
text = Text(root, font=('courier 10 bold'), bg="#356696",fg="white",width=45, height=5)
text.pack(pady=(30,20))

#entry widget
entry = Entry(root, justify=CENTER, font=('courier 10 bold'))
entry.pack(pady=10, ipady=8, padx=60, fill=X)

#buttons frame
btn_frame = Frame(root, bg="#6F8FAF")
btn_frame.pack(pady=20)

#Button 1
button1 = Button(btn_frame, text="ASK", bg="#FFC93C", fg="black", width=8, font=("Arial",10,"bold"), borderwidth=0, pady=8, command=ask)
button1.grid(row=0, column=0, padx=20)

#Button 2
button2 = Button(btn_frame, text="SEND", bg="#FF6B6B",fg="black", width=8, font=("Arial",10,"bold"), borderwidth=0, pady=8, command=send)
button2.grid(row=0, column=2, padx=20)

#Button 3
button3 = Button(btn_frame, text="DELETE", bg="#6BCB77", fg="black", width=8, font=("Arial",10,"bold"), borderwidth=0, pady=8, command=del_text)
button3.grid(row=0, column=1, padx=20)

root.mainloop()
