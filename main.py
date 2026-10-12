
# Name: Tyler Vasquez
# Date: 10/11/2026
# Runs the Tuffy Titan Weather Logger program.

import weather


def main():
    """Run the Tuffy Titan Weather Logger menu."""
    filename = "weather.json"
    data = weather.read_data(filename=filename)

    while True:
        print(" *** TUFFY TITAN WEATHER LOGGER MAIN MENU")
        print("1. Set data filename")
        print("2. Add weather data")
        print("3. Print daily report")
        print("4. Print historical report")
        print("9. Exit the program")

        choice = input("Enter menu choice: ")

        if choice == "1":
            filename = input("Enter data filename: ")
            data = weather.read_data(filename=filename)

        elif choice == "2":
            date = input("Enter date (YYYYMMDD): ")
            time = input("Enter time (hhmmss): ")

            try:
                datetime_key = date + time
                from datetime import datetime
                datetime.strptime(datetime_key, "%Y%m%d%H%M%S")

                temperature = int(input("Enter temperature: "))
                humidity = int(input("Enter humidity: "))
                rainfall = float(input("Enter rainfall: "))

                data[datetime_key] = {
                    "t": temperature,
                    "h": humidity,
                    "r": rainfall,
                }

                weather.write_data(data=data, filename=filename)

            except ValueError:
                print("Invalid date, time, temperature, humidity, or rainfall.")

        elif choice == "3":
            date = input("Enter date (YYYYMMDD): ")

            try:
                datetime.strptime(date, "%Y%m%d")
                print(weather.report_daily(data=data, date=date))
            except ValueError:
                print("Invalid date. Please use YYYYMMDD.")

        elif choice == "4":
            print(weather.report_historical(data=data))

        elif choice == "9":
            break

        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()
