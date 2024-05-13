import tkinter as tk
from tkinter import messagebox

class LoanCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Misr - Plan Your Loan Application")

        self.bg_image = tk.PhotoImage(file="Bankmisr.png")
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)


        self.job_label = tk.Label(root, text="Select Your Job:")
        self.job_label.place(relx=0.1, rely=0.1)
        self.job_var = tk.StringVar(root)
        self.job_var.set("Select Job")
        self.job_options = ["Doctor", "Engineer", "Teacher", "Other"]
        self.job_dropdown = tk.OptionMenu(root, self.job_var, *self.job_options)
        self.job_dropdown.place(relx=0.3, rely=0.1)


        self.loan_label = tk.Label(root, text="Enter Loan Amount:")
        self.loan_label.place(relx=0.1, rely=0.2)
        self.loan_entry = tk.Entry(root)
        self.loan_entry.place(relx=0.3, rely=0.2)


        self.duration_label = tk.Label(root, text="Enter Loan Duration (in years):")
        self.duration_label.place(relx=0.1, rely=0.3)
        self.duration_entry = tk.Entry(root)
        self.duration_entry.place(relx=0.3, rely=0.3)


        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_loan)
        self.calculate_button.place(relx=0.4, rely=0.4)


        self.output_label = tk.Label(root, text="")
        self.output_label.place(relx=0.1, rely=0.6)


        self.clear_button = tk.Button(root, text="Clear", command=self.clear_inputs)
        self.clear_button.place(relx=0.3, rely=0.4)


        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.place(relx=0.5, rely=0.4)

    def calculate_loan(self):
        job = self.job_var.get()
        loan_amount = self.loan_entry.get()
        duration_years = self.duration_entry.get()

        try:
            loan_amount = float(loan_amount)
            duration_years = int(duration_years)
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")
            return

        if job == "Select Job":
            messagebox.showerror("Error", "Please select your job.")
            return


        if duration_years == 1:
            interest_rate = 13.76
        elif duration_years == 3:
            interest_rate = 14.06
        elif duration_years == 5:
            interest_rate = 14.87
        elif duration_years == 7:
            interest_rate = 15.71
        else:
            messagebox.showerror("Error", "Invalid loan duration! Please enter 1, 3, 5, or 7 years.")
            return


        total_interests = loan_amount * (interest_rate / 100) * duration_years
        total_loan = loan_amount + total_interests


        monthly_payment = total_loan / (duration_years * 12)


        output_text = f"Total Interests: {total_interests:.2f}\nTotal Loan: {total_loan:.2f}\nMonthly Payment: {monthly_payment:.2f}"
        self.output_label.config(text=output_text)

    def clear_inputs(self):
        self.job_var.set("Select Job")
        self.loan_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.output_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoanCalculatorApp(root)
    root.mainloop()