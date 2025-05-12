# SmartBills

## Overview
SmartBills reads a CSV file, processes its data, and presents the results in a table. It groups entries by `title`, sums up the `amount` values, and organizes results in descending order.
This is a personal project developed to help me organize my finances more efficiently.

## Features
- Reads data from a CSV file (example.csv).
- Groups transactions by title while summing up amount values.
- Keeps the first date occurrence for each title.
- Sorts records in descending order by total amount.
- Dynamically categorizes transactions using OpenAI's API.
- Displays results in a table with categorized expenses.
- Generates different types of charts, including bar charts and pie charts, to visualize financial trends


## Requirements
Ensure you have:
- Python 3.x installed.
- Pandas (`pip install pandas`)
- Streamlit (`pip install streamlit`)
- OpenAI (`pip install openai`)
- Dotenv (`pip install python-dotenv`)
- Plotly (`pip install plotly`)


## Installation
Clone this repository and navigate to the project directory:

```sh
git clone https://github.com/Luqueze/SmartBills.git
cd SmartBills
