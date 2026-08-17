Project Overview
This project collects real-time weather data from selected Nigerian cities using the OpenWeatherMap API. The data is extracted, transformed, and loaded into a structured dataset for analysis.
Tools Used
Python
Pandas
Requests
OpenWeatherMap API
Jupyter Notebook
ETL Process
Extract
Weather data was collected from:
Lagos
Abuja
Enugu
Transform
Converted JSON response into a DataFrame
Corrected column names
Standardized formatting
Converted timestamps
Load
Processed data was exported to CSV and Excel formats.
Key Findings
Lagos temperature: 28.76°C
Abuja temperature: 28.00°C
Enugu temperature: 27.03°C
Enugu recorded the highest humidity.
Lagos and Abuja experienced overcast clouds.
Enugu experienced moderate rainfall.
Author
Nnamani Faithful
Real-Time Weather Data ETL Pipeline Using Python and OpenWeatherMap API

Project Overview

This project demonstrates the ETL (Extract, Transform, Load) process using real-time weather data from the OpenWeatherMap API. Weather information was collected for selected Nigerian cities, cleaned, transformed into a structured format, and analyzed using Python and Pandas.

Objectives

- Extract real-time weather data from the OpenWeatherMap API.
- Transform and clean the dataset for analysis.
- Load the processed data into CSV and Excel formats.
- Perform basic weather analysis across selected cities.

Tools Used

- Python
- Pandas
- Requests
- OpenWeatherMap API
- Jupyter Notebook
- Excel

Data Source

OpenWeatherMap API

ETL Process

Extract

Weather data was retrieved from the OpenWeatherMap API for the following cities:

- Lagos
- Abuja
- Enugu

The following fields were extracted:

- City
- Temperature (°C)
- Humidity (%)
- Weather Condition
- Wind Speed (m/s)
- Date and Time

Transform

The extracted data was cleaned and transformed by:

- Organizing the data into a Pandas DataFrame.
- Correcting column names and formatting.
- Converting timestamps into a readable date and time format.
- Checking for missing values.
- Checking for duplicate records.

Load

The cleaned dataset was saved as:

- CSV File ("weather_data.csv")
- Excel File ("weather_data.xlsx")

Analysis and Findings

Weather data collected on 18 August 2026 showed the following results:

City| Temperature (°C)| Humidity (%)| Weather Condition
Lagos| 28.76| 68| Overcast Clouds
Abuja| 28.00| 65| Overcast Clouds
Enugu| 27.03| 81| Moderate Rain

Key Findings

- Lagos recorded the highest temperature at 28.76°C.
- Enugu recorded the highest humidity at 81%.
- Lagos and Abuja experienced overcast clouds, indicating skies that were largely covered by clouds.
- Enugu experienced moderate rain, which contributed to its higher humidity level.

Project Files

- Weather_ETL_Project.ipynb
- etl_pipeline.py
- weather_data.csv
- weather_data.xlsx
- README.md

Conclusion

This project demonstrates how Python can be used to automate the extraction, transformation, and loading of real-time weather data from an API. The ETL pipeline successfully collected weather information, prepared it for analysis, and generated insights into temperature, humidity, and weather conditions across selected Nigerian cities.

Author

Nnamani Faithful
