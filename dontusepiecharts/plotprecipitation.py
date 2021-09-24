import math
import re
import os
import pandas
import datetime
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pyplot as plt

# Our new date parser
def yyyymmdd_parser(s):
    return datetime.datetime.strptime(s, '%Y-%m-%d')

def get_data(weather_dir):
    p = re.compile('victoria-weather-[0-9]+.csv')
    data = []
    for filename in sorted(os.listdir(weather_dir)):
        if p.match(filename):
            path = os.path.join(weather_dir, filename)
            # We identify which column contains the date, along with the date parser to use.
            yearly_data = pandas.read_csv(path, parse_dates=['Date/Time'], date_parser=yyyymmdd_parser)
            data.append(yearly_data)
    return pandas.concat(data)

def get_days_since_jan1(date):
    return date.timetuple().tm_yday - 1

def split_data_by_day_of_week(weather):
    by_day_of_week = [[] for _ in range(7)]
    for i, row in weather.iterrows():
        date = row['Date/Time']
        rainfall = row['Total Precip (mm)']

        # 1cm snow = 10mm snow; 13mm of snow = 1mm of rain
        snowfall = row['Total Snow (cm)'] * 10.0 / 13.0
        rainfall += snowfall

        day_of_week = date.weekday()
        by_day_of_week[day_of_week].append(float(rainfall))

    return by_day_of_week

def get_total_rainfall(val):
    year, annual_data = val
    total_rainfall = annual_data['rainfall'].cumsum().to_list()[-1]
    return (total_rainfall, year)

def format_days_since_jan1(days, pos=None):
    date = datetime.date(2020, 1, 1) + datetime.timedelta(days)
    return date.strftime('%b')

import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10.0, 7.0), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])

weather = get_data('data')
weather['Total Precip (mm)'] = weather['Total Precip (mm)'].fillna(0)
weather['Total Snow (cm)'] = weather['Total Snow (cm)'].fillna(0)
rainfall_by_day_of_week = split_data_by_day_of_week(weather)

total_rainfall_by_day_of_week = [sum(x) for x in rainfall_by_day_of_week]

# Monday, Tuesday, ..., Sunday
day_names = days = [datetime.date(2001, 1, 1+i).strftime('%A') for i in range(7)]

import plot
plot.plot_horizontal_lollipop(total_rainfall_by_day_of_week, day_names, 'rainfall-by-day-of-week.png', sort=False, xlabel='precipitation (mm)', ylabel='day of week', reverse=True, title='total precipitation by day of week')

plot.plot_pie(total_rainfall_by_day_of_week, day_names, 'rainfall-by-day-of-week-pie-chart-is-hard-to-read.png')

plot.plot_horizontal_box_and_whisker(rainfall_by_day_of_week, day_names, 'rainfall-by-day-of-week-box-and-whisker-with-outliers.png',
    sort=False, xlabel='precipitation (mm)', ylabel='day of week', reverse=True, title='precipitation by day of week (with outliers)', whis=None)

plot.plot_horizontal_box_and_whisker(rainfall_by_day_of_week, day_names, 'rainfall-by-day-of-week-box-and-whisker.png',
    sort=False, xlabel='precipitation (mm)', ylabel='day of week', reverse=True, title='precipitation by day of week', whis=999999)

amounts_when_raining = [
    [x for x in amounts if x > 0]
    for amounts in rainfall_by_day_of_week
    ]
plot.plot_horizontal_box_and_whisker(amounts_when_raining, day_names, 'rainfall-by-day-of-week-box-and-whisker-when-raining.png',
    sort=False, xlabel='precipitation (mm)', ylabel='day of week', reverse=True, title='amounts of precipitation for days when precipitation happened', whis=None)

binary_raining_or_not_by_day_of_week = [
    sum([1 for x in amounts if x > 0])
    for amounts in rainfall_by_day_of_week
    ]
plot.plot_horizontal_lollipop(binary_raining_or_not_by_day_of_week, day_names, 'number-of-wet-days-by-day-of-week.png', sort=False, reverse=True, percentage=True,
    title='distribution of days that experienced rain >= 1mm, values sum to 100%',
    xlabel='percentage of rainy days',
        )

#plot.plot_waffle(binary_raining_or_not_by_day_of_week, day_names, 'waffle.png', sort=False)

#chance_of_rain_by_day_of_week = [
#    sum([1 for x in amounts if x > 10]) / len(amounts)
#    for amounts in rainfall_by_day_of_week
#    ]
#plot.plot_horizontal_lollipop(chance_of_rain_by_day_of_week, day_names, 'chance-of-rain-by-day-of-week.png', sort=False, reverse=True, format_percentage=True,
#    title='chance of rain given a particular day of the week',
#        )
