import os
import sys
import threading
from datetime import datetime, timedelta
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Loading animation class
class LoadingAnimation:
    def __init__(self, message="Loading..."):
        self.message = message
        self.done = False

    def start(self):
        def animate():
            while not self.done:
                for char in "|/-\\":  # Cycle through spinner characters
                    if self.done:
                        break
                    sys.stdout.write(f"\r{self.message} {char}")
                    sys.stdout.flush()
                    time.sleep(0.1)
        self.thread = threading.Thread(target=animate)
        self.thread.start()

    def stop(self):
        self.done = True
        self.thread.join()
        sys.stdout.write("\r" + " " * (len(self.message) + 4) + "\r")  # Clear the line
        sys.stdout.flush()

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

def get_alarm_time(flight_date):
    # ✅ ChromeDriver path (relative to the script's directory)
    chromedriver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")

    # Headless Chrome setup
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")  # Suppress logs
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Suppress DevTools logs

    # Start driver
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # 🌐 Generate dynamic FlightStats URL with the selected date
        base_url = "https://www.flightstats.com/v2/flight-tracker/arrivals/CRK/"
        dynamic_url = f"{base_url}?year={flight_date.year}&month={flight_date.month}&date={flight_date.day}&hour=6"
        print(f"Scraping flights for CRK at: {dynamic_url}")

        # Add loading animation
        with LoadingAnimation("Loading flight data..."):
            driver.get(dynamic_url)
            time.sleep(10)  # Wait for dynamic content to load

        # Parse the webpage
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # List of domestic airports to exclude
        domestic_airports = {
            "DVO", "ILO", "KLO", "LAO", "CEB", "MNL", "PPS", "BCD", "DRP", "TAG",
            "BXU", "CYZ", "CBO", "TAC", "DPL", "DGT", "GES", "MPH", "OZC", "CGY",
            "WNP", "PAG", "RXS", "TWT", "SJI", "SFS", "TUG", "ZAM", "BSO", "CYP",
            "CGM", "CRM", "CYU", "EUQ", "USU", "JOL", "BAG", "MRQ", "MBT", "OMC",
            "SGL", "SWL", "IAO", "SUG", "TDG", "TBH", "VRC"
        }

        print("\nInternational Flight Arrivals at CRK:\n")
        print(f"{'Origin Airport':<20} | {'City':<15} | {'Time':<10} | {'Airline':<15}")
        print("-" * 65)

        # First, locate the row correctly
        rows = soup.select("a.table__A-sc-1x7nv9w-2.hnJChl")

        # Initialize a variable to store the earliest time
        earliest_time = None
        earliest_flight = None

        for row in rows:
            # Find the main div inside the <a> tag that contains the flight details
            flight_data_divs = row.find_all("div", class_="table__TableRow-sc-1x7nv9w-7 dQsNBa")

            if len(flight_data_divs) >= 2:
                # First div contains flight, departure, arrival, and origin
                flight_info_div = flight_data_divs[0]
                data_elements = flight_info_div.find_all("h2", class_="table__CellText-sc-1x7nv9w-15 fcTUax")

                arrival_time = data_elements[2].get_text(strip=True) if len(data_elements) > 2 else "Unknown"
                origin_airport = data_elements[3].get_text(strip=True) if len(data_elements) > 3 else "Unknown"

                additional_info_div = flight_data_divs[1]
                span_elements = additional_info_div.find_all("span", class_="table__SubText-sc-1x7nv9w-16 bQPdJx")

                airline = span_elements[0].get_text(strip=True) if len(span_elements) > 0 else "Unknown"
                city = span_elements[1].get_text(strip=True) if len(span_elements) > 1 else "Unknown"

                # ✅ Exclude domestic flights
                if origin_airport not in domestic_airports:
                    # Print the row (bold if it's the earliest flight)
                    if arrival_time != "Unknown" and "cargo" not in airline.lower():
                        arrival_time_obj = datetime.strptime(arrival_time, "%H:%M")
                        if earliest_time is None or arrival_time_obj < earliest_time:
                            earliest_time = arrival_time_obj
                            earliest_flight = (origin_airport, city, arrival_time, airline)

                    # Print the row (bold if it's the earliest flight)
                    if earliest_flight and (origin_airport, city, arrival_time, airline) == earliest_flight:
                        print(f"\033[1m{origin_airport:<20} | {city:<15} | {arrival_time:<10} | {airline:<15}\033[0m")
                    else:
                        print(f"{origin_airport:<20} | {city:<15} | {arrival_time:<10} | {airline:<15}")

        # Offset the earliest time by 2 hours
        if earliest_time:
            alarm_time = earliest_time - timedelta(hours=2)
            return alarm_time.strftime("%H:%M")
        return None

    finally:
        driver.quit()
