# Fastest-Coder-Hackathon

## Introduction

This repositorty contains solutions code generated for Fastest Code Hackathon.

![](images/solution_architecture.png)

This is a weather report application that was created for the `Fastest Coder Hackathon`. It uses the `Open Weather API` to get the weather report for a given city name. The application takes the city name as an argument. The city name should be passed as `--city <city name>`. The application will print the weather report for the given city name. If the city name is not passed, then the application will print the help message. If the city name is unknown, then the application will show `None`. The application uses the `geopy library` to get the latitude and longitude of the given city name. The application uses the `dotenv library` to load the environment variables. The application uses the `requests library` to make the API call. The application uses the `argparse library` to parse the arguments. The application uses the `json library` to parse the json data. The application uses the `os library` to get the environment variables. The test cases are implemented using unittest module. 

Here is a demo:

[![Alternate Text](images/fastestcoderhackathon_demo.gif)](images/fastestcoderhackathon_demo.mp4 "Link Title")


## The Github Copilot

The Github Copilot is extensively used in the development of this program. The copilot is good in recommending the statements but yet we need to be wise in choosing recommended options and further modify the code generated by copilot to suit our requirements. 

Much of this documentation statements are generated using CoPilot.

## The Open Weather API

This program uses `openweathermap` service that provides weather data, including current weather data, forecasts, and historical data to the developers of web services and mobile applications. An API key can be obtained by signing up here: `https://openweathermap.org/price`. 

This project uses the `Free` plan that provides access to 5 day forecast for any location on the globe. It includes weather forecast data with 3-hour step. Forecast is available in JSON or XML format.

The `Call 5 day / 3 hour forecast data` API call template is in this format: `api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}`

This progrom requires storing the `API key` in runtime environment variable named `OPEN_WEATHER_API_KEY`. If you are using this program on your development machine then create a `.env file` and specify `OPEN_WEATHER_API_KEY=<your_api_key>`.

## How to run this program?

First, ensure you have set the OPEN_WEATHER_API_KEY in your environment variable. In case if this is not configured then program will show `Open Weather API key is not present` exception.

Then, on your development machine run: `python WeatherReport.py`. This will show you the command-line argument help. 

```
usage: WeatherReport.py [-h] [--city CITY] [--version] [--format]

This is a weather report application that was created for the Fastest Coder Hackathon. It uses the Open Weather API to get the weather report for a given city name. The application takes the city name as an argument. If the city name is unknown, then the application will show None.

options:
  -h, --help   show this help message and exit
  --city CITY  City name for which you want to get the weather report
  --version    show program's version number and exit
  --format     Format the output in a formatted text

Example of usage: python WeatherReport.py --city "New York" --format
```

## How to run unit tests?

First, ensure you have set the OPEN_WEATHER_API_KEY in your environment variable. In case if this is not configured then program will show `Open Weather API key is not present` exception.

Then, on your development machine run: `python TestWeatherReport.py`. This will execute all the unit test cases and show test results. 