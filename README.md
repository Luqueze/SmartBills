# SmartBills

## Overview
SmartBills reads a CSV file, processes its data, and presents the results in a table. It groups entries by `title`, sums up the `amount` values, and organizes results in descending order.
This is a personal project developed to help me organize my finances more efficiently.

## Features
- Reads data from a CSV file (`example.csv`).
- Groups by `title` while summing up `amount` values.
- Keeps the first `date` occurrence for each title.
- Sorts records in descending order by total amount.
- Shows the results in a table.

## Requirements
Ensure you have:
- Python 3.x installed.
- Pandas library (`pip install pandas`).
- Streamlit library (`pip install streamlit`)

## Installation
Clone this repository and navigate to the project directory:

```sh
git clone https://github.com/yourusername/repository-name.git
cd repository-name
