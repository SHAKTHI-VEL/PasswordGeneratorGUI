import random, string
from tkinter import *
  
root =Tk()
root.geometry("400x400") 
 

root.title("Random Password Generator")
 
 
output_pass = StringVar()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
 
def randPassGen():
    password =[]
    password1=""
        
    
    for char in range(1,pass_len.get()):
        password+=random.choice(letters)

    for symbol in range(1,pass_len1.get()):
        password += random.choice(symbols)

    for number in range(1,pass_len2.get()):
        password += random.choice(numbers)
        
    random.shuffle(password)
    
    for char in password:
        password1+=char
    
    output_pass.set(password1)

 
pass_len = IntVar()
pass_len1 = IntVar()
pass_len2 = IntVar()
label=Label(root,text="Enter no of letters",width = 24, font='arial 16').pack()
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 24, font='arial 16').pack()
label=Label(root,text="Enter no of symbols",width = 24, font='arial 16').pack()
length2 = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len1 , width = 24, font='arial 16').pack()
label=Label(root,text="Enter no of numbers",width = 24, font='arial 16').pack()
length3 = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len2 , width = 24, font='arial 16').pack()
 
Button(root, command = randPassGen, text = "Generate Password", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
pass_label = Label(root, text = 'Random Generated Password', font = 'arial 12 bold').pack(pady="30 10")
Entry(root , textvariable = output_pass, width = 24, font='arial 16').pack()
 
root.mainloop() 
