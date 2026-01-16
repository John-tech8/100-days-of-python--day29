from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters=[random.choice(letters) for i in range(nr_letters)]
    password_symbols=[random.choice(symbols) for j in range(nr_symbols)]
    password_number=[random.choice(numbers) for k in range(nr_numbers) ]

    password_list=password_letters+password_symbols+password_number
    random.shuffle(password_list)


    password= "".join(password_list)
    password_entry.insert(0,password )
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    password=password_entry.get()
    email=email_entry.get()

    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="Oops!",message="Please fill all the fields")

    else:

        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail:{email}"
                                                           "f"f"\nPassword:{password} \n Is it ok to save?")
        if is_ok:



            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)






canvas=Canvas(width=200, height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)



website_text=Label(text="Website", font=("Arial", 15))
website_text.grid(row=1,column=1)


email_text=Label( text="Email/Username", font=("Arial", 15))
email_text.grid(row=2,column=1)

password_text=Label( text="Password", font=("Arial", 15))
password_text.grid(row=3,column=1)

website_entry=Entry()
website_entry.grid(row=1,column=2,columnspan=2)
website_entry.focus()
email_entry=Entry()
email_entry.grid(row=2,column=2,columnspan=2)
email_entry.insert(0,"rg520046@gmail.com")
password_entry=Entry()
password_entry.grid(row=3,column=2)

generate_pass_button=Button(text="Generate",command=generate_password)
generate_pass_button.grid(row=3,column=3)

add_button=Button(text="Add",command=save)
add_button.grid(row=4,column=2)



window.mainloop()
