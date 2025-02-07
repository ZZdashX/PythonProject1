import tkinter as tk

def convert_kg_to_lbs():
    try:
        kg = float(entry.get())
        lbs = kg * 2.20462
        result_label.config(text=f"{kg} kg = {lbs:.2f} lbs")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

root = tk.Tk()
root.title("Kg to Lbs Converter")

label = tk.Label(root, text="Enter weight in kilograms:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_kg_to_lbs)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()