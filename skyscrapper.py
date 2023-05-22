#Created on Mon May 22 13:05:22 2023
#Author JJF3

import tkinter as tk

def calculate_area():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        height = float(height_entry.get())

        area = length * width * height

        result_label.config(text=f"The total floor area is: {area} square units")
    except ValueError:
        result_label.config(text="Please enter valid numeric values")

# Create the main window
window = tk.Tk()
window.title("Skyscraper Area Calculator")

# Create labels and entry fields for dimensions
length_label = tk.Label(window, text="Length:")
length_entry = tk.Entry(window)
width_label = tk.Label(window, text="Width:")
width_entry = tk.Entry(window)
height_label = tk.Label(window, text="Height:")
height_entry = tk.Entry(window)

length_label.pack()
length_entry.pack()
width_label.pack()
width_entry.pack()
height_label.pack()
height_entry.pack()

# Create a button to calculate the area
calculate_button = tk.Button(window, text="Calculate", command=calculate_area)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main loop
window.mainloop()
