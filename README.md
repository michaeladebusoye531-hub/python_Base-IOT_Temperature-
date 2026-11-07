# IoT Temperature Monitoring System

## LENS-COS 324 – Internet of Things (IoT) Practical Assignment

### Project Overview

The IoT Temperature Monitoring System is a Python-based project that simulates an Internet of Things (IoT) temperature sensor. It generates temperature readings, stores them in a CSV file, calculates the average temperature, detects missing or invalid data, and displays a warning when the temperature exceeds 35°C.

## Features

- Generates 60 simulated temperature readings.
- Saves readings into a CSV file.
- Reads temperature data from the CSV file.
- Calculates average temperature.
- Detects missing and invalid data.
- Displays warnings when temperature exceeds 35°C.
- Creates a temperature graph using Matplotlib.
- Saves the graph as a PNG image.

## Technologies Used

- Python 3
- CSV
- Random Module
- Matplotlib

## Project Structure

```text
IoT_Temperature_Monitoring/
│
├── main.py
├── temperature_data.csv
├── temperature_graph.png
└── README.md
```

## Installation and Setup

### 1. Install Python

Download Python from https://www.python.org/downloads/

### 2. Install Matplotlib

```bash
pip install matplotlib
```

### 3. Run the Program

```bash
python main.py
```

## How the System Works

1. Generates 60 random temperature readings between 20°C and 45°C.
2. Saves the readings in `temperature_data.csv`.
3. Reads the CSV file using Python.
4. Identifies missing and invalid readings.
5. Calculates the average temperature using valid readings.
6. Displays a warning when temperature exceeds 35°C.
7. Creates and saves a temperature graph.

## Relationship with Real-World IoT

In a real IoT temperature monitoring system, a physical temperature sensor collects readings from its environment and sends the information to a computer for processing.

This project simulates the same process using Python-generated temperature readings instead of physical sensor devices.

## Conclusion

This project demonstrates how Python can be used to simulate an IoT temperature monitoring system. It shows how data can be generated, stored, analyzed and visualized while handling missing and invalid readings.

## Student Information

Name: Adebusoye Gloria Gift

Matric Number: 252007CSC001

Course Code: LENS-COS 324

Course Title: Internet of Things (IoT)

Assignment: Python-Based IoT Temperature Monitoring System
