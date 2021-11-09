import pandas as pd
import matplotlib.pyplot as plt

# Challenge: How many different colours does the LEGO company produce? Read the colors.csv file in the data folder
# and find the total number of unique colours. Try using the .nunique() method to accomplish this.
colors_df = pd.read_csv('data/colors.csv')
colors_df['name'].nunique()

# Challenge: Find the number of transparent colours where is_trans == 't' versus the number of opaque colours where
# is_trans == 'f'. See if you can accomplish this in two different ways.
colors_df['is_trans'].value_counts()
colors_df.groupby('is_trans').count()

# The sets.csv data contains a list of sets over the years and the number of parts that each of these sets contained.
# Challenge: Read the sets.csv data and take a look at the first and last couple of rows.
sets_df = pd.read_csv('data/sets.csv')
sets_df.head()
sets_df.tail()

# Challenge: In which year were the first LEGO sets released and what were these sets called?
sets_df.sort_values('year').head()

# Challenge: How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer
# in the year the company started?
sets_df[sets_df['year'] == 1949]

# Challenge: Find the top 5 LEGO sets with the most number of parts.
sets_df.sort_values('num_parts', ascending=False).head()

# Challenge: Use .groupby() and .count() to show the number of LEGO sets released year-on-year.
# How do the number of sets released in 1955 compare to the number of sets released in 2019?
sets_df.sort_values('year').groupby('year').count()
sets_by_year = sets_df.groupby('year').count()
sets_by_year['set_num'].head()

# Challenge: Show the number of LEGO releases on a line chart using Matplotlib.
# Note that the .csv file is from late 2020, so to plot the full calendar years, you will have to exclude some data
# from your chart. Can you use the slicing techniques covered in Day 21 to avoid plotting the last two years?
# The same syntax will work on Pandas DataFrames.
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])

# Aggregate Data with the Python .agg() Function Let's work out the number of different themes shipped by year. This
# means we have to count the number of unique theme_ids per calendar year.
themes_by_year = sets_df.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
themes_by_year.head()
themes_by_year.tail()

# Challenge: Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e.,
# exclude 2020 and 2021).
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])

# Line Charts with Two Separate Axes
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='g')
ax2.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='b')

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Themes')

ax2.set_ylabel('Number of Sets')

# Challenge: Use the .groupby() and .agg() function together to figure out the average number of parts per set. How
# many parts did the average LEGO set released in 1954 compared to say, 2017?
parts_by_year = sets_df.groupby('year').agg({'num_parts': pd.Series.mean})
parts_by_year.rename(columns={'num_parts': 'average_num_parts'})
parts_by_year.head()
parts_by_year.tail()

# Scatter Plots in Matplotlib Challenge: Has the size and complexity of LEGO sets increased over time based on the
# number of parts? Plot the average number of parts over time using a Matplotlib scatter plot. See if you can use the
# scatter plot documentation before I show you the solution. Do you spot a trend in the chart?
plt.scatter(parts_by_year.index[:-2], parts_by_year.num_parts[:-2])


# Number of Sets per LEGO Theme LEGO has licensed many hit franchises from Harry Potter to Marvel Super Heros to many
# others. But which theme has the largest number of individual sets?
set_theme_count = sets_df['theme_id'].value_counts()
set_theme_count[:5]

# Database Schemas, Foreign Keys and Merging DataFrames The themes.csv file has the actual theme names. The sets .csv
# has theme_ids which link to the id column in the themes.csv.

# Challenge: Explore the themes.csv. How is it structured? Search for the name 'Star Wars'. How many ids correspond
# to this name in the themes.csv? Now use these ids and find the corresponding the sets in the sets.csv (Hint: you'll
# need to look for matches in the theme_id column)
themes_df = pd.read_csv('data/themes.csv')
themes_df.head()
themes_df[themes_df.name == "Star Wars"]
sets_df[sets_df.theme_id == 18]
sets_df[sets_df.theme_id == 209]
sets_df[sets_df.theme_id == 261]

# Merging (i.e., Combining) DataFrames based on a Key
set_theme_count = pd.DataFrame({
    'id': set_theme_count.index,
    'set_count': set_theme_count.values
})
set_theme_count.head()

merged_df = pd.merge(set_theme_count, themes_df, on='id')
merged_df[:3]

plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.ylabel('Number of Sets', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])


# Learning Points & Summary
# In this lesson we looked at how to:
#
# use HTML Markdown in Notebooks, such as section headings # and how to embed images with the <img> tag.
#
# combine the groupby() and count() functions to aggregate data
#
# use the .value_counts() function
#
# slice DataFrames using the square bracket notation e.g., df[:-2] or df[:10]
#
# use the .agg() function to run an operation on a particular column
#
# rename() columns of DataFrames
#
# create a line chart with two separate axes to visualise data that have different scales.
#
# create a scatter plot in Matplotlib
#
# work with tables in a relational database by using primary and foreign keys
#
# .merge() DataFrames along a particular column
#
# create a bar chart with Matplotlib












