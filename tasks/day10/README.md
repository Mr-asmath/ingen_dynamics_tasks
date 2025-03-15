# Sales Data Visualization

## Overview
This Python script reads sales data from a CSV file and visualizes sales growth over the years using a line chart. It helps analyze trends and patterns in sales performance.

## Features
- Reads sales data from a CSV file.
- Generates a line chart for sales growth over the years.
- Adds markers, labels, a legend, and a grid for better visualization.

## Requirements
- Python 3.x
- Required libraries: `pandas`, `matplotlib`

## Installation
1. Install the required dependencies if not already installed:
   ```sh
   pip install pandas matplotlib
   ```
2. Ensure the `sales_data.csv` file is in the same directory as the script.

## Usage
1. Save the script as `sales_chart.py`.
2. Run the script:
   ```sh
   python sales_chart.py
   ```
3. A line chart will be displayed showing sales trends over the years.

## Expected CSV Format (`sales_data.csv`)
```
Year,Sales
2020,10000
2021,15000
2022,20000
2023,25000
```

## Output
- A line chart visualizing sales trends over the years.

## Future Enhancements
- Add bar charts for yearly comparisons.
- Include interactive visualizations using Plotly.
- Support multiple product categories.

