# This file helps us to understand the data in any file.
import pandas as pd
import numpy as np
import datetime


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_list = ['january', 'february', 'march', 'april', 'may', 'june']


#Function to convert month string to month number
def month_to_num(month):
    return months_list.index(month) + 1

# Function to convert month number to month string
def num_to_month(month_num):
    month_num -= 1
    return months_list[month_num]

# Function to identify count of user types
def load_data(city, month, day):
    file = CITY_DATA[city]
    with open(file) as df:
        # Load data file into a dataframe
        df = pd.read_csv(df)
        # Convert Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
#        # Create hour column
        df['Hour'] = df['Start Time'].dt.hour
        # Create day column
        df['Day of week'] = df['Start Time'].dt.weekday
        # Create month column
        df['Month'] = df['Start Time'].dt.month

        # Filter by month if applicable
        # Convert month to lower case
        month = month.lower()
        if month != 'all':
            # Convert to month index and extract month data
            month = month_to_num(month)
            df = df[df['Month'] == month]

        # Filter by day of week if applicable
        # Convert day to lower case
        if day != 'all':
            df = df[df['Day of week'] == day]
    return df

# Create functions for interactive program

# Function to ask user to choose the city
def choose_city():
    while True:
        try:
            user_input = input('\nWhich city would you like to analyse? Chicago, Washington, or New York City? ')
            user_input = user_input.lower()
            if (user_input == 'chicago') or (user_input == 'new york city') or (user_input == 'washington'):
                file = CITY_DATA[user_input]
                city = user_input
                return city
            else:
                false
            break
        except NameError:
            print('Please check your spelling!')

# Function to ask user whether they would like to choose the month
def choose_month():
    while True:
        try:
            user_input = input('\nWould you like to filter by month? Type Y for Yes, N for No: ')
            user_input = user_input.lower()
            if user_input == 'y':
                # Ask user to select the month
                while True:
                    try:
                        user_input = input('Enter a month (January to June): ')
                        user_input = user_input.lower()
                        if user_input in months_list:
                            month = user_input
                            return month
                            break
                        else:
                            false
                        break
                    except NameError:
                        print('Please check your spelling!')
            # Set default month as all
            elif user_input == 'n':
                month = 'all'
                return month
            else:
                false
            break
        except NameError:
            print('Please try entering that answer again.')

# Function to ask user whether they would like to filter by days
def choose_day():
    while True:
        try:
            user_input = input('\nWould you like to filter by day? Type Y for Yes, N for No: ')
            user_input = user_input.lower()
            if user_input == 'y':
                # Ask user to choose the day of the week
                while True:
                    try:
                        user_input = input('Enter a day of the week: ')
                        user_input = user_input.lower()
                        days = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday':6}
                        if user_input in days:
                            day = days[user_input]
                            print('You selected {}.'.format(user_input.title()))
                            return day
                        else:
                            false
                        break
                    except NameError:
                        print('Please check your spelling!')
            # Set default day as all
            elif user_input == 'n':
                day = 'all'
                print('You selected all days.')
                return day
            else:
                false
            break
        except NameError:
            print('Please try entering that answer again.')
    return day

# Function to ask user whether they would like to see raw data
def choose_raw_data(df):
    while True:
        try:
            user_input = input('\nWould you like to view the raw data? Y or N: ')
            user_input = user_input.lower()
            if user_input == 'y':
                i = 0
                while user_input == 'y':
                    user_input == 'y'
                    print(df[i:i+5])
                    user_input = input('Would you like to view more raw data? Y or N: ')
                    user_input = user_input.lower()
                    i += 5
            elif user_input == 'n':
                print('You have asked not to display raw data.')
            break
        except NameError:
            print('Check your answer and try again.')

# Function to identify most popular travel time_stats
def popular_times(df, city, month, day):
    city = city.title()
    print('\nWhat are the most popular times for bikeshare travel?')
    #Find popular month:
    if month == 'all':
        popular_month = df['Month'].mode()[0]
        popular_month = num_to_month(popular_month).title()
        print('The most popular month in {} is: {}.'.format(city, popular_month))
    #Find popular day:
    if day == 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        popular_day = df['Day of week'].mode()[0]
        popular_day = days[popular_day].title()
        print('The most popular day in {} is: {}.'.format(city, popular_day))
    #Find popular hour:
    popular_hour = df['Hour'].mode()[0]
    print('The most popular hour is: {}:00.'.format(popular_hour))

