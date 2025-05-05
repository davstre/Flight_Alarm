from flight_scraper import get_alarm_time
from alarm_scheduler import schedule_alarm_on_kukuklok
from date_selector import select_date

def main():
    # Get the selected date from the GUI
    flight_date = select_date()

    if flight_date:
        # Get the alarm time from the scraper
        alarm_time = get_alarm_time(flight_date)

        if alarm_time:
            print(f"Alarm time calculated: {alarm_time}")
            # Schedule the alarm
            schedule_alarm_on_kukuklok(alarm_time)
        else:
            print("No valid alarm time found.")
    else:
        print("No date selected.")

if __name__ == "__main__":
    main()