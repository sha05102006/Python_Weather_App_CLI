# Intern Details:
* Intern ID: CITS1691
* Full Name: Shashath.B.S
* No.Of Weeks: 4 Weeks

## Introduction:

The scope of this project is to provide users with real-time weather information through a simple *Command Line Interface (CLI)* application. This project is developed using *Python* and integrates with the *OpenWeatherMap API* to retrieve current weather information for any specified city or country. The application accepts the location as a command-line argument, sends a request to the weather API, processes the received JSON data, and displays the weather details in a clean and user-friendly format with colored output and weather icons.

The Python script attached in this repository can perform functions such as:

* Accepting a city or country name through the command line.
* Fetching real-time weather information using the OpenWeatherMap API.
* Displaying the current temperature in Celsius.
* Displaying the "Feels Like" temperature.
* Displaying the current weather condition.
* Displaying weather icons based on the weather condition.
* Printing the city name in large ASCII art using PyFiglet.
* Displaying colored terminal output for improved readability.
* Handling invalid API requests by displaying an appropriate error message.

This project provides users with a quick and convenient way to check weather conditions directly from the terminal without the need for a graphical interface.

## Features:

### Weather Information

* Search weather using a city or country name.
* Display current weather description.
* Display current temperature in Celsius.
* Display "Feels Like" temperature.
* Display weather icons corresponding to current weather conditions.

### Command Line Interface

* Accept user input using command-line arguments.
* Generate clean and readable terminal output.
* Display the city name as ASCII art.

### API Integration

* Retrieve live weather information using the OpenWeatherMap API.
* Parse JSON responses received from the API.
* Display an error message if weather information cannot be retrieved.

## Modules Used:

### Requests

Used for sending HTTP requests to the OpenWeatherMap API.

https://requests.readthedocs.io/

### Argparse

Used for handling command-line arguments.

https://docs.python.org/3/library/argparse.html

### PyFiglet

Used for displaying the city name in ASCII art format.

https://pypi.org/project/pyfiglet/

### Simple Chalk

Used for adding colored output to the terminal.

https://pypi.org/project/simple-chalk/

## Output (Video):

WeatherApp_CLI_Demo.mp4

## Output (Images):

### Running the Application:

Screenshot_Command_Line.png

### Weather Information Display:

Screenshot_Weather_Output.png

### Invalid City Error:

Screenshot_Error_Message.png
