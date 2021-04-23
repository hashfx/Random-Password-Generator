from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import random, string

def generate():
    try:
        password.set(''.join(random.choices(data, k = int(n.get()))))
    except:
        msg.showinfo("Unidentified Input", "Enter Natural Numbers Only")



def clear_text():
    display.delete("0", END)


def copy_text():
    txt = display.get()
    print(txt)
    window.clipboard_append(txt)


window = Tk()
window.title('Random Password Generator')
window.geometry("620x250")
window.iconphoto(True, PhotoImage(file="icon.png"))
# window.config(bg="#7285A5")
window.resizable(0,0)

bg=PhotoImage(file='image.png')
label1 = Label(window, image=bg)
label1.place(x=1, y=0)


n = StringVar()
password = StringVar()


data = '!@#$%^&*()' + string.ascii_letters + string.digits

Label(window, text="Length of Password: ", borderwidth=5, relief="ridge", font="TimesNewRoman 12 bold", fg="white", bg="#ff5f1f").grid(
    column = 0, row = 0, padx=5, pady = 10
)

try:
    combo = ttk.Combobox(window, width = 5, textvariable = n, font="TimesNewRoman 14", justify='center', state="readonly")
    combo['values'] = [i for i in range(6,23)]
    # TODO: generate msg.showinfo dialog-box if combo-box-input goes above 20
    combo.grid(column = 1, row = 0, pady = 10)
    combo.current(0)
except:
    msg.showerror("Error!", "Try Again..!")
    window.destroy()


Button(window, text = "Generate Password", relief="groove", bg="coral", fg="blue", font="TimesNewRoman 12 bold", borderwidth=4, command = generate).grid(
    row = 1, column = 1, pady = 10, padx = 15
)

display = Entry(window, textvariable = password, highlightthickness=2, width=35, justify="center", bg="pink", font="TimesNewRoman 10 bold")
display.config(highlightbackground="green", highlightcolor="red")
display.grid(row = 2, column = 1, padx = 0, pady = 10) #0,3



def exitG():
    val = msg.askquestion("Confirm exit", "Do you want to exit?")
    if val == "yes":
        exit(0)



button2 = Button(window, text = "clear Password", font = ("ariel", 16), fg='white', bg='black', relief="ridge", command = clear_text)
button2.grid(row=3, column=0, pady=10) #12
button3 = Button(window, text = "Copy Password", font = ("ariel", 16), fg='royalblue', bg='lightblue', command = copy_text)
button3.grid(row=3, column=2, pady=8)
button4 = Button(window, text = "Exit", font = ("ariel", 18, "bold"), fg="white", bg="red", command = exitG, relief="raised")
button4.grid(row=3, column=1, pady=15)


window.mainloop()

