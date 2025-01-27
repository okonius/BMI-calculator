import tkinter as tk
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")

# GUI elements
labelWel = tk.Label(root, text="Welcome to BMI Calculator")

labelH = tk.Label(root, text="Height (cm):")
entryH = tk.Entry(root)

labelW = tk.Label(root, text="Weight (kg):")
entryW = tk.Entry(root)


def calculate():
    height = entryH.get()
    weight = entryW.get()
    if height and weight:
        try:
            height = float(height)
            weight = float(weight)
            bmi = weight / (height / 100) ** 2
            labelBMI.config(text=f"Your BMI is: {bmi:.2f}")
        except ValueError:
            labelBMI.config(text="Please enter valid numbers")
    else:
        labelBMI.config(text="Please enter both height and weight")

        
buttonSubmit = tk.Button(root, text="Calculate BMI", command=calculate)

labelBMI = tk.Label(root, text="Your BMI is:")

# Packing
labelWel.pack()
labelH.pack()
entryH.pack(pady=5)
labelW.pack()
entryW.pack(pady=5)
buttonSubmit.pack(pady=5)
labelBMI.pack()

root.mainloop()