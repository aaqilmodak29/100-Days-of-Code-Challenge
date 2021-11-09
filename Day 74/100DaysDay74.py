# https://drive.google.com/file/d/1Y903pSBoZ759bdk0l6dSiPYs9ZOgh4GL/view?usp=sharing
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')


# Data Exploration
# Tesla
# Challenge:
# What are the shapes of the dataframes?
# How many rows and columns?
# What are the column names?
# Complete the f-string to show the largest/smallest number in the search data column
# Try the .describe() function to see some useful descriptive statistics
# What is the periodicity of the time series data (daily, weekly, monthly)?
# What does a value of 100 in the Google Trend search popularity actually mean?
df_tesla.shape
df_tesla.sort_values('MONTH')

df_tesla.columns

tesla_max = df_tesla["TSLA_USD_CLOSE"].max()
tesla_min = df_tesla["TSLA_USD_CLOSE"].min()
print(f'Largest value for Tesla in Web Search: {tesla_max}')
print(f'Smallest value for Tesla in Web Search: {tesla_min}')

df_tesla.describe()


# Unemployment Data
df_unemployment.shape
df_unemployment.head()

max_val = df_unemployment["UE_BENEFITS_WEB_SEARCH"].max()
max_val_2 = df_unemployment["UNRATE"].max()
print('Largest value for "Unemployemnt Benefits" '
      f'in Web Search: {max_val}')
print('Largest value for "Unemployemnt Benefits" '
      f'in Web Search: {max_val_2}')


# Bitcoin
df_btc_price.shape
df_btc_price.head()

df_btc_search.shape
df_btc_search.head()

max_val_btc = df_btc_search["BTC_NEWS_SEARCH"].max()
print(f'largest BTC News Search: {max_val_btc}')


# Data Cleaning Check for Missing Values
# Challenge: Are there any missing values in any of the dataframes? If so,
# which row/rows have missing values? How many missing values are there?
null_values_tsla = df_tesla.isna().values.sum()
null_values_un = df_unemployment.isna().values.sum()
null_values_btc_search = df_btc_search.isna().values.sum()
null_values_btc_price = df_btc_price.isna().values.sum()

print(f'Missing values for Tesla?: {null_values_tsla}')
print(f'Missing values for U/E?: {null_values_un}')
print(f'Missing values for BTC Search?: {null_values_btc_search}')
print(f'Missing values for BTC price?: {null_values_btc_price}')

total_null_values = null_values_btc_price + null_values_btc_search + null_values_tsla + null_values_un
print(f'Number of missing values: {total_null_values}')

# Challenge: Remove any missing values that you found.
df_btc_price.dropna(inplace=True)


# Convert Strings to DateTime Objects
# Challenge: Check the data type of the entries in the DataFrame MONTH or DATE
# columns. Convert any strings in to Datetime objects. Do this for all 4 DataFrames. Double check if your type
# conversion was successful.
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_tesla.MONTH.head()

df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_unemployment.MONTH.head()

df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_btc_search.MONTH.head()

df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
df_btc_price.DATE.head()


# Converting from Daily to Monthly Data
df_btc_price_monthly = df_btc_price.resample('M', on='DATE').last()
# If we wanted the average price over the course of the month, we could use something like:
# df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()
df_btc_price_monthly.head()
df_btc_price_monthly.shape

# Data Visualisation
# Notebook Formatting & Style Helpers
# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_format = mdates.DateFormatter('%Y')

# Tesla Stock Price v.s. Search Volume
# Challenge: Plot the Tesla stock price against the Tesla search volume using a
# line chart and two different axes. Label one axis 'TSLA Stock Price' and the other 'Search Trend'.

# Challenge:
# Add colours to style the chart. This will help differentiate the two lines and the axis labels. Try using one of the
# blue colour names for the search volume and a HEX code for a red colour for the stock price.

# Hint: you can colour both the axis labels and the lines on the chart using keyword arguments (kwargs).

# Challenge: Make the chart larger and easier to read.
# Increase the figure size (e.g., to 14 by 8).
# Increase the font sizes for the labels and the ticks on the x-axis to 14.
# Rotate the text on the x-axis by 45 degrees.
# Make the lines on the chart thicker.
# Add a title that reads 'Tesla Web Search vs Price'
# Keep the chart looking sharp by changing the dots-per-inch or DPI value.
# Set minimum and maximum values for the y and x axis. Hint: check out methods like set_xlim().
# Finally use plt.show() to display the chart below the cell instead of relying on the automatic notebook output.
# How to add tick formatting for dates on the x-axis.
plt.figure(figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search VS Price')

plt.xticks(fontsize=14, rotation=45)

price_axis = plt.gca()
search_axis = price_axis.twinx()

price_axis.set_ylabel('TSLA Stock Price', fontsize=14)
search_axis.set_ylabel('Search Trend', fontsize=14)

price_axis.set_ylim([0, 600])
price_axis.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

price_axis.xaxis.set_major_locator(years)
price_axis.xaxis.set_major_formatter(years_format)
price_axis.xaxis.set_minor_locator(months)

price_axis.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='g', linewidth=3)
search_axis.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='b', linewidth=3)

plt.show()


