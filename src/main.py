import customtkinter


def login():
    print("Test")


def main():

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("500x350")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Login System")
    label.pack(pady=12, padx=10)

    entry_username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    entry_username.pack(pady=12, padx=10)

    entry_password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry_password.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.pack(pady=12, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