# Function to identify the most popular start and end locations
def popular_places(df):
    print('\nWhat are the most popular start and end stations?')
    popular_start = df['Start Station'].mode()[0]
    print('Most popular journey start: {}.'.format(popular_start))
    popular_end = df['End Station'].mode()[0]
    print('Most popular journey end: {}.'.format(popular_end))

# Function to identify most popular journey from start to end
def popular_journey(df):
    print('\nWhat is the most popular journey?')
    #Make a new column combining start and end stations.
    df['Journey'] = df['Start Station'] + ' to ' + df['End Station']
    popular_journey = df['Journey'].mode()[0]
    print('The most popular journey is {}.'.format(popular_journey))

# Function to break up a number of seconds into largest possible time units
# Returns either with weeks as largest unit, or minutes as largest unit
def seconds_into_time(num_seconds,biggest_unit):
    tot_weeks = num_seconds // 604800
    remainder = num_seconds % 604800
    tot_days = remainder // 86400
    remainder = remainder % 86400
    tot_hours = remainder // 3600
    remainder = remainder % 3600
    tot_min = remainder // 60
    remainder = remainder % 60
    tot_sec = int(remainder)
    if biggest_unit == 'weeks_biggest':
        return '{} week(s), {} days(s), {} hour(s), {} minute(s) and {} second(s)'.format(tot_weeks, tot_days, tot_hours, tot_min, tot_sec)
    elif biggest_unit == 'min_biggest':
        return '{} minute(s) and {} second(s)'.format(tot_min, tot_sec)

# Function to find the total travel time
# "Total travel time" interpreted to be sum of all journey durations in df
def total_travel(df):
    total_travel = sum(df['Trip Duration'])
    total_travel = seconds_into_time(total_travel, 'weeks_biggest')
    print('\nTotal travel time is {}.'.format(total_travel))

# Function to find mean trip duration
def avg_travel(df):
    avg_travel = df['Trip Duration'].mean()
    avg_travel = seconds_into_time(avg_travel, 'min_biggest')
    print('\nAverage trip duration is {}.'.format(avg_travel))

# Function to count user types
def user_types(df):
    num_user_types = df['User Type'].value_counts()
    print('\nThe count of user types is: ')
    print('Customer: {}'.format(num_user_types['Customer']))
    print('Subscriber: {}'.format(num_user_types['Subscriber']))
    if 'Dependent' in num_user_types:
        print('Dependent: {}'.format(num_user_types['Dependent']))


# Function to count male and female bike share user_types
def user_gender(df):
    num_gender = df['Gender'].value_counts()
    print('\nThe count of user genders is:')
    print('Male: {}'.format(num_gender['Male']))
    print('Female: {}'.format(num_gender['Female']))

def birth_year(df):
    print('\nBirth year of users:')
    # Find most common birth year.
    common_year = df['Birth Year'].mode()[0]
    common_year = int(common_year)
    print('The most common birth year among users is {}.'.format(common_year))
    # Find earliest birth year.
    early_year = df['Birth Year'].min()
    early_year = int(early_year)
    print('\nThe earliest recorded birth year is {}.'.format(early_year))
    if early_year <= 1917:
        age = 2017 - early_year
        print('(That bike share user is {} years old! Astonishing!)'.format(age))
    late_year = df['Birth Year'].max()
    late_year = int(late_year)
    print('\nThe latest recorded birth year is {}.'.format(late_year))
    if late_year >= 2014:
        age = 2017 - late_year
        print('(Apparently that bikeshare user is {} year(s) old! Wow.)'.format(age))


#Begin interactive program

def main():
    do_analysis = 'y'
    while do_analysis.lower() == 'y':
        print('\n\nLet\'s begin analysing the bikeshare data.')
        # Get user inputs for city, month, day
        # City
        city = choose_city()
        print('You selected this city: {}.'.format(city))
        # Month
        month = choose_month()
        print('The month(s) you selected is: {}.'.format(month.title()))
        # Day
        day = choose_day()
        # Load selected data
        df = load_data(city,month,day)
        # Get user input for seeing raw data
        choose_raw_data(df)
        # Begin printing statistics
        print('\n\nHere are summary statistics for the data you have chosen: ')
        popular_times(df, city, month, day)
        popular_places(df)
        popular_journey(df)
        total_travel(df)
        avg_travel(df)
        user_types(df)
        if city in ['new york city', 'chicago']:
            user_gender(df)
            birth_year(df)
        else:
            break

        do_analysis = input("\n\nPlease press 'y' to start again, or press any other key to exit. ")



if __name__ == '__main__':
    main()
