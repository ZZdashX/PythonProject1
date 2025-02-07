import tkinter as tk

def convert_celsius_to_fahrenheit():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

root = tk.Tk()
root.title("Celsius to Fahrenheit Converter")

label = tk.Label(root, text="Enter temperature in Celsius:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_celsius_to_fahrenheit)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()