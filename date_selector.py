import tkinter as tk
from datetime import datetime, timedelta

def select_date():
    """
    Opens a GUI with two buttons for selecting 'Today' or 'Next Day'.
    Displays the current time and date above the buttons.
    Returns the selected date as a datetime object.
    """
    selected_date = None

    def set_today():
        nonlocal selected_date
        selected_date = datetime.now()
        root.destroy()

    def set_next_day():
        nonlocal selected_date
        selected_date = datetime.now() + timedelta(days=1)
        root.destroy()

    # Get current time and date
    current_time = datetime.now().strftime("%I:%M %p")  # Format: HH:MM AM/PM
    current_date = datetime.now().strftime("%B %d, %Y")  # Format: Month Day, Year

    # Get today's and next day's dates in 'Month Day' format
    today_date = datetime.now().strftime("%B %d")
    next_day_date = (datetime.now() + timedelta(days=1)).strftime("%B %d")

    # Create the GUI
    root = tk.Tk()
    root.title("Select Date")
    root.geometry("300x200")

    # Display current time and date
    time_label = tk.Label(root, text=f"Current Time: {current_time}", font=("Arial", 12))
    time_label.pack(pady=5)

    date_label = tk.Label(root, text=f"Current Date: {current_date}", font=("Arial", 12))
    date_label.pack(pady=5)

    # Display the prompt
    label = tk.Label(root, text="Check flights for:", font=("Arial", 14))
    label.pack(pady=10)

    # Buttons for selecting today or the next day
    today_button = tk.Button(root, text=f"Today - {today_date}", font=("Arial", 12), command=set_today)
    today_button.pack(pady=5)

    next_day_button = tk.Button(root, text=f"The next day - {next_day_date}", font=("Arial", 12), command=set_next_day)
    next_day_button.pack(pady=5)

    root.mainloop()
    return selected_date