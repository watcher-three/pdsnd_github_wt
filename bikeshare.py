import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print("\nWelcome to the Bikeshare Data Analysis Program. Begin by selecting a city to study:")
        print("\nChicago\nNew York City\nWashington\n")
        city = input().lower()
        
        if city not in CITY_DATA.keys():
            print("\nInput not recognized, please check your selection and try again.")
    
    print("\nYou have selected {} as your city of study.".format(city.title()))
    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    MONTH_LIST = {'january', 'february', 'march', 'april', 'may', 'june', 'all'}
    month = ''
    while month not in MONTH_LIST:
        print("\nPlease select a month to study:")
        print("\nJanuary\nFebruary\nMarch\nApril\nMay\nJune\nAll\n")
        month = input().lower()
        
        if month not in MONTH_LIST:
            print("\nInput not recognized, please check your selection and try again.")
    
    print("\nYou have selected {} as your month(s) of study.".format(month.title()))
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    DAY_LIST = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = ''
    while day not in DAY_LIST:
        print("\nPlease select a day of the week to study:")
        print("\nSunday\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nAll\n")
        day = input().lower()
        
        if day not in DAY_LIST:
            print("\nInput not recognized, please check your selection and try again.")
    
    print("\nYou have selected {} as your day(s) of study.".format(day.title()))
    
    print("\nYou have elected to study data for {} on day(s): {} in month(s): {}.".format(city.title(), day.title(), month.title()))
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nLoading...")
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    top_month = df['month'].mode()[0]
    
    print("The top travel month is {}.".format(top_month))

    # TO DO: display the most common day of week
    top_day = df['day_of_week'].mode()[0]
    
    print("\nThe top travel day is {}.".format(top_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    top_hour = df['hour'].mode()[0]
    
    print("\nThe top departure hour is {}00 hours.".format(top_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    top_start_station = df['Start Station'].mode()[0]
    
    print("The top starting station is {}.".format(top_start_station))

    # TO DO: display most commonly used end station
    top_end_station = df['End Station'].mode()[0]
    
    print("\nThe top ending station is {}.".format(top_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'].str.cat(df['End Station'], sep = ' to ')
    top_station_combo = df['Start to End'].mode()[0]
    
    print("\nThe top start point to end point trip is {}.".format(top_station_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    if total_time > 68400:
        m, s = divmod(total_time, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        print("\nThe total trip duration is {} days, {} hours, {} minutes, and {} seconds.".format(d, h, m, s))
    elif s > 3600:
        m, s = divmod(total_time, 60)
        h, m = divmod(m, 60)
        print("\nThe total trip duration is {} hours, {} minutes, and {} seconds.".format(h, m, s))
    else:
        m, s = divmod(total_time, 60)
        print("\nThe total trip duration is {} minutes and {} seconds.".format(m, s))
    
   # TO DO: display mean travel time
    avg_time = round(df['Trip Duration'].mean())
    if avg_time > 68400:
        m, s = divmod(avg_time, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        print("\nThe average trip duration is {} days, {} hours, {} minutes, and {} seconds.".format(d, h, m, s))
    elif s > 3600:
        m, s = divmod(avg_time, 60)
        h, m = divmod(m, 60)
        print("\nThe average trip duration is {} hours, {} minutes, and {} seconds.".format(h, m, s))
    else:
        m, s = divmod(avg_time, 60)
        print("\nThe average trip duration is {} minutes and {} seconds.".format(m, s))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    
    print("The counts of each type of user are given below:\n\n{}".format(user_type))

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_count()
        print("\nThe count of each gender user are given below:\n\n{}".format(user_gender))
    except:
        print("\nThere is no gender information in this file.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth is {}\nThe most recent year of birth is {}\nThe most common year of birth is {}".format(earliest, most_recent, most_common))
    except:
        print("There is no year of birth information in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    #Prompt to display rows of data
    RESPONSE_LIST = ['yes', 'no']
    view_data = ''
    start_loc = 0
    while view_data not in RESPONSE_LIST:
        print("\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n")
        view_data = input().lower()
        
        if view_data not in RESPONSE_LIST:
            print("\nInput not recognized, please enter yes or no.\n")
        elif view_data == 'yes':
            print(df.head())

    while view_data == 'yes':
        print("\nDo you wish to view more individual trip data? Enter yes or no\n")
        view_data = input().lower()
        start_loc += 5
        if view_data not in RESPONSE_LIST:
            print("\nInput not recognized, please enter yes or no.\n")
        elif view_data == 'yes':
            print(df[start_loc:start_loc+5])
        elif view_data == 'no':
            break
        
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
