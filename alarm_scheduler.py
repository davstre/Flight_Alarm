from plyer import notification
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def schedule_alarm_on_kukuklok(alarm_time):
    # ✅ ChromeDriver path
    chromedriver_path = 'C:/WebDrivers/chromedriver.exe'

    # Start driver using Service
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

    try:
        # Open kukuklok.com
        driver.get("https://kukuklok.com/")
        time.sleep(5)  # Wait for the page to load

        # Parse the alarm time
        hour, minute = map(int, alarm_time.split(":"))
        hour_one, hour_two = divmod(hour, 10)  # Split hour into tens and ones
        minute_one, minute_two = divmod(minute, 10)  # Split minute into tens and ones

        # Adjust the hours (tens digit)
        current_hour_one = int(driver.find_element("id", "hours_one").text)
        while current_hour_one != hour_one:
            driver.find_element("id", "button_plus_hour").click()
            time.sleep(0.5)  # Wait for the UI to update
            current_hour_one = int(driver.find_element("id", "hours_one").text)

        # Adjust the hours (ones digit)
        current_hour_two = int(driver.find_element("id", "hours_two").text)
        while current_hour_two != hour_two:
            driver.find_element("id", "button_plus_hour").click()
            time.sleep(0.5)  # Wait for the UI to update
            current_hour_two = int(driver.find_element("id", "hours_two").text)

        # Adjust the minutes (tens digit)
        current_minute_one = int(driver.find_element("id", "minutes_one").text)
        while current_minute_one != minute_one:
            driver.find_element("id", "button_plus_min").click()
            time.sleep(0.5)  # Wait for the UI to update
            current_minute_one = int(driver.find_element("id", "minutes_one").text)

        # Adjust the minutes (ones digit)
        current_minute_two = int(driver.find_element("id", "minutes_two").text)
        while current_minute_two != minute_two:
            driver.find_element("id", "button_plus_min").click()
            time.sleep(0.5)  # Wait for the UI to update
            current_minute_two = int(driver.find_element("id", "minutes_two").text)

        # Activate the alarm
        driver.find_element("id", "set_alarm_button").click()
        print("Alarm successfully scheduled on kukuklok.com!")

        # Notify the user
        notification.notify(
            title="🚨 Flight Alarm Scheduled!",
            message=f"Alarm set for {alarm_time} on kukuklok.com.",
            timeout=10
        )
    finally:
        # Do not close the browser
        pass