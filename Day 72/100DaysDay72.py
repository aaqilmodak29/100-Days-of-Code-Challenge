# # All Done in Google Colab
#
#
# # Import Statements
# # import pandas as pd
# # import matplotlib.pyplot as plt
#
#
# # Data Exploration
# # Read the .csv file and store it in a Pandas dataframe
# df = pd.read_csv("QueryResults.csv", names=['DATE', 'TAG', 'POSTS'])
#
# df.isna()
# clean_df = df.dropna()
#
# # Examine the first 5 rows and the last 5 rows of the of the dataframe
# clean_df.head()
# clean_df.tail()
#
# # Check how many rows and how many columns there are. What are the dimensions of the dataframe?
# clean_df.shape
#
# # Count the number of entries in each column of the dataframe
# clean_df.count()
#
# # Calculate the total number of post per language. Which Programming language has had the highest total number of
# # posts of all time?
# clean_df.groupby("TAG").sum()  # no. of posts
#
# max_id = clean_df['POSTS'].idxmax()
# clean_df['TAG'][max_id]
#
# # How many months of data exist per language? Which language had the fewest months with an entry?
# clean_df.groupby("TAG").count()  # months of entries per language
#
#
# # Data Cleaning
# # Let's fix the date format to make it more readable. We need to use Pandas to change format from a string of
# # "2008-07-01 00:00:00" to a datetime object with the format of "2008-07-01"
# df['DATE'][1]  # second entry in date column
#
# print(pd.to_datetime(df.DATE[1]))  # converting data type from str to timestamp
# type(pd.to_datetime(df.DATE[1]))
#
# # converting entire column
# df.DATE = pd.to_datetime(df.DATE)
# df.head()
#
#
# # Data Manipulation
# reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
#
# # What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column names
# # and print out the first 5 rows of the dataframe.
# reshaped_df.count()  # .count() excludes NaN values
# reshaped_df.shape
# reshaped_df.head()
# reshaped_df.tail()
#
# reshaped_df.columns
#
# # The inplace argument means that we are updating reshaped_df. Without this argument we would have to write something
# # like this: reshaped_df = reshaped_df.fillna(0)
# reshaped_df.fillna(0, inplace=True)
#
# # We can also check if there are any NaN values left in the entire DataFrame with this line:
# reshaped_df.isna().values.any()
# # we're chaining two more things:
# # the values attribute and the any() method.
# # This means we don't have to search through the entire DataFrame to spot if .isna() is True.
#
#
# # Data Visualisation with with Matplotlib
# # .figure() - allows us to resize our chart
# # .xticks() - configures our x-axis
# # .yticks() - configures our y-axis
# # .xlabel() - add text to the x-axis
# # .ylabel() - add text to the y-axis
# # .ylim() - allows us to set a lower and upper bound
#
# # To make our chart larger we can provide a width (16) and a height (10) as the figsize of the figure.
# plt.figure(figsize=(16,10))
#
# # setting lower limit of y axis
# plt.ylim(0, 35000)
#
# # adding labels
# plt.xlabel('Date', fontsize=14)
# plt.ylabel('Number of Posts', fontsize=14)
#
# # when we increase the size of the chart, we should also increase the fontsize of the ticks on our axes so that they
# # remain easy to read:
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)
#
# # plot the popularity of the Java programming language.
# # plt.plot(reshaped_df.index, reshaped_df.java)
#
# # plot the popularity of the Python programming language.
# # plt.plot(reshaped_df.index, reshaped_df.python)
#
# # plot the popularity of all programming language.
# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column], linewidth=3, label=reshaped_df[column].name)
# plt.legend(fontsize=16)
#
#
# # Smoothing out Time Series Data
# # Time series data can be quite noisy, with a lot of up and down spikes. To better see a trend we can
# # plot an average of, say 6 or 12 observations. This is called the rolling mean. We calculate the average in a window
# # of time and move it forward by one overservation. Pandas has two handy methods already built in to work this out:
# # rolling() and mean().
#
# roll_df = reshaped_df.rolling(window=12).mean()
#
# plt.figure(figsize=(16, 10))
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)
# plt.xlabel('Date', fontsize=14)
# plt.ylabel('Number of Posts', fontsize=14)
# plt.ylim(0, 35000)
#
# # plot the roll_df instead
# for column in roll_df.columns:
#     plt.plot(roll_df.index, roll_df[column],
#              linewidth=3, label=roll_df[column].name)
#
# plt.legend(fontsize=16)
#
#
# # Learning Points & Summary
#
# # We've
# # used .groupby() to explore the number of posts and entries per programming language
#
# # converted strings to Datetime objects with to_datetime() for easier plotting
#
# # reshaped our DataFrame by converting categories to columns using .pivot()
#
# # used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then replaced using
# # .fillna()
#
# # created (multiple) line charts using .plot() with a for-loop
#
# # styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.
#
# # added a legend to tell apart which line is which by colour
#
# # smoothed out our time-series observations with .rolling().mean() and plotted them to better identify trends over
# # time.
