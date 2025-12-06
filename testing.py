import pandas as pd


csv_files = [
    "final-project-team-1/data/circuits.csv", "final-project-team-1/data/constructor_results.csv", "final-project-team-1/data/constructor_standings.csv", "final-project-team-1/data/constructors.csv",
    "final-project-team-1/data/driver_standings.csv", "final-project-team-1/data/drivers.csv", "final-project-team-1/data/lap_times.csv", "final-project-team-1/data/pit_stops.csv",
    "final-project-team-1/data/qualifying.csv", "final-project-team-1/data/races.csv", "final-project-team-1/data/results.csv", "final-project-team-1/data/seasons.csv",
    "final-project-team-1/data/sprint_results.csv", "final-project-team-1/data/status.csv"
]

#Read all of the CSVs into a list of DataFrames
dfs = [pd.read_csv(file) for file in csv_files]

#check the .head() of the first CSV
print(dfs[0].head())

#Concatenate them side by side (columns), as I don't know precisely which columns to "merge on" here, with .merge, so .concat is used instead
concat_df = pd.concat(dfs, axis=1)
print(concat_df.head())


#Merge on meaningful keys

# Start with 'results' as the fact table
results = dfs[10]        #results.csv
drivers = dfs[5]         #drivers.csv
constructors = dfs[3]    #constructors.csv
races = dfs[9]           #races.csv
circuits = dfs[0]        #circuits.csv

#Merge results with drivers and constructors
merged_df = results.merge(drivers, on='driverId', how='left') \
                   .merge(constructors, on='constructorId', how='left') \
                   .merge(races, on='raceId', how='left') \
                   .merge(circuits, on='circuitId', how='left')

print(merged_df.head())


#Compute rolling averages

#Potential Example: Driver points rolling average over last 5 races
merged_df = merged_df.sort_values(['driverId', 'raceId'])
merged_df['driver_points_rolling_avg_5'] = merged_df.groupby('driverId')['points'] \
                                                   .rolling(5, min_periods=1).mean() \
                                                   .reset_index(level=0, drop=True)

print(merged_df[['driverId', 'raceId', 'points', 'driver_points_rolling_avg_5']].head(10))