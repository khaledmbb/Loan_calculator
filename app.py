from tkinter import *  # type:ignore
import ttkbootstrap as ttk
from ttkbootstrap.constants import *  # type:ignore
from tkinter import font  # type:ignore
from tkinter import messagebox


class App:
    def __init__(self):
        self.root = ttk.Window(themename="lumen", title="Loan calculator")
        self.root.geometry("600x620")
        self.root.maxsize(600, 620)
        self.fonts = font.families()

        self.font = ("jetbrains mono", 12)
        self.root.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)  # type: ignore
        self.root.configure(padx=15, pady=15)

        self.create_gui()

    def create_gui(self):
        my_style = ttk.Style()
        my_style.configure("success.Outline.TButton", font=(self.font[0], 15, "bold"))

        title = ttk.Label(
            self.root, text="Loan calculator :", font=(self.font[0], 15, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="nsw")

        loan_amount_lb = ttk.Label(self.root, text="Loan amount :", font=self.font)
        loan_amount_lb.grid(row=1, column=0, sticky="nsew", pady=20)

        loan_amount_spinbox = ttk.Spinbox(
            self.root,
            from_=1,
            to=10**9,
            bootstyle="success",
            font=self.font,
        )
        loan_amount_spinbox.grid(row=1, column=4, sticky="nsew", pady=20)

        interest_rate_lb = ttk.Label(self.root, text="interest rate :", font=self.font)
        interest_rate_lb.grid(row=2, column=0, sticky="nsew", pady=20)

        interest_rate_spinbox = ttk.Spinbox(
            self.root,
            from_=1,
            to=100,
            bootstyle="success",
            font=self.font,
        )
        interest_rate_spinbox.grid(row=2, column=4, sticky="nsew", pady=20)

        month_lb = ttk.Label(self.root, text="Years / Months :", font=self.font)
        month_lb.grid(row=3, column=0, sticky="nsew", pady=20)

        year_spinbox = ttk.Spinbox(
            self.root,
            from_=0,
            to=10**3,
            bootstyle="success",
            font=self.font,
            width=8,
        )

        year_spinbox.grid(row=3, column=4, sticky="nsw", pady=20)
        month_spinbox = ttk.Spinbox(
            self.root,
            from_=0,
            to=10**3,
            bootstyle="success",
            font=self.font,
            width=8,
        )
        month_spinbox.grid(row=3, column=4, sticky="nse", pady=20)

        calc_btn = ttk.Button(
            self.root,
            style="success.Outline.TButton",
            text="Calculate",
            bootstyle="success outline",
            padding=(20, 10),
            command=lambda: self.check_error(
                loan_amount_spinbox.get(),
                interest_rate_spinbox.get(),
                year_spinbox.get(),
                month_spinbox.get(),
            ),
        )
        calc_btn.grid(row=4, column=0, columnspan=2, sticky="nsew")

        clear_btn = ttk.Button(
            self.root,
            style="success.Outline.TButton",
            text="Clear",
            bootstyle="success outline",
            padding=(20, 10),
            command=lambda: self.clear(
                interest_rate_spinbox,
                loan_amount_spinbox,
                year_spinbox,
                month_spinbox,
            ),
        )

        clear_btn.grid(row=4, column=4, columnspan=2, sticky="nsew")

        result_title = ttk.Label(
            self.root, text="Calculated result :", font=(self.font[0], 15, "bold")
        )
        result_title.grid(row=5, column=0, columnspan=2, sticky="nsw", pady=20)

        monthly_payment_lb = ttk.Label(
            self.root, text="Monthly Payment :", font=self.font
        )
        monthly_payment_lb.grid(row=6, column=0, sticky="nsew", columnspan=2, pady=10)

        self.monthly_payment = ttk.Label(self.root, text="$ 00.00", font=self.font)
        self.monthly_payment.grid(row=6, column=4, sticky="nsew", columnspan=2)

        total_interest_lb = ttk.Label(
            self.root, text="Total interest :", font=self.font
        )
        total_interest_lb.grid(row=7, column=0, sticky="nsew", columnspan=2, pady=10)

        self.total_interest = ttk.Label(self.root, text="% 00", font=self.font)
        self.total_interest.grid(row=7, column=4, sticky="nsew", columnspan=2)

        total_amount_lb = ttk.Label(self.root, text="Total amount :", font=self.font)
        total_amount_lb.grid(row=8, column=0, sticky="nsew", columnspan=2, pady=10)

        self.total_amount = ttk.Label(self.root, text="$ 00.00", font=self.font)
        self.total_amount.grid(row=8, column=4, sticky="nsew", columnspan=2)

    def calc_loan(self, loan_amount, interest, year, month):
        months = year * 12 + month
        monthly_payment = (loan_amount * interest * (1 + interest) ** months) / (
            (1 + interest) ** months - 1
        )
        total_interest = (monthly_payment * months) - loan_amount
        total_payment = loan_amount + total_interest

        self.monthly_payment["text"] = "$ " + str(round(monthly_payment, 2))
        self.total_interest["text"] = str(round(total_interest, 2)) + " %"
        self.total_amount["text"] = "$ " + str(round(total_payment, 2))

        loan_amount = 0
        interest = 0
        year = 0
        month = 0

    def clear(self, loan_amount, interest, year, month):
        loan_amount.delete(0, END)
        interest.delete(0, END)
        year.delete(0, END)
        month.delete(0, END)
        self.monthly_payment["text"] = "$ 00.00"
        self.total_interest["text"] = "% 00"
        self.total_amount["text"] = "$ 00.00"

    def check_error(self, loan_amount, interest, year, month):
        try:
            if (
                type(int(loan_amount)) == int
                and type(int(interest)) == int
                and type(int(year)) == int
                and type(int(month))
            ):
                pass
        except ValueError:
            messagebox.showerror("Value error", "Please enter a valid number")
        else:
            self.calc_loan(
                int(loan_amount), int(interest) / 100 / 12, int(year), int(month)
            )

    def run_app(self):
        self.root.mainloop()


app = App()
app.run_app()
