from tkinter import *
from tkinter import messagebox

def predict():
    try:
        attendance = int(attendance_entry.get())
        assignment = int(assignment_entry.get())
        test = int(test_entry.get())
        study = int(study_entry.get())

        score = (attendance * 0.3) + (assignment * 1.5) + (test * 1.2) + (study * 5)

        if score >= 100:
            result = "Excellent"
            color = "#00ff7f"
            suggestion = "Outstanding Performance!"
        elif score >= 80:
            result = "Good"
            color = "#00bfff"
            suggestion = "Keep Working Hard!"
        elif score >= 60:
            result = "Average"
            color = "#ffd700"
            suggestion = "Practice More."
        else:
            result = "Poor"
            color = "#ff4444"
            suggestion = "Need Improvement."

        result_label.config(
            text=f"Performance : {result}",
            fg=color
        )

        suggestion_label.config(
            text=suggestion,
            fg=color
        )

    except:
        messagebox.showerror("Error", "Please Enter Valid Numbers")


root = Tk()
root.title("AI Student Performance Predictor")
root.geometry("600x650")
root.configure(bg="#2d033b")

title = Label(
    root,
    text="STUDENT PERFORMANCE PREDICTOR",
    font=("Arial", 20, "bold"),
    bg="#2d033b",
    fg="#ff66c4"
)
title.pack(pady=20)

Label(
    root,
    text="Attendance (%)",
    font=("Arial", 12, "bold"),
    bg="#2d033b",
    fg="white"
).pack()

attendance_entry = Entry(
    root,
    font=("Arial", 12),
    width=25,
    bg="#810ca8",
    fg="white",
    insertbackground="white"
)
attendance_entry.pack(pady=8)

Label(
    root,
    text="Assignment Marks (0-20)",
    font=("Arial", 12, "bold"),
    bg="#2d033b",
    fg="white"
).pack()

assignment_entry = Entry(
    root,
    font=("Arial", 12),
    width=25,
    bg="#810ca8",
    fg="white",
    insertbackground="white"
)
assignment_entry.pack(pady=8)

Label(
    root,
    text="Test Marks (0-50)",
    font=("Arial", 12, "bold"),
    bg="#2d033b",
    fg="white"
).pack()

test_entry = Entry(
    root,
    font=("Arial", 12),
    width=25,
    bg="#810ca8",
    fg="white",
    insertbackground="white"
)
test_entry.pack(pady=8)

Label(
    root,
    text="Study Hours Per Day",
    font=("Arial", 12, "bold"),
    bg="#2d033b",
    fg="white"
).pack()

study_entry = Entry(
    root,
    font=("Arial", 12),
    width=25,
    bg="#810ca8",
    fg="white",
    insertbackground="white"
)
study_entry.pack(pady=8)

Button(
    root,
    text="PREDICT PERFORMANCE",
    command=predict,
    font=("Arial", 13, "bold"),
    bg="#ff66c4",
    fg="black",
    width=20
).pack(pady=25)

result_label = Label(
    root,
    text="",
    font=("Arial", 18, "bold"),
    bg="#2d033b"
)
result_label.pack(pady=10)

suggestion_label = Label(
    root,
    text="",
    font=("Arial", 13, "bold"),
    bg="#2d033b"
)
suggestion_label.pack(pady=10)

footer = Label(
    root,
    text="AI Powered Student Analysis System",
    font=("Arial", 10, "italic"),
    bg="#2d033b",
    fg="#ff66c4"
)
footer.pack(side=BOTTOM, pady=15)

root.mainloop()