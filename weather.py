# Name: Tyler Vasquez
# Date: 10/11/2026
# Provides functions for storing and reporting weather data.

import json
import calendar
from datetime import datetime


def read_data(*, filename):
    """Read weather data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def write_data(*, data, filename):
    """Write weather data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def max_temperature(*, data, date):
    """Return the maximum temperature for a given date."""
    values = [
        readings["t"]
        for timestamp, readings in data.items()
        if timestamp.startswith(date)
    ]
    return max(values) if values else None


def min_temperature(*, data, date):
    """Return the minimum temperature for a given date."""
    values = [
        readings["t"]
        for timestamp, readings in data.items()
        if timestamp.startswith(date)
    ]
    return min(values) if values else None


def max_humidity(*, data, date):
    """Return the maximum humidity for a given date."""
    values = [
        readings["h"]
        for timestamp, readings in data.items()
        if timestamp.startswith(date)
    ]
    return max(values) if values else None


def min_humidity(*, data, date):
    """Return the minimum humidity for a given date."""
    values = [
        readings["h"]
        for timestamp, readings in data.items()
        if timestamp.startswith(date)
    ]
    return min(values) if values else None


def tot_rain(*, data, date):
    """Return the total rainfall for a given date."""
    return sum(
        readings["r"]
        for timestamp, readings in data.items()
        if timestamp.startswith(date)
    )


def report_daily(*, data, date):
    """Return a formatted daily weather report."""
    lines = [
        "========================= DAILY REPORT ========================",
        "Date Time Temperature Humidity Rainfall",
        "==================== ======== =========== ======== ========",
    ]

    matching = sorted(
        (timestamp, readings)
        for timestamp, readings in data.items()
        if timestamp.startswith(date)
    )

    for timestamp, readings in matching:
        recorded = datetime.strptime(timestamp, "%Y%m%d%H%M%S")
        formatted_date = (
            f"{calendar.month_name[recorded.month]} "
            f"{recorded.day}, {recorded.year}"
        )
        formatted_time = recorded.strftime("%H:%M:%S")

        lines.append(
            f"{formatted_date} {formatted_time} "
            f"{readings['t']} {readings['h']} {readings['r']:.2f}"
        )

    return "\n".join(lines)


def report_historical(*, data):
    """Return a formatted historical weather report."""
    lines = [
        "============================== HISTORICAL REPORT ===========================",
        " Minimum Maximum Minumum Maximum Total",
        "Date Temperature Temperature Humidity Humidity Rainfall",
        "==================== =========== =========== ======== ======== ========",
    ]

    dates = sorted({timestamp[:8] for timestamp in data})

    for date in dates:
        date_readings = [
            readings
            for timestamp, readings in data.items()
            if timestamp.startswith(date)
        ]

        if not date_readings:
            continue

        recorded = datetime.strptime(date, "%Y%m%d")
        formatted_date = (
            f"{calendar.month_name[recorded.month]} "
            f"{recorded.day}, {recorded.year}"
        )

        temperatures = [reading["t"] for reading in date_readings]
        humidities = [reading["h"] for reading in date_readings]
        rainfall = sum(reading["r"] for reading in date_readings)

        lines.append(
            f"{formatted_date} "
            f"{min(temperatures)} {max(temperatures)} "
            f"{min(humidities)} {max(humidities)} {rainfall:.2f}"
        )

    return "\n".join(lines)
