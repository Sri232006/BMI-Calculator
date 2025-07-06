import tkinter as tk
from tkinter import messagebox
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        
        if weight <= 0 or height_cm <= 0:
            raise ValueError
        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)
        if bmi < 18.5: 
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        result_label.config(text=f"BMI: {bmi}\nCategory: {category}", fg="#ffffff")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers greater than 0.")
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x400")
root.configure(bg="#1e1e2e")  
heading_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 11, "bold")
tk.Label(root, text="BMI Calculator", font=heading_font, bg="#1e1e2e", fg="#cba6f7").pack(pady=20)
tk.Label(root, text="Weight (kg):", font=label_font, bg="#1e1e2e", fg="#ffffff").pack()
weight_entry = tk.Entry(root, font=label_font, width=20, justify='center')
weight_entry.pack(pady=5)
tk.Label(root, text="Height (cm):", font=label_font, bg="#1e1e2e", fg="#ffffff").pack()
height_entry = tk.Entry(root, font=label_font, width=20, justify='center')
height_entry.pack(pady=5)
tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    font=button_font,
    bg="#89b4fa",
    fg="black",
    activebackground="#74c7ec",
    relief="flat",
    padx=10,
    pady=5).pack(pady=20)
result_label = tk.Label(root, text="", font=label_font, bg="#1e1e2e", fg="#ffffff")
result_label.pack(pady=10)
root.mainloop()
