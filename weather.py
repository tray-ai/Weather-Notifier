"""This script retrieves and displays weather 
information for Biloxi, MS, USA using the OpenWeatherMap API."""

import os
import time
import requests
import schedule
from dotenv import load_dotenv
from email_mod import send_notification_message

def main():
    """Main function of the program which makes an API request,
    and gather weather data from OpenWeather API."""

    # Load environmental variables for API key.
    load_dotenv()
    apikey = os.getenv('API_KEY')

    try:
        weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q'
                            f'=Biloxi,MS,US&units=imperial&appid={apikey}',
                            timeout=10)
    except requests.exceptions.ConnectionError as error:
        print(error)
    except requests.exceptions.HTTPError as error:
        print(error)
    except requests.exceptions.Timeout as error:
        print(error)
    except requests.exceptions.TooManyRedirects as error:
        print(error)

    # Parse the API response into a python object.
    weather_data = weather.json()

    # Compose a string for weather data to be sent as pushover notification.
    w_data = f'\nCity: {weather_data['name']}\n'

    # Iterate through the list to collect weather descriptions.
    for weather in weather_data['weather']:
        # Append them to the 'w_data' string.
        w_data += f'Sky: {weather['main']}\n'
        w_data += f'Description: {weather['description'].title()}\n'

    # Iterate through the dictionary to collect temperature information.
    for type_temp, temp in weather_data['main'].items():
        # Append it to the 'w_data' string.
        if type_temp in ['temp','temp_min', 'temp_max']:
            w_data += f'{type_temp}: {temp}\n'

    # Call the function to send a notification to the Pushover app.
    send_notification_message(w_data)

# Schedule this program to run twice a day at 11AM and 6PM CST.
schedule.every().day.at('11:00').do(main)
schedule.every().day.at('18:00').do(main)

def schedule_program():
    """Function runs any pending scheduled tasks and
    waits 60 seconds each time to save resources."""

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    schedule_program()
