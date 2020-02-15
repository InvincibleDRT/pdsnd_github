import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}


def get_filters_input():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while(city not in CITY_DATA):
        city = input(
            'enter  a valid city (chicago, new york city, washington):\n').lower()

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    # get user input for month (all, january, february, ... , june)
    month = ''

    while (month not in months) and month != 'all':
        month = input(
            "enter a valid month in 'january', 'february', 'march', 'april', 'may', 'june' :\n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day = ''
    while (day not in days) and day != 'all':
        day = input(
            "enter a valid day e.g. 'Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday' : \n").title()

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
        df - pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    # display the most common month
    print('Most common month:',  months[df['month'].mode()[0]-1].title())

    # display the most common day of week
    print('Most common day of week:', df['day_of_week'].mode()[0])

    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]

    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    print('Most Commonly used Start Station:', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Most Commonly used End Stations:', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['station_combo'] = 'Start Station : ' + \
        df['Start Station'] + ' End Station : ' + df['End Station']
    print('most frequent combination of start station and end station trip:',
          df['station_combo'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    start_time = time.time()

    # display total travel time
    print('\nCalculating Trip Duration...' +
          str(df['Trip Duration'].sum()) + ' \n')

    # display mean travel time
    print('\nCalculating Average Duration...' +
          str(df['Trip Duration'].mean()) + ' \n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User type counts : ')
    print(df['User Type'].value_counts())
    

    if 'Gender' in df.columns: 
        # Display counts of gender
        print('Gender counts: ')
        print(df['Gender'].value_counts())
    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        print('Earliest, Most Recent and Most Common Year of birth:')
        print((df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0]))
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def displaysample(df):
    display =input('do you want to display 5 rows of the data frame? Enter Yes or No :\n').lower()
    count =0
    while display == 'yes':
        print(df.iloc[count:count + 5])
        display=input('do you want to display 5 rows of the data frame? Enter Yes or No :\n')
        count+=5

        

def main():
    while True:
        city, month, day = get_filters_input()
        df = load_data(city, month, day)
        displaysample(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
