# Practical Materials

## Preparation Activity

The goal of this activity is to ensure that all participants have a working account on the Digital Earth Australia Sandbox and that they can run Python notebooks.
The activity also serves to introduce participants to some basic Python, which has been designed to introduce concepts that will arise during the practical acvities.

To run the activity, have participants upload the resources below into the Digital Earth Australia Sandbox.
Then, have the participants run the intro_to_python.ipynb notebook, followed by the more_python.ipynb notebook. 
The error_guide.ipynb notebook serves as a resource, which may be useful for participants to review if they encounter errors during any of the activities.

### Resources

- intro_to_python.ipynb
- more_python.ipynb
- error_guide.ipynb

## Practical 1 - Logging Site Selection

The goal of this practical is to get the participant familiar with data collected on logging activities. 
By the end of the activity, the participant will have learned to:

- load geospatial data files and explore their contents.
- clean, explore and filter all available data to identify different types of logging events.
- export a collection of events that can be compared with satellite imagery.

To run the activity, have participants upload the resources below into the Digital Earth Australia Sandbox.
Then, have the participants run the prac1_logging_site_selection.ipynb notebook.

### Resources

- prac1_logging_site_selection.ipynb
- LOG_SEASON.gpkg
- LOG_SEASON_column_names.txt
- polygon_attribute.png

## Practical 2 - Logging Site Monitoring

The goal of this practical is for the participant to load satellite data for logging events selected during Practical 1 and analyse patterns in the normalised difference vegetation index for the site over time. 
By the end of the activity, the participant will have learned to:

- select specific rows from a table of geospatial data.
- load satellite data for the time and location corresponding to a given logging event.
- review satellite data, both as images and as timeseries.
- 
To run the activity, have participants upload the resources below into the Digital Earth Australia Sandbox.
If they have already run Practical 1, they should already have the LOG_SEASON_FILTERED.gpkg file.
Then, have the participants run the prac2_logging_site_monitoring.ipynb notebook.

### Resources

- prac2_logging_site_monitoring.ipynb
- LOG_SEASON_FILTERED.gpkg
- plotting_functions.py