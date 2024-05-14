import tkinter as tk
from tkinter import messagebox


def calculate_installment():
    try:
        loan_amount = int(loan_amount_entry.get())
        years = int(years_entry.get())
        job = job_var.get()


        interest_rates = {1: 13.76, 3: 14.06, 5: 14.87, 7: 15.71}
        interest_rate = interest_rates.get(years)

        if not interest_rate:
            raise ValueError("Invalid number of years")

        interest_in_one_year = loan_amount * interest_rate / 100
        total_interests = interest_in_one_year * years
        total_loan = loan_amount + total_interests
        monthly_payment = total_loan / (years * 12)

        result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid values.")

# Function to clear the input fields
def clear_fields():
    loan_amount_entry.delete(0, tk.END)
    years_entry.delete(0, tk.END)
    result_label.config(text="")
    job_var.set("")

# GUI setup
root = tk.Tk()
root.title("Bank Misr – Plan Your Loan Application")

# Background Image
bg_image = tk.PhotoImage(file="bankmisr.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Job Selection
job_var = tk.StringVar()
job_label = tk.Label(root, text="Select Your Job:", bg="#6b9dc2", font=("Arial", 12))
job_label.place(relx=0.5, rely=0.2, anchor="center")
jobs = ["Doctor", "Engineer", "Teacher", "Other"]
job_dropdown = tk.OptionMenu(root, job_var, *jobs)
job_dropdown.config(bg="#d9d9d9", font=("Arial", 10))
job_dropdown.place(relx=0.5, rely=0.25, anchor="center")

# Loan Amount Entry
loan_amount_label = tk.Label(root, text="Enter Loan Amount:", bg="#6b9dc2", font=("Arial", 12))
loan_amount_label.place(relx=0.5, rely=0.35, anchor="center")
loan_amount_entry = tk.Entry(root, bg="#d9d9d9", font=("Arial", 10))
loan_amount_entry.place(relx=0.5, rely=0.4, anchor="center")

# Years Entry
years_label = tk.Label(root, text="Enter Number of Years:", bg="#6b9dc2", font=("Arial", 12))
years_label.place(relx=0.5, rely=0.5, anchor="center")
years_entry = tk.Entry(root, bg="#d9d9d9", font=("Arial", 10))
years_entry.place(relx=0.5, rely=0.55, anchor="center")

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", bg="#4caf50", fg="white", font=("Arial", 12), command=calculate_installment)
calculate_button.place(relx=0.3, rely=0.65, anchor="center")

# Clear Button
clear_button = tk.Button(root, text="Clear", bg="#f44336", fg="white", font=("Arial", 12), command=clear_fields)
clear_button.place(relx=0.5, rely=0.65, anchor="center")

# Result Label
result_label = tk.Label(root, bg="#6b9dc2", font=("Arial", 12))
result_label.place(relx=0.5, rely=0.75, anchor="center")

# Exit Button
exit_button = tk.Button(root, text="Exit", bg="#f44336", fg="white", font=("Arial", 12), command=root.destroy)
exit_button.place(relx=0.7, rely=0.65, anchor="center")

root.mainloop()
