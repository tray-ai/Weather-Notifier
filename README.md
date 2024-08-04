# Weather-Notifier
WeatherNotifier
weather.py:

This is a Python script that retrieves and displays weather information for Biloxi, MS, USA using the OpenWeatherMap API. It fetches current weather data, processes the information, and sends notifications via the Pushover app twice a day.

Features:
- Retrieves weather data from OpenWeatherMap API.
- Handles various types of request errors.
- Parses API responses and formats weather information.
- Sends notifications with weather details using the send_notification_message function.
- Schedules notifications at 11 AM and 6 PM CST using the schedule library.

Usage:

- Set up your .env file with the necessary API key.
- Ensure all dependencies are installed.
- Run the script to start receiving weather notifications for Biloxi, MS.
- This program is designed to retrieve weather information for a specified city. By default, it uses static parameters for the city, state, country, and API key. However, you can easily modify these parameters to suit your needs. 

Dependencies:
- os
- time
- requests
- schedule
- dotenv
- Custom module: email_mod

email_mod.py:

This module facilitates sending notifications to your phone via the Pushover app. It utilizes SMTP to send email or text messages at scheduled times, as defined in the weather.py program. The module securely connects to a Gmail SMTP server, authenticates using credentials from environment variables, and delivers notifications to the address specified in the .env file.

.env.example:

This file serves as a template for configuring environment variables required by the project. It includes placeholders for:

- API_KEY: Your OpenWeather API key for accessing weather data.
- EMAIL: Your Gmail address used for sending notifications.
- PASSWORD: The password for the Gmail account.
- PUSHOVER_EMAIL: The email address for Pushover notifications.

Note: This is an example file. Rename it to .env and replace the placeholder values with your actual credentials to use the project.
 
