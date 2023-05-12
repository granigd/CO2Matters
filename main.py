import pandas as pd
import matplotlib.pyplot as plt

# Data sourcing
# Load the first dataset from an external source
df_anomaly = pd.read_csv('https://datahub.io/core/global-temp/r/annual.csv')
# Load the second dataset from an external source
df_co2 = pd.read_csv('https://datahub.io/core/co2-ppm/r/co2-mm-mlo.csv')

# Data transformation
# Convert the date column in the first dataframe to a datetime object
df_anomaly['Date'] = pd.to_datetime(df_anomaly['Year'], format='%Y')
# Filter the first dataset to include only data from 1958 onwards
df_anomaly = df_anomaly[df_anomaly['Date'].dt.year >= 1959]
# Rename column
df_anomaly = df_anomaly.rename(columns={'Mean': 'Temp Anomaly'})

# extract the 2 sources into seperate dataframes
df_anomaly_GCAG = df_anomaly.loc[df_anomaly['Source'] == 'GCAG']
df_anomaly_GCAG = df_anomaly_GCAG[['Year', 'Temp Anomaly']]
df_anomaly_GCAG = df_anomaly_GCAG.rename(columns={'Temp Anomaly': 'Temp Anomaly GCAG'})

df_anomaly_GISTEMP = df_anomaly.loc[df_anomaly['Source'] == 'GISTEMP']
df_anomaly_GISTEMP = df_anomaly_GISTEMP[['Year', 'Temp Anomaly']]
df_anomaly_GISTEMP = df_anomaly_GISTEMP.rename(columns={'Temp Anomaly': 'Temp Anomaly GISTEMP'})

# Same thing for the second dataframe
df_co2['Date'] = pd.to_datetime(df_co2['Date'], format='%Y-%m-%d')
df_co2 = df_co2[df_co2['Date'].dt.year >= 1959]
# Rename the columns in the second dataset
df_co2 = df_co2.rename(columns={'Trend': 'Average CO2'})
# we are only interested in date and average
df_co2 = df_co2[['Date', 'Average CO2']]
# As the resolution of the first dataframe is yearly, we also convert the second dataframe to yearly average
yearly_average = df_co2.groupby(pd.PeriodIndex(df_co2['Date'], freq="Y"))['Average CO2'].mean()
yearly_average = pd.DataFrame({'Year': yearly_average.index, 'Average CO2': yearly_average.values})
yearly_average['Year'] = yearly_average['Year'].apply(lambda x: int(x.strftime("%Y")))


# Merge the two datasets on the Date column
df = pd.merge(df_anomaly_GISTEMP, yearly_average, on='Year')
df = pd.merge(df_anomaly_GCAG, df, on='Year')

# Data visualization GISTEMP
# Create a line plot of the global temperature anomaly and CO2 levels over time
fig, ax1 = plt.subplots()
ax1.plot(df['Year'], df['Temp Anomaly GISTEMP'], color='tab:red')
ax1.set_xlabel('Year')
ax1.set_ylabel('Global Temperature Anomaly GISTEMP (°C)', color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.plot(df['Year'], df['Average CO2'], color='tab:blue')
ax2.set_ylabel('CO2 Levels (ppm)', color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title('Global Temperature Anomaly (GISTEMP) and CO2 Levels Over Time')
plt.savefig('Global Temperature Anomaly (GISTEMP) and CO2 Levels Over Time')
plt.show()


# Data visualization GCAG
# Create a line plot of the global temperature anomaly and CO2 levels over time
fig, ax1 = plt.subplots()
ax1.plot(df['Year'], df['Temp Anomaly GCAG'], color='tab:red')
ax1.set_xlabel('Year')
ax1.set_ylabel('Global Temperature Anomaly GCAG (°C)', color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.plot(df['Year'], df['Average CO2'], color='tab:blue')
ax2.set_ylabel('CO2 Levels (ppm)', color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title('Global Temperature Anomaly (GCAG) and CO2 Levels Over Time')
plt.savefig('Global Temperature Anomaly (GCAG) and CO2 Levels Over Time')
plt.show()


# Machine-actionable data
# Save the merged dataset to a CSV file
df.to_csv('temp_anomaly_co2.csv', index=False)