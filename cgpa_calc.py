import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_sgpa(sem, value):
    try:
        sgpa = float(value)
        if sgpa < 0 or sgpa > 10:
            return
        sgpa_list[sem] = round(sgpa, 2)
        sgpa_scales[sem].set(sgpa)
        update_graph()
    except ValueError:
        return

def scale_update_sgpa(sem, value):
    sgpa = float(value)
    sgpa_list[sem] = round(sgpa, 2)
    sgpa_entries[sem].delete(0, tk.END)
    sgpa_entries[sem].insert(0, str(sgpa))
    update_graph()

def entry_update_sgpa(event, sem):
    value = sgpa_entries[sem].get()
    update_sgpa(sem, value)

def update_target_cgpa(val):
    target_cgpa = float(val)
    calculate_cgpa(target_cgpa)

def calculate_cgpa(target_cgpa):
    num_semesters_completed = len(sgpa_list)
    current_cgpa = sum(sgpa_list) / num_semesters_completed if num_semesters_completed > 0 else 0
    cgpa_label.config(text=f"Current CGPA: {current_cgpa:.2f}")

    remaining_semesters = 8 - num_semesters_completed
    total_sgpa_needed = target_cgpa * 8 - sum(sgpa_list)
    
    if total_sgpa_needed > remaining_semesters * 10:
        result.set(f"Target CGPA not achievable. Max possible CGPA: {((sum(sgpa_list) + remaining_semesters * 10) / 8):.2f}")
    else:
        optimum_sgpa = total_sgpa_needed / remaining_semesters
        result.set(f"Optimum SGPA for remaining semesters: {optimum_sgpa:.2f}")

def update_graph():
    ax.clear()
    ax.plot(range(1, len(sgpa_list) + 1), sgpa_list, marker='o')
    ax.set_xlabel('Semester')
    ax.set_ylabel('SGPA')
    ax.set_title('SGPA per Semester')
    ax.set_xticks(range(1, 9))
    ax.set_yticks(range(0, 11))
    ax.grid(True)
    canvas.draw()

def semesters_completed():
    try:
        num_semesters = int(semesters_entry.get())
        if num_semesters < 1 or num_semesters > 8:
            semesters_entry.delete(0, tk.END)
            semesters_entry.insert(0, "Enter 1-8")
            return
        create_sgpa_inputs(num_semesters)
    except ValueError:
        semesters_entry.delete(0, tk.END)
        semesters_entry.insert(0, "Invalid Input")

def create_sgpa_inputs(num_semesters):
    for widget in sgpa_frame.winfo_children():
        widget.destroy()
    sgpa_entries.clear()
    sgpa_scales.clear()
    sgpa_list.clear()

    for i in range(num_semesters):
        sgpa_label = tk.Label(sgpa_frame, text=f"SGPA {i+1}:")
        sgpa_label.grid(row=i, column=0)

        sgpa_entry = tk.Entry(sgpa_frame)
        sgpa_entry.grid(row=i, column=1)
        sgpa_entry.insert(0, "0.00")
        sgpa_entry.bind('<FocusOut>', lambda event, sem=i: entry_update_sgpa(event, sem))
        sgpa_entries.append(sgpa_entry)

        sgpa_scale = tk.Scale(sgpa_frame, from_=0, to=10, resolution=0.01, orient=tk.HORIZONTAL, command=lambda value, sem=i: scale_update_sgpa(sem, value))
        sgpa_scale.set(0)
        sgpa_scale.grid(row=i, column=2)
        sgpa_scales.append(sgpa_scale)

        sgpa_list.append(0.0)

# Initialize tkinter window
window = tk.Tk()
window.title("CGPA Calculator")

sgpa_list = []
sgpa_entries = []
sgpa_scales = []

# Number of semesters completed input
semesters_label = tk.Label(window, text="Semesters Completed:")
semesters_label.grid(row=0, column=0)
semesters_entry = tk.Entry(window)
semesters_entry.grid(row=0, column=1)
semesters_button = tk.Button(window, text="Enter", command=semesters_completed)
semesters_button.grid(row=0, column=2)

# Frame for SGPA inputs
sgpa_frame = tk.Frame(window)
sgpa_frame.grid(row=1, columnspan=4)

# Target CGPA scale
target_cgpa_label = tk.Label(window, text="Target CGPA:")
target_cgpa_label.grid(row=2, column=0)
target_cgpa_scale = tk.Scale(window, from_=0, to=10, resolution=0.01, orient=tk.HORIZONTAL, command=update_target_cgpa)
target_cgpa_scale.set(0)
target_cgpa_scale.grid(row=2, column=1)

# Current CGPA label
cgpa_label = tk.Label(window, text="Current CGPA: 0.00")
cgpa_label.grid(row=3, columnspan=3)

# Result label
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.grid(row=4, columnspan=3)

# Graph setup
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=window)  
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=5, columnspan=3)

window.mainloop()
