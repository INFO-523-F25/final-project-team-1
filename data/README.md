# Data
-   **[FastF1]**: Provides access to F1 lap timing, car telemetry and position, tyre data, weather data, the event schedule and session results. Official documentation can be found [here](https://docs.fastf1.dev/index.html)

# Overview over the available data

| **Topic** | **Data** | **References** |
|------------|-----------|----------------|
| **Event Schedule** | event names, countries, locations, dates, scheduled starting times,… (previous and current season including upcoming events) | [`events`](https://docs.fastf1.dev/events.html#module-fastf1.events), [`get_event_schedule()`](https://docs.fastf1.dev/fastf1.html#fastf1.get_event_schedule), [`get_event()`](https://docs.fastf1.dev/fastf1.html#fastf1.get_event) |
| **Results** | driver names, team names, finishing and grid positions, points, finishing status,… | [`SessionResults`](https://docs.fastf1.dev/core.html#fastf1.core.SessionResults), [`DriverResult`](https://docs.fastf1.dev/core.html#fastf1.core.DriverResult) |
| **Timing Data** | sector times, lap times, pit stops, tyre data and much more | [`laps`](https://docs.fastf1.dev/core.html#fastf1.core.Session.laps), [`Laps`](https://docs.fastf1.dev/core.html#fastf1.core.Laps) |
| **Track Status** | flags, safety car | [`track_status`](https://docs.fastf1.dev/core.html#fastf1.core.Session.track_status) |
| **Session Status** | started, finished, finalized | [`session_status`](https://docs.fastf1.dev/core.html#fastf1.core.Session.session_status) |
| **Race Control Messages** | investigations, penalties, restart announcements,… | [`race_control_messages`](https://docs.fastf1.dev/core.html#fastf1.core.Session.race_control_messages) |
| **Telemetry** | speed, rpm, gear, normalized track position,… | [`Telemetry`](https://docs.fastf1.dev/core.html#fastf1.core.Telemetry), [`get_car_data()`](https://docs.fastf1.dev/core.html#fastf1.core.Lap.get_car_data) |
| **Track Markers** | corner numbers, marshall sectors, marshall lights | [`get_circuit_info()`](https://docs.fastf1.dev/core.html#fastf1.core.Session.get_circuit_info), [`Circuit Information`](https://docs.fastf1.dev/circuit_info.html#circuit-info) |
| **Ergast API** | all endpoints that are provided by Ergast | [`Ergast API Interface`](https://docs.fastf1.dev/ergast.html#ergast) |


# Codebook for Dataset
There are numerous variables and data points available in this API, and this information will be expanded and updated as the project progresses.

## Variable Names and Descriptions:

-   **variable**: 
** There are numerous variables and data points available in this API, and this information will be expanded and updated as the project progresses.

## Data Types:

-   **Column**:
There are numerous variables and data points available in this API, and this information will be expanded and updated as the project progresses.



