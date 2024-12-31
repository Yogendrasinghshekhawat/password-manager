from tkinter import *
from tkinter import messagebox

from numpy.core.defchararray import title

window=Tk()
window.title("password manager")
window.config(padx=20,pady=20)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()


    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="please make sure you have not left any space empty")

    is_ok=messagebox.askokcancel(title="website",message=f"these are the details entered: \n Email:{email} \n Password:{password}\n is it ok to save")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
img="logo.png"
canvas=Canvas(window,height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(window,text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(window,text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(window,text="Password:")
password_label.grid(row=3,column=0)


#entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)

website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"yogendra@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

#buttons

generate_password_button=Button(text="Generate password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()
