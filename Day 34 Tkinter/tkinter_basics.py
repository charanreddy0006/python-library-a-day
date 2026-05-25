import tkinter as tk

# --- create window ---
window = tk.Tk()

window.title("Python Tkinter App")

window.geometry("400x250")

# --- label ---
label = tk.Label(
    window,
    text="Welcome to Tkinter 🚀",
    font=("Arial", 18)
)

label.pack(pady=20)

# --- button function ---
def button_click():
    result_label.config(text="Button Clicked ✅")

# --- button ---
button = tk.Button(
    window,
    text="Click Me",
    command=button_click,
    bg="blue",
    fg="white",
    font=("Arial", 12)
)

button.pack(pady=10)

# --- result label ---
result_label = tk.Label(window, text="", font=("Arial", 14))

result_label.pack(pady=10)

# --- run application ---
window.mainloop()