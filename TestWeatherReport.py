import unittest
from WeatherReport import WeatherReport

# unit test class for WeatherReport
class TestWeatherReport(unittest.TestCase):

    # test warther report class initialization
    def test_weather_report_class_initialization(self):
        # initialize weather report class
        weather_report = WeatherReport()

        # check whether weather report class is initialized
        self.assertTrue(weather_report)

    # test get latitude and longitude method with invalid city name
    def test_get_lat_lon_with_invalid_city_name(self):
        # initialize weather report class
        weather_report = WeatherReport()

        # get latitude and longitude of the given city name
        lat, lon = weather_report.get_lat_lon("invalid_city_name")

        # check whether latitude and longitude is none
        self.assertIsNone(lat)
        self.assertIsNone(lon)

    # test get latitude and longitude method with valid city name
    def test_get_lat_lon_with_valid_city_name(self):
        # initialize weather report class
        weather_report = WeatherReport()

        # get latitude and longitude of the given city name
        lat, lon = weather_report.get_lat_lon("London")

        # check whether latitude and longitude is none
        self.assertIsNotNone(lat)
        self.assertIsNotNone(lon)

    # test create report method with invalid city name
    def test_create_report_with_invalid_city_name(self):
        # initialize weather report class
        weather_report = WeatherReport()

        # get weather report for the given city name
        weather_report = weather_report.create_report("invalid_city_name")

        # check whether weather report is none
        self.assertIsNone(weather_report)

    # test create report method with valid city name
    def test_create_report_with_valid_city_name(self):
        # initialize weather report class
        weather_report = WeatherReport()

        # get weather report for the given city name
        weather_report = weather_report.create_report("London")

        # check whether weather report is none
        self.assertIsNotNone(weather_report)

# main block
if __name__ == "__main__":
    unittest.main()
