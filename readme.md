# Flight Alarm System

Flight Alarm is a tailored solution specifically designed for professionals working inside airports. By providing real-time updates on flight schedules and notifications, this project ensures that airport staff can efficiently manage their tasks and responsibilities. It is built to address the unique requirements of individuals whose occupation demands precise and timely flight information.

---

## Features

- **Real-Time Flight Data**: Dynamically scrapes flight schedules and arrival times from `flightstats.com`.
- **Customizable Notifications**: Automatically schedules alarms 2 hours before the earliest flight.
- **Exclusion Rules**: Filters out domestic flights and flights with "Cargo" in the airline name.
- **User-Friendly GUI**: Allows users to select "Today" or "Next Day" flights via an intuitive interface.
- **Cross-Platform Notifications**: Uses desktop notifications to alert users of scheduled alarms.

---

## Installation

### Prerequisites
1. Install **Python 3.8+** from [python.org](https://www.python.org/).
2. Install **Google Chrome** and ensure the version matches the ChromeDriver version.
3. Download the appropriate **ChromeDriver** binary from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Flight_Alarm.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Flight_Alarm
    ```
3. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. Run the application:
    ```bash
    python main.py
    ```
2. Follow the GUI prompts to select "Today" or "Next Day" flights.
3. The application will scrape flight data, display the results in the terminal, and schedule an alarm for the earliest flight.

### Example Output
```plaintext
Scraping flights for CRK at: https://www.flightstats.com/v2/flight-tracker/arrivals/CRK/?year=2025&month=5&date=6&hour=6

International Flight Arrivals at CRK:

Origin Airport       | City           | Time       | Airline        
-----------------------------------------------------------------
HKG                  | Hong Kong      | 08:30      | Cathay Pacific 
SIN                  | Singapore      | 09:15      | Singapore Air  
TPE                  | Taipei         | 07:45      | Cargo Express  
NRT                  | Tokyo          | 06:50      | Japan Airlines 
```

In this example, the earliest flight is from Tokyo (NRT) at 06:50. An alarm will be scheduled for 04:50.

---

## Project Structure

```
Flight_Alarm/
│
├── alarm_scheduler.py       # Handles alarm scheduling
├── date_selector.py         # GUI for selecting dates
├── flight_scraper.py        # Scrapes flight data and calculates alarm time
├── main.py                  # Entry point for the application
├── chromedriver.exe         # ChromeDriver binary (required for Selenium)
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation
```

---

## Contributing

We welcome contributions that enhance the functionality of Flight Alarm for airport professionals. To contribute:

1. Fork the repository.
2. Create a branch for your feature:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request for review.

---

## Future Enhancements

- Add support for multiple browsers (e.g., Firefox, Edge).
- Implement logging for better debugging and monitoring.
- Add filters for flights based on airline, arrival time, or origin airport.
- Support internationalization for multiple languages.
- Improve the GUI with additional features like flight filtering.

---

## Acknowledgments

- [Selenium](https://www.selenium.dev/) for browser automation.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing.
- [FlightStats](https://www.flightstats.com/) for flight data.
