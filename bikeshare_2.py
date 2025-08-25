import time
import pandas as pd

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv"
}

# I have restructured the program a little bit as i was having issues running the python file from VS code


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    df = pd.read_csv(CITY_DATA[city])
# conversion of Start Time coloumn to pandas datetime data type, also extracting the month, days, hours
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour

    # filter for months
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month_index = months.index(month) + 1
        df = df[df["month"] == month_index]

    # filter for days
    if day != "all":
        df = df[df["day_of_week"].str.lower() == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print("\nMost Frequent Times of Travel\n")
    start_time = time.time()


    # for finding common month
    common_month = df["month"].mode()[0]
    print(f"Most common month: {common_month}")

     # for finding common day
    common_day = df["day_of_week"].mode()[0]
    print(f"Most common day of week: {common_day}")
  
    # for finding common hour
    common_hour = df["hour"].mode()[0]
    print(f"Most common start hour: {common_hour}")

    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    common_start = df["Start Station"].mode()[0]
    print(f"Most commonly used start station: {common_start}")

    common_end = df["End Station"].mode()[0]
    print(f"Most commonly used end station: {common_end}")

    df["route"] = df["Start Station"] + " -> " + df["End Station"]
    common_route = df["route"].mode()[0]
    print(f"Most frequent trip: {common_route}")

    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print("\nCalculating Trip Duration...\n")
    start_time = time.time()
  
    total_travel = df["Trip Duration"].sum()
    mean_travel = df["Trip Duration"].mean()

    print(f"Total time traveled: {total_travel} seconds")
    print(f"Mean travel time: {mean_travel} seconds")

    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Displaying the number of use types
    print("Number of user types:")
    print(df["User Type"].value_counts())
    
    # Gender (not present in washington data set)
    if "Gender" in df.columns:
        print("\nTypes of gender:")
        print(df["Gender"].value_counts())
    else:
        print("\nGender not available for city")

    # Birth Year (not present in washington data set)
    if "Birth Year" in df.columns:
        earliest = int(df["Birth Year"].min())
        most_recent = int(df["Birth Year"].max())
        common_year = int(df["Birth Year"].mode()[0])

        print("\nBirth year stats:")

        print(f"Earliest birth year: {earliest}")

        print(f"Most recent: {most_recent}")

        print(f"Most common: {common_year}")
    else:
        print("\nBirth year not available for city")

    print(f"\nThis took {time.time() - start_time} seconds.")
    print("-" * 40)

def main():
    while True:
        print("Hello! Let's explore some US bikeshare data!")
      
      #asking user for city with invalid city check
        while True:
            city_input = input("Choose a city (chicago, new york city, washington): ").strip().lower()
            if city_input in ["chicago", "new york city", "washington"]:
                city = city_input
                break
            else:
                print("City not present, Please choose from: chicago, new york city, washington")

        
        while True:
            month_input = input("Choose a month (january, february, march, april, may, june, or 'all'): ").strip().lower()
            if month_input in ["january", "february", "march", "april", "may", "june", "all"]:
                month = month_input
                break
            else:
                print("Month not present, Please choose from: january, february, march, april, may, june, all")

        
        while True:
            day_input = input("Choose a day of week (monday, tuesday, wednesday, thursday, friday, saturday, sunday, or 'all'): ").strip().lower()
            if day_input in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
                day = day_input
                break
            else:
                print("Invalid day, Please choose from: monday, tuesday, wednesday, thursday, friday, saturday, sunday, all")
        
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input("\n Restart Program? (yes/no): ").lower()
        if restart != "yes":
            print("Goodbye - Kripansh")
            break

     #using this to run main() function directly 
if __name__ == "__main__":
    main()
