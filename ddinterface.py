import tkinter as tk
from tkinter import ttk


def submit():
    option1_value = option1_var.get()
    option2_value = option2_var.get()
    degree_type1 = degree_type_var1.get()
    degree_type2 = degree_type_var2.get()

    # Update labels with selected values
    label_option1_result.config(text=f"Option 1: {option1_value} {degree_type1}")
    label_option2_result.config(text=f"Option 2: {option2_value} {degree_type2}")


# Create the main window
root = tk.Tk()
root.title("Double Dip")
root.geometry("600x500")

# Title Label
title_label = tk.Label(root, text="Double Dip", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=4, pady=10)

# Option 1 Label and Dropdown
label_option1 = tk.Label(root, text="Option 1")
label_option1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

codes = ["ANTH", "ARTH", "ARTS", "BIOL", "CHEM", "CHST", "CLAS", "CSCI", "COMM", "DNCE", "ECON", "ENGL", "ENVS", "ETHN",
         "HIST", "MATH", "MUSC", "NEUR", "PHIL", "PHSC", "PHYS", "POLI", "PSYC", "RSOC", "SOCI", "WGST"]
option1_var = tk.StringVar()
option1_dropdown = ttk.Combobox(root, textvariable=option1_var, values=codes)
option1_dropdown.grid(row=1, column=1, padx=10, pady=10)
option1_dropdown.set(codes[0])  # Set default value

# Degree Type Label and Dropdown

degree_types = ["Major", "Minor"]
degree_type_var1 = tk.StringVar()
degree_type_var2 = tk.StringVar()

degree_type_dropdown1 = ttk.Combobox(root, textvariable=degree_type_var1, values=degree_types)
degree_type_dropdown1.grid(row=1, column=3, padx=10, pady=10)
degree_type_dropdown1.set(degree_types[0])  # Set default value

degree_type_dropdown2 = ttk.Combobox(root, textvariable=degree_type_var2, values=degree_types)
degree_type_dropdown2.grid(row=2, column=3, padx=10, pady=10)
degree_type_dropdown2.set(degree_types[0])  # Set default value

# Option 2 Label and Dropdown
label_option2 = tk.Label(root, text="Option 2")
label_option2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

option2_var = tk.StringVar()
option2_dropdown = ttk.Combobox(root, textvariable=option2_var, values=codes)
option2_dropdown.grid(row=2, column=1, padx=10, pady=10)
option2_dropdown.set(codes[1])  # Set default value

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0, columnspan=4, pady=20)

# Result Labels
label_option1_result = tk.Label(root, text="Option 1:")
label_option1_result.grid(row=1, column=4, padx=10, pady=10, sticky="w")

label_option2_result = tk.Label(root, text="Option 2:")
label_option2_result.grid(row=2, column=4, padx=10, pady=10, sticky="w")

# Run the Tkinter event loop
root.mainloop()
