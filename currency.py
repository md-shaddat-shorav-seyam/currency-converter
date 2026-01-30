import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/{}"

def convert_currency():
    from_currency = from_var.get()
    to_currency = to_var.get()
    amount = amount_entry.get()

    if not amount:
        messagebox.showerror("Error", "Please enter an amount")
        return

    try:
        amount = float(amount)
        response = requests.get(API_URL.format(from_currency))
        data = response.json()

        rate = data["rates"][to_currency]
        result = amount * rate

        result_label.config(
            text=f"{amount} {from_currency} = {result:.2f} {to_currency}"
        )

    except ValueError:
        messagebox.showerror("Error", "Invalid number")
    except KeyError:
        messagebox.showerror("Error", "Invalid currency code")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Currency Converter", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="From Currency (USD, EUR, BDT)").pack()
from_var = tk.StringVar(value="USD")
from_entry = tk.Entry(root, textvariable=from_var)
from_entry.pack()

tk.Label(root, text="To Currency (USD, EUR, BDT)").pack()
to_var = tk.StringVar(value="BDT")
to_entry = tk.Entry(root, textvariable=to_var)
to_entry.pack()

tk.Button(root, text="Convert", command=convert_currency).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