# Bitcoin (BTC) Price v.s. Search Volume
# Challenge: Create the same chart for the Bitcoin Prices vs. Search volumes.
#
# Modify the chart title to read 'Bitcoin News Search vs Resampled Price'
# Change the y-axis label to 'BTC Price'
# Change the y- and x-axis limits to improve the appearance
# Investigate the linestyles to make the BTC price a dashed line
# Investigate the marker types to make the search datapoints little circles
# Were big increases in searches for Bitcoin accompanied by big increases in the price?
plt.figure(figsize=(14, 8), dpi=120)
plt.title('Bitcoin News Search VS Resampled Price')

plt.xticks(fontsize=14, rotation=45)

price_axis = plt.gca()
search_axis = price_axis.twinx()

price_axis.set_ylabel('BTC Price', fontsize=14)
search_axis.set_ylabel('Search Trend', fontsize=14)

price_axis.set_ylim([0, 15000])
price_axis.set_xlim([df_btc_price_monthly.DATE.min(), df_btc_price_monthly.DATE.max()])

price_axis.xaxis.set_major_locator(years)
price_axis.xaxis.set_major_formatter(years_format)
price_axis.xaxis.set_minor_locator(months)

price_axis.plot(df_btc_price_monthly.DATE, df_btc_price_monthly.CLOSE, color='g', linewidth=3, linestyle='dashed')
search_axis.plot(df_btc_price_monthly.DATE, df_btc_search.BTC_NEWS_SEARCH, color='b', linewidth=3, marker="o")

plt.show()


# Unemployement Benefits Search vs. Actual Unemployment in the U.S.
# Challenge Plot the search for "unemployment benefits" against the unemployment rate.
#
# Change the title to: Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate
# Change the y-axis label to: FRED U/E Rate
# Change the axis limits
# Add a grey grid to the chart to better see the years and the U/E rate values. Use dashes for the line style
# Can you discern any seasonality in the searches? Is there a pattern?
# Challenge: Calculate the 3-month or 6-month rolling average for the web searches.
# Plot the 6-month rolling average search data against the actual unemployment.
# What do you see in the chart? Which line moves first?
plt.figure(figsize=(14, 8), dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. VS the U/E Rate')

plt.xticks(fontsize=14, rotation=45)

price_axis = plt.gca()
search_axis = price_axis.twinx()

price_axis.set_ylabel('FRED U/E Rate', fontsize=14)
search_axis.set_ylabel('Search Trend', fontsize=14)

price_axis.set_ylim([3, 11])
price_axis.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])

price_axis.xaxis.set_major_locator(years)
price_axis.xaxis.set_major_formatter(years_format)
price_axis.xaxis.set_minor_locator(months)

price_axis.grid(color='grey', linestyle='dashed')

roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
price_axis.plot(df_unemployment.MONTH, roll_df.UNRATE, color='g', linewidth=3, linestyle='dashed')
search_axis.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, color='b', linewidth=3)

plt.show()


# Including 2020 in Unemployment Charts
# Challenge: Read the data in the 'UE Benefits Search vs UE Rate 2004-20.csv' into a DataFrame.
# Convert the MONTH column to Pandas Datetime objects and then plot the chart. What do you see?
df_unemployment_till_2020 = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-20.csv')
df_unemployment_till_2020.MONTH = pd.to_datetime(df_unemployment_till_2020.MONTH)
df_unemployment_till_2020.head()

plt.figure(figsize=(14, 8), dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. VS the U/E Rate')

plt.xticks(fontsize=14, rotation=45)

price_axis = plt.gca()
search_axis = price_axis.twinx()

price_axis.set_ylabel('FRED U/E Rate', fontsize=14)
search_axis.set_ylabel('Search Trend', fontsize=14)

price_axis.set_ylim([3, 15])
price_axis.set_xlim([df_unemployment_till_2020.MONTH.min(), df_unemployment_till_2020.MONTH.max()])

price_axis.xaxis.set_major_locator(years)
price_axis.xaxis.set_major_formatter(years_format)
price_axis.xaxis.set_minor_locator(months)

price_axis.grid(color='grey', linestyle='dashed')

roll_df = df_unemployment_till_2020[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
price_axis.plot(
    df_unemployment_till_2020.MONTH, df_unemployment_till_2020.UNRATE, color='g', linewidth=3, linestyle='dashed'
)

search_axis.plot(
    df_unemployment_till_2020.MONTH, df_unemployment_till_2020.UE_BENEFITS_WEB_SEARCH, color='b', linewidth=3
)


# Learning Points & Summary
# In this lesson we looked at how to:

# How to use .describe() to quickly see some descriptive statistics at a glance.

# How to use .resample() to make a time-series data comparable to another by changing the periodicity.

# How to work with matplotlib.dates Locators to better style a timeline (e.g., an axis on a chart).

# How to find the number of NaN values with .isna().values.sum()

# How to change the resolution of a chart using the figure's dpi

# How to create dashed '--' and dotted '-.' lines using linestyles

# How to use different kinds of markers (e.g., 'o' or '^') on charts.

# Fine-tuning the styling of Matplotlib charts by using limits, labels, linewidth and colours
# (both in the form of named colours and HEX codes).

# Using .grid() to help visually identify seasonality in a time series.














