import customtkinter as ctk

# Theme
ctk.set_appearance_mode("dark")

# Window
app = ctk.CTk()

app.title("CustomTkinter Demo")

app.geometry("400x300")

# Label
label = ctk.CTkLabel(
    app,
    text="Welcome to CustomTkinter 🚀",
    font=("Arial", 20)
)

label.pack(pady=20)

# Button Function
def clicked():
    label.configure(
        text="Button Clicked ✅"
    )

# Button
button = ctk.CTkButton(
    app,
    text="Click Me",
    command=clicked
)

button.pack(pady=10)

app.mainloop()