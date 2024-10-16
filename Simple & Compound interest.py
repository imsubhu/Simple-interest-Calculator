import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import ttkbootstrap as ttkb
from tkinter.font import Font

# Function to automatically resize text based on window size
def resize_text(event):
    new_size = max(12, int(root.winfo_width() / 30))
    font.configure(size=new_size)

# Function to calculate Simple Interest
def calculate_simple_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        start_date = datetime.strptime(start_date_entry.get(), "%Y-%m-%d")
        end_date = datetime.strptime(end_date_entry.get(), "%Y-%m-%d")
        days = (end_date - start_date).days

        if days < 0:
            raise ValueError("समाप्त मिति सुरु मितिपछि हुनुपर्छ।")

        # Adjust the rate if it is per month
        if rate_type.get() == "महिना अनुसार":
            rate = rate * 12  # Convert to yearly rate

        interest = principal * (rate / 100) * (days / 365)
        total_amount = principal + interest

        result_text = (
            f"अवधि: {days} दिन\n"
            f"ब्याज रकम: ₨ {interest:.2f}\n"
            f"कुल रकम: ₨ {total_amount:.2f}"
        )
        result_label.config(text=result_text)
    except Exception as e:
        messagebox.showerror("त्रुटि", f"अमान्य इनपुट: {e}")

# Function to calculate Compound Interest
def calculate_compound_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        start_date = datetime.strptime(start_date_entry.get(), "%Y-%m-%d")
        end_date = datetime.strptime(end_date_entry.get(), "%Y-%m-%d")
        days = (end_date - start_date).days

        if days < 0:
            raise ValueError("समाप्त मिति सुरु मितिपछि हुनुपर्छ।")

        # Adjust the rate if it is per month
        if rate_type.get() == "महिना अनुसार":
            rate = rate * 12  # Convert to yearly rate

        n = 12  # Compounded monthly
        t = days / 365

        amount = principal * (1 + (rate / (100 * n)))**(n * t)
        interest = amount - principal
        total_amount = amount

        result_text = (
            f"अवधि: {days} दिन\n"
            f"ब्याज रकम: ₨ {interest:.2f}\n"
            f"कुल रकम: ₨ {total_amount:.2f}"
        )
        result_label.config(text=result_text)
    except Exception as e:
        messagebox.showerror("त्रुटि", f"अमान्य इनपुट: {e}")

# Function to switch between Simple and Compound Interest calculations
def switch_calculation_mode(event):
    mode = interest_type.get()
    if mode == 'साधारण ब्याज':
        calculate_button.config(command=calculate_simple_interest)
    elif mode == 'चक्रवृद्धि ब्याज':
        calculate_button.config(command=calculate_compound_interest)

# Function to show the About section
def show_about():
    messagebox.showinfo(
        "ABOUT",
        "साधारण र चक्रवृद्धि ब्याजको गणना गर्ने एप्लिकेसन।\n"
        "साधारण र चक्रवृद्धि ब्याजलाई विभिन्न अवधि र दरमा गणना गर्न सकिने।\n"
        "Developed by imsubhu\n"
        "Love From Nepal"
    )

# Create main application window
root = ttkb.Window(themename="flatly")  # Bootstrap theme for modern look
root.title("साधारण ब्याज हिसाब किताब ")
root.geometry("600x600")
root.minsize(400, 400)

# Font for dynamic resizing
font = Font(family="Arial", size=12)
result_font = Font(family="Arial", size=14, weight="bold")  # Bold font for results

# Make the window resizable
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create the menu
menubar = tk.Menu(root)
root.config(menu=menubar)

# Add About menu to the right
about_menu = tk.Menu(menubar, tearoff=0)
about_menu.add_command(label="हाम्रो बारे ", command=show_about)
menubar.add_cascade(label="हाम्रो बारे ", menu=about_menu)

# Title Label
title_label = ttkb.Label(root, text="साधारण ब्याज हिसाब किताब ", font=("Arial", 18, "bold"), bootstyle="info")
title_label.pack(pady=10)

# Frame to hold input fields and make UI responsive
frame = ttkb.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

# Principal amount input
ttkb.Label(frame, text="ऋण दिएको रकम (₨):").grid(row=0, column=0, sticky=tk.W, pady=5)
principal_entry = ttkb.Entry(frame)
principal_entry.grid(row=0, column=1, pady=5, sticky="ew")

# Interest rate input (annual or monthly rate in percentage)
ttkb.Label(frame, text="ब्याज दर (%):").grid(row=1, column=0, sticky=tk.W, pady=5)
rate_entry = ttkb.Entry(frame)
rate_entry.grid(row=1, column=1, pady=5, sticky="ew")

# Dropdown to select rate type (per year or per month)
ttkb.Label(frame, text="ब्याज दरको प्रकार:").grid(row=2, column=0, sticky=tk.W, pady=5)
rate_type = ttkb.Combobox(frame, values=["वर्ष अनुसार", "महिना अनुसार"], state="readonly")
rate_type.current(0)
rate_type.grid(row=2, column=1, pady=5, sticky="ew")

# Start Date input
ttkb.Label(frame, text="रकम दिएको मिति (YYYY-MM-DD):").grid(row=3, column=0, sticky=tk.W, pady=5)
start_date_entry = ttkb.Entry(frame)
start_date_entry.grid(row=3, column=1, pady=5, sticky="ew")

# End Date input
ttkb.Label(frame, text="रकम प्राप्त मिति (YYYY-MM-DD):").grid(row=4, column=0, sticky=tk.W, pady=5)
end_date_entry = ttkb.Entry(frame)
end_date_entry.grid(row=4, column=1, pady=5, sticky="ew")

# Interest Type (Simple or Compound)
ttkb.Label(frame, text="ब्याजको प्रकार छान्नुहोस्:").grid(row=5, column=0, sticky=tk.W, pady=5)
interest_type = ttkb.Combobox(frame, values=["साधारण ब्याज", "चक्रवृद्धि ब्याज"], state="readonly")
interest_type.current(0)
interest_type.grid(row=5, column=1, pady=5, sticky="ew")

# Button to calculate
calculate_button = ttkb.Button(frame, text="हिसाब गर्नुहोस ", bootstyle="success")
calculate_button.grid(row=6, columnspan=2, pady=20, sticky="ew")

# Bind the interest type selection to switch between calculation modes
interest_type.bind("<<ComboboxSelected>>", switch_calculation_mode)

# Label to display result
result_label = ttkb.Label(root, text="", font=result_font, justify=tk.CENTER, bootstyle="dark")
result_label.pack(pady=10, fill="both", expand=True)

# Start with Simple Interest calculation mode
calculate_button.config(command=calculate_simple_interest)

# Make the frame grid flexible for resizing
for i in range(2):
    frame.columnconfigure(i, weight=1)

# Bind the window resize event to dynamically adjust text size
root.bind('<Configure>', resize_text)

# Start the GUI application
root.mainloop()
