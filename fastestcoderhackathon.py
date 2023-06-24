# import the libraries
import requests, json
from geopy.geocoders import Nominatim
import datetime

# API key
api_key = "TODO"

# base_url variable to store url
base_url = "https://api.openweathermap.org/data/2.5/forecast?"

# function to return longitude and latitude of a given city name
def get_lat_lon(city_name):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="MyApp")

    # Assign latitude and longitude to location
    location = geolocator.geocode(city_name)

    # return latitude and longitude of the given city name
    return location.latitude, location.longitude

# function to return the weather data for a given city name
def get_weather_data(city_name):

    # initialize empty list for weather report
    waether_report = []

    # get the latitude and longitude of the given city name
    lat, lon = get_lat_lon(city_name)

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object convert
    # json format data 
    response_json = response.json()

     # now response_json contains list
    # of nested dictionaries
    # check the value of "cod" key is equal to
    # "200", means city is found otherwise, 
    # city is not found
    if response_json["cod"] == "200":
        # obtain the weather data
        weather_data = parse_weather_list(response_json)

        # append the weather data to the weather report
        waether_report.append(weather_data)
    
    # return the weather report
    return waether_report

# function to parse the weather json data
def parse_weather_list(weather_list):

    # initialize empty list for weather data
    weather_data = []

    # check whether list is present in the weather list
    if "list" in weather_list:
        # iterate through list
        # of nested dictionaries
        for list_item in weather_list["list"]:
            # obtain date from list item
            date_time = list_item["dt_txt"]  
            
            # initialize none for temperature, pressure, humidity, temp_min, temp_max
            temperature = None
            pressure = None
            humidity = None
            temp_min = None
            temp_max = None

            # check whether main object is present in the list item
            if "main" in list_item:
                # obtain values for temperature, pressure, humidity, temp_min, temp_max
                temperature = list_item["main"]["temp"]
                pressure = list_item["main"]["pressure"]
                humidity = list_item["main"]["humidity"]
                temp_min = list_item["main"]["temp_min"]
                temp_max = list_item["main"]["temp_max"]


            # initialize none for description
            description = None

            # check whether weather object is present in the list item 
            if "weather" in list_item:
                # obtain description
                description = list_item["weather"][0]["description"]
            
            # initialize none for speed and direction
            speed = None
            direction = None

            # check whether wind object is present in the list item
            if "wind" in list_item:
                # obtain wind speed and direction
                speed = list_item["wind"]["speed"]
                direction = list_item["wind"]["deg"]

            # initialize none for clouds
            clouds = None

            # check whether clouds object is present in the list item
            if "clouds" in list_item:
                # obtain clouds
                clouds = list_item["clouds"]["all"]

            # obtain visibility if present
            visibility = list_item["visibility"] if list_item["visibility"] in list_item else None

            # obtain pop if present
            pop = list_item["pop"] if list_item["pop"] in list_item else None

            # append the data to the warther data list
            weather_data.append({
                "date_time": date_time,
                "temperature": temperature,
                "pressure": pressure,
                "humidity": humidity,
                "temp_min": temp_min,
                "temp_max": temp_max,
                "description": description,
                "speed": speed,
                "direction": direction,
                "clouds": clouds,
                "visibility": visibility,
                "pop": pop
            })

    # return the weather data
    return weather_data

# main function
def main():
    # print the welcome message
    print("Welcome to the weather report")

    # get the weather data for a given city name
    weather_data = get_weather_data("London")
    print(weather_data)


if __name__ == "__main__":
    main()