# import the libraries
import requests, json
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import os
import argparse

# create a class for weather report
class WeatherReport:

    # initialize the class
    def __init__(self, api_key):
        # assign the api key
        self.api_key = api_key

        # base_url variable to store url
        self.base_url = "https://api.openweathermap.org/data/2.5/forecast?"

    # function to return longitude and latitude of a given city name
    def get_lat_lon(self, city_name):
        # Initialize Nominatim API
        geolocator = Nominatim(user_agent="MyApp")

        # Assign latitude and longitude to location
        location = geolocator.geocode(city_name)

        # check whether location is not none
        if location is not None:
            # return latitude and longitude of the given city name
            return location.latitude, location.longitude
        else:
            # return none for latitude and longitude
            return None, None
    
    # function to return the weather report for a given city name
    def create_report(self, city_name):

        # initialize empty list for weather report
        waether_report = []

        # get the latitude and longitude of the given city name
        lat, lon = self.get_lat_lon(city_name)

        # check whether latitude and longitude is none
        if lat is None or lon is None:
            return None
        else:
            # complete_url variable to store
            # complete url address
            complete_url = self.base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + self.api_key

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
                weather_data = self.parse_weather_list(response_json)

                # append the weather data to the weather report
                waether_report.append(weather_data)
            
            # return the weather report
            return waether_report

    # function to parse the weather json data
    def parse_weather_list(self, weather_list):

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

    about_application = """
    This is a weather report application that was created for the Fastest Coder Hackathon. 
    It uses the Open Weather API to get the weather report for a given city name. 
    The application takes the city name as an argument. 
    If the city name is unknown, then the application will show None. 
    """
    example_of_use = """
    Example of usage: 
    
    python WeatherReport.py --city \"New York\"
    """

    try:
        # create an instance of the argument parser
        parser = argparse.ArgumentParser(
            description=about_application,
            epilog=example_of_use)

        # add the argument for city name
        parser.add_argument("--city", help="City name for which you want to get the weather report")

        # parse the arguments
        args = parser.parse_args()

        # check whether city argument is passed
        if not args.city or args.city.isspace():
            # print help message
            parser.print_help()
        else:

            # get the city name from the arguments
            city_name = args.city
            
            # load the environment variables
            load_dotenv()

            # get the api key from the environment variables
            api_key = os.getenv("OPEN_WEATHER_API_KEY")

            # create an instance of the weather report
            weather_report = WeatherReport(api_key)

            # get the weather data for the given city name
            report = weather_report.create_report(city_name)

            # print the weather report
            print(report)

    except Exception as ex:
        # print the exception
        print(ex)

if __name__ == "__main__":
    # call the main function
    main()

