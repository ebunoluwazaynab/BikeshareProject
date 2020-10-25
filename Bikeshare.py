import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january' , 'february' , 'march' , 'april' , 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        # get user input for city (chicago, new york city, washington)
        city = input('Would you like to see data for Chicago, New York City or Washington? : ').strip().lower()
        # check if city is in CITY_DATA
        if city in CITY_DATA:
            break
        else:
            print('\n City not valid')
            
               
    while True:
        user_input = input('Do you want to filter by month, day, both or none? : ' ).strip().lower()
       # ask user to filter data by month, day, both, or none
        if user_input == 'month':
            # get user input for month (all, january, february, ... , june)
            month = input('Which month? January, February, March, April, May, June or All? : ').strip().lower()
            #check if month is in months
            while month not in months:
                print('\n Month not valid') 
                month = input('Enter month again... :')
            else:
                day = "all"
            break
            
        elif user_input == 'day':
            # get user input for day of week (all, monday, tuesday, ... sunday)
            day = input('Which day?  Sunday, Monday, Tuesday, Wednesday.....Saturday? : ').strip().lower()
            #check if day is in days
            while day not in days:
                print('\n Day not valid')
                day = input('Enter day again... :')
            else:
                month = "all"
            break
            
        elif user_input == 'both':
            # get user input for month (all, january, february, ... , june)
            month = input('Which month? January, February, March, April, May, June or All? : ').strip().lower()
            while month not in months:
                print('\n month not valid') 
                month = input('Enter month again...:') 
            # get user input for day of week (all, monday, tuesday, ... sunday)
            day = input('Which day?  Sunday, Monday, Tuesday, Wednesday.....Saturday or All ? : ').strip().lower()
            #check if month in months and day in days
            while day not in days:
                print('\n Day not valid')
                day = input('Enter day again...:')
            break
            
        elif user_input == 'none' :
            month = "all"
            day = "all"
            break
        else:
            print('Input not valid')
            pass      
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city -name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
  
    df = pd.read_csv(CITY_DATA[city])
   
    df['Start Time'] = pd.to_datetime(df['Start Time'], format = '%Y-%m-%d %H:%M:%S')
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.capitalize()]

    
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day'] == day.capitalize()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('\nMost Common Month:\n', most_common_month)

    # display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('\nMost Common Day of Week:\n', most_common_day)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('\nMost Common Day Start Hour:\n', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('\n Most Commonly Used Start Station :\n', most_commonly_used_start_station)

    # display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('\n Most Commonly Used End Station :\n', most_commonly_used_end_station)

    # display most frequent combination of start station and end station trip
    most_frequent_combination_of_start_station_and_end_station_trip = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    print('\n Most Frequent Combination Of Start Station And End Station Trip :\n', most_frequent_combination_of_start_station_and_end_station_trip.mode()[0])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    
    # display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal Travel Time :\n', pd.Timedelta(total_travel_time, unit = 's'))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean Travel Time :\n', pd.Timedelta(mean_travel_time, unit = 's'))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('\nCounts of User Types :\n', counts_of_user_types)
    

    # Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('\nCounts of Gender :\n', counts_of_gender)
    except:
        print('No gender')
    

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        print('\nEarliest Year of Birth\n' , earliest_year_of_birth)
        most_recent_year_of_birth = int(df['Birth Year'].max())
        print('\nMost Recent Year Of Birth\n' , most_recent_year_of_birth)
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print('\nMost Common Year Of Birth\n' , most_common_year_of_birth)
    except:
        print('\nNo Birth Year\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
