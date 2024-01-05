# # Data Import, Cleaning and Structuring

# Here is the link to this specific data set, [**Motor Vehicle Collisions**](https://catalog.data.gov/dataset/motor-vehicle-collisions-crashes)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mv_col = pd.read_csv("./Motor_Vehicle_Collisions.csv", low_memory=False)
mv_col.info()

# Date and time are in different columns but we can do alot if they are both in the same column rather than when apart. So let us put them together then convert to datetime format

mv_col["CRASH DATE"] = mv_col["CRASH DATE"] + " " + mv_col["CRASH TIME"]

mv_col["CRASH DATE"]

mv_col["CRASH DATE"] = pd.to_datetime(mv_col["CRASH DATE"])

mv_col.shape

# From the date column, let us create four more columns, 
# * Crash year, will have only the year of crash.
# * Crash month will have the month relating to the crash in numeric format.
# * Crash month name will be the name of the month.
# * Crash hour will be the hour of the day, in 24hr format, when the crash occurred.

mv_col["CRASH YEAR"] = mv_col["CRASH DATE"].dt.year
mv_col["CRASH MONTH"] = mv_col["CRASH DATE"].dt.month
mv_col["CRASH MONTH NAME"] = mv_col["CRASH DATE"].dt.strftime('%b')
mv_col["CRASH HOUR"] = mv_col["CRASH DATE"].dt.hour
mv_col["CRASH WEEK"] = mv_col["CRASH DATE"].dt.strftime('%a')

# Later on during the analysis, you will notice that some of the vehicle types have their names in different cases(upper and lower) in both Vehicle Type Code 1 and Vehicle Type 2 columns. To avoid getting back data preparation once the analysis has started, let's us do it right now.
# * **SPORT UTILITY / STATION WAGON** and **Station Wagon/Sport Utility Vehicle** are treated and different categories, we will rename the former to match the later.
# * The same is observed in the instances of **PICK-UP TRUCK** vs **Pick-up Truck** and **TAXI** vs **Taxi**

mv_col["VEHICLE TYPE CODE 1"] = mv_col["VEHICLE TYPE CODE 1"].replace(["SPORT UTILITY / STATION WAGON"], "Station Wagon/Sport Utility Vehicle")
mv_col["VEHICLE TYPE CODE 2"] = mv_col["VEHICLE TYPE CODE 2"].replace(["SPORT UTILITY / STATION WAGON"], "Station Wagon/Sport Utility Vehicle")

mv_col['VEHICLE TYPE CODE 1'] = mv_col['VEHICLE TYPE CODE 1'].replace(["PICK-UP TRUCK"], "Pick-up Truck")
mv_col['VEHICLE TYPE CODE 2'] = mv_col['VEHICLE TYPE CODE 2'].replace(["PICK-UP TRUCK"], "Pick-up Truck")

mv_col['VEHICLE TYPE CODE 1'] = mv_col['VEHICLE TYPE CODE 1'].replace(["TAXI"], "Taxi")
mv_col['VEHICLE TYPE CODE 2'] = mv_col['VEHICLE TYPE CODE 2'].replace(["TAXI"], "Taxi")

# We will also put **4 dr sedan** in the **Sedan** category by renaming the former

mv_col['VEHICLE TYPE CODE 1'] = mv_col['VEHICLE TYPE CODE 1'].replace(["4 dr sedan"], "Sedan")
mv_col['VEHICLE TYPE CODE 2'] = mv_col['VEHICLE TYPE CODE 2'].replace(["4 dr sedan"], "Sedan")

# We might have to check the road accidents during different seasons, so let us create a Crash Season column

def get_season(month):
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Autumn"
    else:
        return "Winter"

mv_col["CRASH SEASON"] = mv_col['CRASH MONTH'].apply(get_season)

mv_col.shape

mv_col.isna().sum()

# There are a number of columns which will not be of help to our analysis, We will get rid of them. Currently, there are a totals of 35 columns, 16 will be of no use that means we will only need 19 of them. 
# For the columns that we will use, there are only a few of them which are missing their values hence the missing values are insignificant and will not affect our analysis

retain = ["CRASH DATE", "CRASH YEAR", "CRASH MONTH", "CRASH MONTH NAME", 
          "CRASH HOUR", "CRASH WEEK", "CRASH SEASON","NUMBER OF PERSONS INJURED", "NUMBER OF PERSONS KILLED",
        "NUMBER OF PEDESTRIANS INJURED", "NUMBER OF PEDESTRIANS KILLED", 
        "NUMBER OF CYCLIST INJURED", "NUMBER OF CYCLIST KILLED", 
        "NUMBER OF MOTORIST INJURED", "NUMBER OF MOTORIST KILLED", 
        "CONTRIBUTING FACTOR VEHICLE 1", "CONTRIBUTING FACTOR VEHICLE 2", 
        "VEHICLE TYPE CODE 1", "VEHICLE TYPE CODE 2"]

mv_collisions = mv_col[retain]

mv_collisions.info()

mv_collisions.shape

# This dataset may have some duplicated rows, and for accurate analysis, we will have to get rid of them.

mv_collisions = mv_collisions.drop_duplicates()

mv_collisions.to_csv("./cleaned_data.csv",index=False)