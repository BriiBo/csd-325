# Brian Palm
# Module 4.2 Assignment
# High/Low Temperatures
# Modified to allow the user to view high or low temperatures or exit the program.

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
        
# Display menu until the user chooses to exit.
while True:
    print("\nTemperature Menu")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        # Plot the high temperatures in red.
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c="red")

        # Format the high-temperature graph.
        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel("", fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis="both", which="major", labelsize=16)
        plt.show()
    elif choice == "2":
        # Plot the low temperatures in blue.
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c="blue")

        # Format the low-temperature graph.
        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel("", fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis="both", which="major", labelsize=16)
        plt.show()    
    elif choice == "3":
        print("Thank you for using the temperature program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")