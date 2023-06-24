# import the libraries
import requests, json
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import os
import argparse

"""
This is a weather report application that was created for the Fastest Coder Hackathon. 
This application uses the Open Weather API to get the weather report for a given city name.
The application takes the city name as an argument.
If the city name is unknown, then the application will show None.
Please ensure that you have configured the Open Weather API key in the environment variable before running this application.
"""

# create a class for weather report
class WeatherReport:

    # initialize the class
    def __init__(self):
        # load the environment variables
        load_dotenv()

        # get the api key from the environment variables
        api_key = os.getenv("OPEN_WEATHER_API_KEY")

        # verify whether api key is present
        if not api_key or api_key.isspace():
            # raise exception
            raise Exception("Open Weather API key is not present")
        else:
            # assign api key to the class variable
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
            else:
                # raise exception that api key is not valid
                raise Exception("Open Weather API key is not valid")

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

    # function to create the formatted report
    def create_formatted_report(self, city_name):

        # get the weather report for the given city name
        report = self.create_report(city_name)

        # check whether report is none
        if report is None:
            # print none
            return None
        else:

            # Initialize a string to store the formatted report
            formatted_report = ""

            # append the city name to the formatted report
            formatted_report += "Weather report for city: {0}\n\n".format(city_name)

            # iterate through the report
            for data in report:
                # iterate through the weather data
                for weather_data in data:
                    # append the formatted weather_data to the formatted report
                    formatted_report += "Date Time: {0}\nTemperature: {1}\nPressure: {2}\nHumidity: {3}\nTemp Min: {4}\nTemp Max: {5}\nDescription: {6}\nSpeed: {7}\nDirection: {8}\nClouds: {9}\nVisibility: {10}\nPop: {11}\n\n".format(
                        weather_data["date_time"],
                        weather_data["temperature"],
                        weather_data["pressure"],
                        weather_data["humidity"],
                        weather_data["temp_min"],
                        weather_data["temp_max"],
                        weather_data["description"],
                        weather_data["speed"],
                        weather_data["direction"],
                        weather_data["clouds"],
                        weather_data["visibility"],
                        weather_data["pop"]
                    )
            # return the formatted report
            return formatted_report

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
    
    python WeatherReport.py --city \"New York\" --format
    """

    try:
        # create an instance of the argument parser
        parser = argparse.ArgumentParser(
            description=about_application,
            epilog=example_of_use)

        # add the argument for city name
        parser.add_argument("--city", help="City name for which you want to get the weather report")

        # add the argument for version
        parser.add_argument("--version", action="version", version="%(prog)s 1.0")

        # add the argument for formatted text output
        parser.add_argument("--format", help="Format the output in a formatted text", action="store_true")

        # parse the arguments
        args = parser.parse_args()

        # check whether city argument is passed
        if not args.city or args.city.isspace():
            # print help message
            parser.print_help()
        else:

            # get the city name from the arguments
            city_name = args.city
            
            # create an instance of the weather report
            weather_report = WeatherReport()

            # check the format argument
            if args.format:    
                # get the weather data for the given city name
                report = weather_report.create_formatted_report(city_name)

                # print the weather report as json string
                print(report)
            else:
                # get the weather data for the given city name
                report = weather_report.create_report(city_name)

                # print the weather report as formatted text
                print(report)

    except Exception as ex:
        # print the exception
        print(ex)

if __name__ == "__main__":
    # call the main function
    main()

