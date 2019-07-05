#!/usr/bin/env python3
import pyowm
import argparse
import subprocess

# font from => https://github.com/erikflowers/weather-icons/tree/master/font

# use case:
# ./openweather_day.py --get_weather_unicode --api_key <API_KEY> --city $(./whereami_city.sh)  --ccode $(./whereami_countrycode.sh)

def icoToUnicode(s):
    if s == "01d":
        return "\uF00D"
    elif s == "01n":
        return "\uF02E"
    elif s == "02d":
        return "\uF002"
    elif s == "02n":
        return "\uF086"
    elif s == "03d":
        return "\uF041"
    elif s == "03n":
        return "\uF041"
    elif s == "04d":
        return "\uF013"
    elif s == "04n":
        return "\uF013"
    elif s == "09d":
        return "\uF01A"
    elif s == "09n":
        return "\uF01A"
    elif s == "10d":
        return "\uF009"
    elif s == "10n":
        return "\nF029"
    elif s == "11d":
        return "\uF005"
    elif s == "11n":
        return "\uF025"
    elif s == "13d":
        return "\uF00A"
    elif s == "13n":
        return "\uF02A"
    elif s == "50d":
        return "\uF003"
    elif s == "50n":
        return "\uF04A"

def process (args):

    owm = pyowm.OWM(args.api_key[0])
    weather_details = owm.weather_at_place(args.city[0] + ',' + args.ccode[0])
    weather_values = weather_details.get_weather()

    if args.get_temp_c:
        print(int(weather_values.get_temperature(unit='celsius')['temp']))
    if args.get_temp_f:
        print(int(weather_values.get_temperature(unit='fahrenheit')['temp']))
    if args.get_weather_icon:
        print('PNG/'+weather_values.get_weather_icon_name()+'.png')
    if args.get_wind_angle:
        print(int(weather_values.get_wind()['deg']))
    if args.get_wind_force:
        print(int(weather_values.get_wind()['speed']))
    if args.get_weather_unicode:
        print(icoToUnicode(weather_values.get_weather_icon_name()))
    if args.is_night:
        print(weather_values.get_weather_icon_name()[2])
    


parser = argparse.ArgumentParser(description='Openweather script.')
parser.add_argument('--api_key',help='OWM API key.',nargs=1,metavar=('[api_key]'), required=True)
parser.add_argument('--city',help='Cityname.',nargs=1,metavar=('[city]'), required=True)
parser.add_argument('--ccode',help='Country code.',nargs=1,metavar=('[code]'), required=True)
parser.add_argument('--get_temp_c',help='Get temperature in Celsius.',action='store_true')
parser.add_argument('--get_temp_f',help='Get temperature in Fahrenheit.',action='store_true')
parser.add_argument('--get_weather_icon',help='Get weekday.',action='store_true')
parser.add_argument('--get_wind_angle',help='Get wind angle.',action='store_true')
parser.add_argument('--get_wind_force',help='Get wind force.',action='store_true')
parser.add_argument('--get_weather_unicode',help='Get weather in unicode.',action='store_true')
parser.add_argument('--is_night',help='Get day/night.',action='store_true')
args = parser.parse_args()

process(args)
