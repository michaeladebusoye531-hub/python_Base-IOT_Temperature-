
import random
import csv
import matplotlib.pyplot as plt

# IoT Temperature Monitoring System

print("========================================")
print("   IoT TEMPERATURE MONITORING SYSTEM")
print("========================================")

# Step 1: Generate 60 simulated temperature readings

temperatures = []

for i in range(60):
    temperature = round(random.uniform(20, 45), 2)
    temperatures.append(temperature)

# Add some missing and invalid data for testing
temperatures[5] = None
temperatures[15] = "invalid"
temperatures[25] = ""

print("\nTemperature readings generated successfully!")

# Step 2: Save readings into a CSV file

with open("temperature_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Reading Number", "Temperature"])

    for i, temp in enumerate(temperatures, start=1):
        writer.writerow([i, temp])

print("Temperature data saved to CSV file.")

# Step 3: Read the CSV file and check the data

valid_temperatures = []

print("\nReading temperature data from CSV...")
print("----------------------------------------")

with open("temperature_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        reading_number = row["Reading Number"]
        value = row["Temperature"]

        try:
            if value == "":
                print(f"Reading {reading_number}: Missing data")
                continue

            temperature = float(value)

            if temperature < 0 or temperature > 100:
                print(f"Reading {reading_number}: Invalid temperature")
                continue

            valid_temperatures.append(temperature)

            print(f"Reading {reading_number}: {temperature}°C")

            # Step 4: Temperature warning
            if temperature > 35:
                print("WARNING! Temperature is above 35°C!")

        except ValueError:
            print(f"Reading {reading_number}: Invalid data detected")

# Step 5: Calculate average temperature

if len(valid_temperatures) > 0:
    average = sum(valid_temperatures) / len(valid_temperatures)

    print("\n----------------------------------------")
    print("TEMPERATURE SUMMARY")
    print("----------------------------------------")

    print("Total readings:", 60)
    print("Valid readings:", len(valid_temperatures))
    print("Invalid or missing readings:",
          60 - len(valid_temperatures))

    print(f"Average Temperature: {average:.2f}°C")

else:
    print("No valid temperature readings available.")

# Step 6: Create temperature graph

reading_numbers = list(range(1, len(temperatures) + 1))

# Convert valid readings to numbers for plotting.
# Missing and invalid values will appear as gaps.
plot_temperatures = []

for temp in temperatures:
    try:
        if temp == "" or temp is None:
            plot_temperatures.append(None)
        else:
            plot_temperatures.append(float(temp))
    except ValueError:
        plot_temperatures.append(None)

plt.figure(figsize=(12, 6))

plt.plot(
    reading_numbers,
    plot_temperatures,
    marker="o",
    label="Temperature"
)

plt.axhline(
    y=35,
    linestyle="--",
    label="Warning Limit (35°C)"
)

plt.title("IoT Temperature Monitoring Graph")
plt.xlabel("Reading Number")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

plt.savefig("temperature_graph.png")

plt.show()

print("\nTemperature graph saved successfully!")
print("CSV file saved successfully!")
print("\nIoT Temperature Monitoring System completed.")
