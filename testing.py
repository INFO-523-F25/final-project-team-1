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