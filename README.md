# Dicoding Project: Bicycle Rental Count

## Project Overview

Submission for Dicoding "Learn Data Analysis with Python" course. This dashboard provides an interactive way to explore bicycle rental counts by considering variables such as weather, season, time, and bicycle types

## Data Source
This dataset contains the hourly and daily count of rental bikes between the years 2011 and 2012 in the Capital bike share system with the corresponding weather and seasonal information.

## Modules Used
-  pandas
-  streamlit
-  plotly

## How to Run the Dashboard
1. **Create and Activate a Python Environment**:
   - If using Conda (ensure [Conda](https://docs.conda.io/en/latest/) is installed):
     ```
     conda create --name main-ds python=3.9
     conda activate main-ds
     ```
   - If using venv (standard Python environment tool):
     ```
     python -m venv main-ds
     source airquality-ds/bin/activate  # On Windows use `main-ds\Scripts\activate`
     ```
   - If using Shell/Terminal:
     ```
      mkdir bicycle_rental_count
      cd bicycle_rental_count
      pipenv install
      pipenv shell
      pip install -r requirements.txt
     ```

2. **Install Required Packages**:
   - The following packages are necessary for running the analysis and the dashboard:
     ```
     pip install pandas streamlit plotly
     ```
     or you can do
     ```
     pip install -r requirements.txt
     ```
### Run the Streamlit App
