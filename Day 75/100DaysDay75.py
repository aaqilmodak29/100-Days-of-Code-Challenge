# https://drive.google.com/file/d/1DNLOk7ELuR0Vw1VbpA6GkNWU9qml6mh_/view?usp=sharing
#
#
# import pandas as pd
# import plotly.express as px
#
#
# # Notebook Presentation
# # Show numeric output in decimal format e.g., 2.15
# pd.options.display.float_format = '{:,.2f}'.format
#
#
# # Read the Dataset
# df_apps = pd.read_csv('apps.csv')
#
#
# # Data Cleaning
# # Challenge: How many rows and columns does df_apps have? What are the column names?
# # Look at a random sample of 5 different rows with .sample().
# df_apps.shape
# df_apps.columns
# df_apps.sample(5)
#
#
# # Drop Unused Columns
# # Challenge: Remove the columns called Last_Updated and Android_Version from the DataFrame.
# # We will not use these columns.
# del df_apps['Android_Ver']
# del df_apps['Last_Updated']
# df_apps.shape
#
#
# # Find and Remove NaN values in Ratings
# # Challenge: How may rows have a NaN value (not-a-number) in the Ratings column?
# # Create DataFrame called df_apps_clean that does not include these rows.
# df_apps.isna().values.sum()
# df_apps_clean = df_apps.dropna()
# df_apps_clean.shape
#
#
# # Find and Remove Duplicates
# # Challenge: Are there any duplicates in data? Check for duplicates using the .duplicated() function.
# # How many entries can you find for the "Instagram" app?
# # Use .drop_duplicates() to remove any duplicates from df_apps_clean.
# df_apps_clean.duplicated()
# df_apps_clean[df_apps_clean.App == "Instagram"]
# df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
# df_apps_clean[df_apps_clean.App == "Instagram"]
# df_apps_clean.shape
#
#
# # Find Highest Rated Apps
# # Challenge: Identify which apps are the highest rated.
# # What problem might you encounter if you rely exclusively on ratings alone to determine the quality of an app?
# df_apps_clean.sort_values('Rating', ascending=False).head()
#
#
# # Find 5 Largest Apps in terms of Size (MBs)
# # Challenge: What's the size in megabytes (MB) of the largest Android apps in the Google Play Store.
# # Based on the data, do you think there could be limit in place or can developers make apps as large as they please?
# df_apps_clean.sort_values('Size_MBs', ascending=False).head()
#
#
# # Find the 5 App with Most Reviews
# # Challenge: Which apps have the highest number of reviews? Are there any paid apps among the top 50?
# df_apps_clean.sort_values('Reviews', ascending=False).head()
# df_apps_clean.sort_values('Reviews', ascending=False).head(50)
#
#
# # Plotly Pie and Donut Charts - Visualise Categorical Data: Content Ratings
# ratings = df_apps_clean.Content_Rating.value_counts()
# print(ratings)
#
# fig = px.pie(
#     labels=ratings.index,
#     values=ratings.values,
#     title='Content Ratings',
#     names=ratings.index,
#     hole=0.6
# )
# fig.update_traces(textposition='outside', textinfo='percent+label')
# fig.show()
#
# # Numeric Type Conversion: Examine the Number of Installs
# # Challenge: How many apps had over 1 billion (that's right - BILLION) installations?
# # How many apps just had a single install?
# # Check the datatype of the Installs column.
# # Count the number of apps at each level of installations.
# # Convert the number of installations (the Installs column) to a numeric data type. Hint: this is a 2-step process.
# # You'll have make sure you remove non-numeric characters first.
# df_apps_clean.Installs.describe()
# df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
# df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
# df_apps_clean[['App', 'Installs']].groupby('Installs').count()
#
#
# # Find the Most Expensive Apps, Filter out the Junk, and Calculate a (ballpark) Sales Revenue Estimate
# # Let's examine the Price column more closely.
# # Challenge: Convert the price column to numeric data. Then investigate the top 20 most expensive apps in the dataset.
# # Remove all apps that cost more than $250 from the df_apps_clean DataFrame.
# # Add a column called 'Revenue_Estimate' to the DataFrame.
# # This column should hold the price of the app times the number of installs.
# # What are the top 10 highest grossing paid apps according to this estimate?
# # Out of the top 10 highest grossing paid apps, how many are games?
# df_apps_clean['Price'].describe()
# df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
# df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
# df_apps_clean['Price'].describe()
# df_apps_clean.sort_values('Price', ascending=False).head(10)
#
# # The most expensive apps sub $250
# df_apps_clean = df_apps_clean[df_apps_clean.Price < 250]
# df_apps_clean.sort_values('Price', ascending=False).head(10)
#
# # Highest Grossing Paid Apps (ballpark estimate)
# df_apps_clean['Revenue Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
# df_apps_clean.sort_values('Revenue Estimate', ascending=False).head(10)
#
#
# # Plotly Bar Charts & Scatter Plots: Analysing App Categories
# df_apps_clean.Category.nunique()
# top10_category = df_apps_clean.Category.value_counts()[:10]
# print(top10_category)
#
# # Vertical Bar Chart - Highest Competition (Number of Apps)
# bar = px.bar(
#     x = top10_category.index,
#     y = top10_category.values
# )
# bar.show()
#
# # Horizontal Bar Chart - Most Popular Categories (Highest Downloads)
# category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
# category_installs.sort_values('Installs', ascending=True, inplace=True)
# h_bar = px.bar(
#     x = category_installs.Installs,
#     y = category_installs.index,
#     orientation='h',
#     title='Category Popularity'
# )
# h_bar.update_layout(
#     xaxis_title='Number of Downloads',
#     yaxis_title='Category'
# )
# h_bar.show()
#
# # Category Concentration - Downloads vs. Competition
# # Challenge:
# # First, create a DataFrame that has the number of apps in one column and the number of installs in another:
# category_concentration = df_apps_clean.groupby('Category').agg({'App': pd.Series.count, 'Installs': pd.Series.sum})
# category_concentration.sort_values('Installs', ascending=True, inplace=True)
#
# scatter = px.scatter(
#     x = category_concentration.App,
#     y = category_concentration.Installs,
#     title='Categpry Concentration',
#     size=category_concentration.App,
#     hover_name=category_concentration.index,
#     color=category_concentration.Installs
# )
#
# scatter.update_layout(
#     xaxis_title='Number of Apps (Lower = More Concentrated)',
#     yaxis_title='Installs',
#     yaxis=dict(type='log')
# )
# scatter.show()
#
#
# # Extracting Nested Data from a Column
# # Challenge: How many different types of genres are there? Can an app belong to more than one genre?
# # Check what happens when you use .value_counts() on a column with nested values?
# # See if you can work around this problem by using the .split() function and the DataFrame's .stack() method.
# df_apps_clean.Genres.nunique()
# df_apps_clean.Genres.value_counts().sort_values(ascending=True)[:5]
# stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
# print(stack.shape)
#
# num_genres = stack.value_counts()
# print(num_genres)
#
#
# # Colour Scales in Plotly Charts - Competition in Genres
# # Challenge: Can you create this chart with the Series containing the genre data?
# # Try experimenting with the built in colour scales in Plotly. You can find a full list here.
# # Find a way to set the colour scale using the color_continuous_scale parameter.
# # Find a way to make the color axis disappear by using coloraxis_showscale.
# bar = px.bar(
#     x = num_genres.index[:15],
#     y = num_genres.values[:15],
#     hover_name=num_genres.index[:15],
#     color=num_genres.values[:15],
#     color_continuous_scale='Plasma',
# )
#
# bar.update_layout(
#     coloraxis_showscale=False,
#     xaxis_title='Genres',
#     yaxis_title='Number of Apps'
# )
# bar.show()
#
#
# # Grouped Bar Charts: Free vs. Paid Apps per Category
# df_apps_clean.Type.value_counts()
# df_free_vs_paid = df_apps_clean.groupby(['Category', 'Type'], as_index=False).agg({'App': pd.Series.count})
# df_free_vs_paid.head()
#
# # Challenge: Use the plotly express bar chart examples and the .bar() API reference to create this bar chart:
# # You'll want to use the df_free_vs_paid DataFrame that you created above that has the total number of
# # free and paid apps per category.
# # See if you can figure out how to get the look above by changing the categoryorder to 'total descending'
# # as outlined in the documentation here.
# bar = px.bar(
#     df_free_vs_paid,
#     title='Free VS Paid',
#     x='Category',
#     y='App',
#     color='Type',
#     barmode='group'
# )
# bar.update_layout(
#     xaxis={'categoryorder': 'total descending'},
#     yaxis=dict(type='log')
# )
# bar.show()
#
#
# # Plotly Box Plots: Lost Downloads for Paid Apps
# # Challenge: Create a box plot that shows the number of Installs for free versus paid apps.
# # How does the median number of installations compare? Is the difference large or small?
# # Use the Box Plots Guide and the .box API reference to create the following chart.
# box = px.box(
#     df_apps_clean,
#     x = 'Type',
#     y = 'Installs',
#     color = 'Type',
#     notched=True,
#     points='all',
#     title='How Many Downloads are Apps Giving Up?'
# )
# box.update_layout(
#     yaxis=dict(type='log')
# )
# box.show()
#
#
# # Plotly Box Plots: Revenue by App Category
# # Challenge: See if you can generate the chart below:
# # Looking at the hover text, how much does the median app earn in the Tools category?
# # If developing an Android app costs $30,000 or thereabouts,
# # does the average photography app recoup its development costs?
# # Hint: I've used 'min ascending' to sort the categories.
# df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
# box = px.box(df_paid_apps,
#              x='Category',
#              y='Revenue Estimate',
#              title='How Much Can Paid Apps Earn?')
#
# box.update_layout(xaxis_title='Category',
#                   yaxis_title='Paid App Ballpark Revenue',
#                   xaxis={'categoryorder': 'min ascending'},
#                   yaxis=dict(type='log'))
#
# box.show()
#
#
# # How Much Can You Charge? Examine Paid App Pricing Strategies by Category
# # Challenge: What is the median price price for a paid app?
# # Then compare pricing by category by creating another box plot.
# # But this time examine the prices (instead of the revenue estimates) of the paid apps.
# # I recommend using {categoryorder':'max descending'} to sort the categories.
# df_paid_apps.Price.median()
# box = px.box(df_paid_apps,
#              x='Category',
#              y="Price",
#              title='Price per Category')

# box.update_layout(xaxis_title='Category',
#                   yaxis_title='Paid App Price',
#                   xaxis={'categoryorder': 'max descending'},
#                   yaxis=dict(type='log'))

# box.show()


# # In this lesson we looked at how to:
# #
# # Pull a random sample from a DataFrame using .sample()
# #
# # How to find duplicate entries with .duplicated() and .drop_duplicates()
# #
# # How to convert string and object data types into numbers with .to_numeric()
# #
# # How to use plotly to generate beautiful pie, donut, and bar charts as well as box and scatter plots
