import tkinter as tk
from tkinter import Label, Button, Entry, IntVar, Checkbutton, messagebox

from faker_generator import generate_data, data_types


def generate_fake_data():
    try:
        records = int(entry.get())
        selected_data_types = [data_type for data_type, var in data_type_vars.items() if var.get()]
        if not selected_data_types:
            messagebox.showerror("Error", "Please select at least one data type.")
            return

        generate_data(records, selected_data_types)
        messagebox.showinfo("Success", f"Fake data generated successfully! Data saved in: fake_data.json")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


# Create the main window
window = tk.Tk()

# Set the window title
window.title("Fake Data Generator")

# Set the window size (width x height)
window.geometry("400x400")

# Create a label and an entry widget for the user to enter the number of records
label_records = Label(window, text="Enter the number of records:")
label_records.pack(pady=10)

entry = Entry(window, width=35)
entry.pack(pady=5)

# Create IntVar instances to track the state of checkboxes
data_type_vars = {}

# Create Checkbutton widgets for each data type
for data_type in data_types:
    data_type_vars[data_type] = IntVar()
    checkbox = Checkbutton(window, text=data_type, variable=data_type_vars[data_type])
    checkbox.pack(anchor="w")

# Create a button to exit the program
exit_button = Button(window, text="Exit", height=2, width=10, command=window.destroy)
exit_button.pack(pady=5, side=tk.BOTTOM)

# Create a button to trigger the fake data generation
generate_button = Button(window, text="Generate Fake Data", height=2, width=20, command=generate_fake_data)
generate_button.pack(pady=5, side=tk.BOTTOM)

# Start the Tkinter event loop
window.mainloop()
