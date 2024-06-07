import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your dataset
df = pd.read_csv('D:\code\HiSCoD\db_hiscod_csv_v1_en.csv')

# Group data by year and region, and calculate the number of conflicts for each group
conflicts_by_year_region = df.groupby(['year', 'admin_level_1']).size().reset_index(name='conflict_count')

# Plot the trend of conflict counts in different regions of Europe
for region in conflicts_by_year_region['admin_level_1'].unique():
    region_data = conflicts_by_year_region[conflicts_by_year_region['admin_level_1'] == region]
    plt.plot(region_data['year'], region_data['conflict_count'], label=region)

plt.xlabel('Year')
plt.ylabel('Conflict Count')
plt.title('Conflict Count Trend in Different European Regions')

# Adjust the size of the legend
plt.legend(fontsize='small', bbox_to_anchor=(1.05, 1), loc='upper left', ncol=1)

plt.show()

# Classify conflicts by type and calculate the number of conflicts every decade
df['decade'] = (df['year'] // 10) * 10
conflicts_by_decade_type = df.groupby(['decade', 'riot_type_hiscod']).size().reset_index(name='conflict_count')

# Find the most prominent conflict type in each decade
most_prominent_conflicts = conflicts_by_decade_type.loc[conflicts_by_decade_type.groupby('decade')['conflict_count'].idxmax()]
print(most_prominent_conflicts)

# Plot a bar chart of the most prominent conflict type in each decade
plt.figure(figsize=(10, 6))
plt.bar(most_prominent_conflicts['decade'].astype(str), most_prominent_conflicts['conflict_count'], color='skyblue')
plt.xlabel('Decade')
plt.ylabel('Conflict Count')

# Adjust the size of the x-axis tick labels
plt.xticks(fontsize='small', rotation=75)
plt.title('Most Prominent Conflict Type in Each Decade')
plt.show()

# Convert the year to decade and century intervals
df['decade'] = (df['year'] // 10) * 10
df['century'] = (df['year'] // 100) * 100

# Classify conflicts by type and calculate the number of conflicts every decade and every century
conflicts_by_decade_type = df.groupby(['decade', 'riot_type_hiscod']).size().reset_index(name='conflict_count')
conflicts_by_century_type = df.groupby(['century', 'riot_type_hiscod']).size().reset_index(name='conflict_count')

# Find the most prominent conflict type in each decade and each century
most_prominent_conflicts_decade = conflicts_by_decade_type.loc[conflicts_by_decade_type.groupby('decade')['conflict_count'].idxmax()]
most_prominent_conflicts_century = conflicts_by_century_type.loc[conflicts_by_century_type.groupby('century')['conflict_count'].idxmax()]

# Output the results
print('Most prominent conflict type in each decade:')
print(most_prominent_conflicts_decade)
print('\nMost prominent conflict type in each century:')
print(most_prominent_conflicts_century)

# Output all types of conflicts
print('\nAll types of conflicts:')
print(df['riot_type_hiscod'].unique())

conflicts_by_type = df['riot_type_hiscod'].value_counts()
plt.figure(figsize=(10, 6))
plt.pie(conflicts_by_type.values, labels=conflicts_by_type.index, autopct='%1.1f%%')
plt.title('Pie Chart of Conflict Types')
plt.show()