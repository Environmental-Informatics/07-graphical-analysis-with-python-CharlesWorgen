#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2020/4/27
by Charles Huang

Lab7 - Graphical Analysis with Python
The program should accept command line options with both complete input and
output filenames, then import data from the given file, generating three plots
in one figure, then ouput it as a pdf file with given name. When the code is 
first written, the file Tippecanoe_River_at_Ora.Annual_Metrics.txt is used.
Therefore, variable TROA is named after it.
"""


import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

#Import data
data = pd.read_csv("all_month.csv")
EQ = data.dropna(how='any') #Dropping missing value

#histogram of earthquake magnitude.
#Skew to right, meaning only small earthquake happened, 
#no earthquake larger than Mg. = 4
#bin size should be smaller than 1, and range from 0 to 4 for better display
plt.figure(1)
n, bins, patches = plt.hist(EQ['mag'], bins=10, range= (0,10), facecolor='r')
plt.xlabel('Magnitude')
plt.ylabel('Counts')
plt.title(r'Histogram of Earthquake Magnitude')
plt.savefig('Histogram_Earthquake_Magnitude.jpg')

#KDE plot
#Kernel type and width are "scott" as default
#Almost 60% of the reported earthquakes are around Mg. = 1
plt.figure(2)
EQ['mag'].plot.kde()
plt.xlabel('Magnitude')
plt.title(r'KDE plot of Earthquake Magnitude')
plt.savefig('KDE_Earthquake_Magnitude.jpg')

#latitude versus longitude for all earthquakes
#most are distributed around (16-62N, 50-180 W), most concentrated
#around (30-50N,105-128W),some outlier are close to (50N, 180 E)
plt.figure(3)
plt.plot(EQ['longitude'],EQ['latitude'],'ro')
plt.axis([-200, 200, 15, 65])
plt.grid(linestyle='-')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title(r'Location for all Earthquakes')
plt.savefig('Location_Earthquake.jpg')

#normalized cumulative distribution plot of earthquake depths
# about 80% of the earthquake happened above 10km depth, and 97% happened above
# 30km depth, and start to end at around 63km depth (there are few more outliers
# all the way up to 140 km).
plt.figure(4)
n, bins, patches = plt.hist(EQ['depth'], density=True,cumulative=True,
                            bins=85, range=(-5,80),facecolor='b',
                            histtype='step')
plt.xlabel('Depth(km)')
plt.ylabel('%')
plt.title(r'Normalized cumulative plot of earthquake depths')
plt.savefig('Norm_Cumulative_Depth.jpg')

#scatter plot of earthquake magnitude with depth
# It seems like shallow depth generally have earthquakes with smaller magnitude,
# when those with larger magnitude (> 3) can happen in shallow layer but more
# likely in the greater depth
plt.figure(5)
plt.scatter(EQ['mag'],EQ['depth'])
plt.xlabel('Magnitude')
plt.ylabel('Depth(km)')
plt.title(r'Earthquakes Depth vs. Magnitude')
plt.axis([0,4.5,-5,140])
plt.savefig('Depth_Magnitude.jpg')

# Q-Q plot of the earthquake magnitudes
#The Q-Q plot is assuming the earthquake magnitudes should be normal distributed
#According to the plot, data points are close to the straight line, which means
#that they are normal distributed
plt.figure(6)
stats.probplot(EQ['mag'], plot=plt)
plt.title(r'Q-Q plot of earthquake magnitudes')
plt.savefig('QQ_Magnitude.jpg')