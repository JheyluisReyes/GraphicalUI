import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

system = customtkinter.CTk()
system.title("Graphical UI | Sign In")
system.geometry("500x350")

def login():
    username = "root"
    password = "123"

    if buser.get() == username and bpass.get() == password:
        print("")
        print("Logged in as", username + ".")

        new_window = customtkinter.CTkToplevel(system)
        new_window.title("Graphical UI | Home")
        new_window.geometry("500x350")

        customtkinter.CTkLabel(new_window, text="Welcome back, " + username, font=("Roboto", 24)).pack()

    elif buser.get() == username and bpass.get() != password:
        print("")
        print("Wrong password.")
    elif buser.get() != username and bpass.get() == password:
        print("")
        print("Wrong username.")
    else:
        print("")
        print("Wrong username and password.")

frame = customtkinter.CTkFrame(master=system)
frame.pack(pady=20, padx=60, fill="both", expand=True)

title = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
title.pack(pady=12, padx=10)

buser = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
buser.pack(pady=12, padx=10)

bpass = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
bpass.pack(pady=12, padx=10)

login_button = customtkinter.CTkButton(master=frame, text="Login", command=login)
login_button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

system.mainloop()