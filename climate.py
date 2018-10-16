
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


# In[3]:


import numpy as np
import pandas as pd


# In[4]:


import datetime as dt


# # Reflect Tables into SQLAlchemy ORM

# In[5]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func


# In[6]:


engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# In[7]:


inspector = inspect(engine)
inspector.get_columns('measurement')


# In[8]:


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# In[9]:


# We can view all of the classes that automap found
Base.classes.keys()


# In[10]:


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[11]:


# Create our session (link) from Python to the DB
session = Session(engine)


# # Exploratory Climate Analysis

# In[25]:


# Design a query to retrieve the last 12 months of precipitation data and plot the results

# Calculate the date 1 year ago from today
a = dt.datetime.now() - dt.timedelta(days=366)
a = dt.datetime.date(a)
print(a)
# Perform a query to retrieve the data and precipitation scores
mes =session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > a)
# Save the query results as a Pandas DataFrame and set the index to the date column
prcp_DF = pd.read_sql(mes.statement, session.bind)
prcp_DF.head()
# Sort the dataframe by date
prcp_DF = prcp_DF.sort_values('date')
prcp_DF['date'] = pd.to_datetime(prcp_DF['date'])
prcp_DF = prcp_DF.set_index('date')
prcp_DF.head()
prcp_DF.dropna(inplace=True)
prcp_DF.head()
# Use Pandas Plotting with Matplotlib to plot the data
ax = plt.subplot()
prcp_DF.plot(ax=ax)
# Rotate the xticks for the dates
ax.set_xticks = prcp_DF.index
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='red')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('red')
ax.set_ylabel('Precipitation')


# In[11]:


# Use Pandas to calcualte the summary statistics for the precipitation data


# In[12]:


# How many stations are available in this dataset?


# In[13]:


# What are the most active stations?
# List the stations and the counts in descending order.


# In[14]:


# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature most active station?


# In[15]:


# Choose the station with the highest number of temperature observations.
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram


# In[16]:


# Write a function called `calc_temps` that will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
print(calc_temps('2012-02-28', '2012-03-05'))


# In[17]:


# Use your previous function `calc_temps` to calculate the tmin, tavg, and tmax 
# for your trip using the previous year's data for those same dates.


# In[18]:


# Plot the results from your previous query as a bar chart. 
# Use "Trip Avg Temp" as your Title
# Use the average temperature for the y value
# Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)


# In[19]:


# Calculate the rainfall per weather station for your trip dates using the previous year's matching dates.
# Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation



# ## Optional Challenge Assignment

# In[20]:


# Create a query that will calculate the daily normals 
# (i.e. the averages for tmin, tmax, and tavg for all historic data matching a specific month and day)

def daily_normals(date):
    """Daily Normals.
    
    Args:
        date (str): A date string in the format '%m-%d'
        
    Returns:
        A list of tuples containing the daily normals, tmin, tavg, and tmax
    
    """
    
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    return session.query(*sel).filter(func.strftime("%m-%d", Measurement.date) == date).all()
    
daily_normals("01-01")


# In[21]:


# calculate the daily normals for your trip
# push each tuple of calculations into a list called `normals`

# Set the start and end date of the trip

# Use the start and end date to create a range of dates

# Stip off the year and save a list of %m-%d strings

# Loop through the list of %m-%d strings and calculate the normals for each date


# In[22]:


# Load the previous query results into a Pandas DataFrame and add the `trip_dates` range as the `date` index


# In[23]:


# Plot the daily normals as an area plot with `stacked=False`

