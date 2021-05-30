# -*- coding: utf-8 -*-
"""
Created on Sat May 29 11:40:20 2021

@author: MaryamHashemi
"""
#import libraries

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

####################################################################   
#read the text file
text_fil = open('hw20150120sodankyla.txt', 'r')
#read each line
lines=text_fil.readlines()

####################################################################
#creating the height matrix
height_matrix = np.zeros((6,24))
height_array=[]
for f in range(0,6):
    i=5*f+1
    heights = lines[i].split()
    height_array.append(heights)
 
      
i=-1
for lines in height_array:
    i=i+1
    height_matrix[i,:]=lines[4]


####################################################################
#creating the time matrix
text_fil = open('hw20150120sodankyla.txt', 'r')
#read each line
lines=text_fil.readlines()

times_matrix = np.zeros((6,24))
times_array=[]
for f in range(0,6):
    i=5*f+2
    times = lines[i].split()
    times_array.append(times)
 
      
i=-1
for lines in times_array:
    i=i+1
    for j in range (1,25):
        times_matrix[i,j-1]=lines[j]


####################################################################
#creating the zonal matrix
text_fil = open('hw20150120sodankyla.txt', 'r')
#read each line
lines=text_fil.readlines()

zonal_matrix = np.zeros((6,24))
zonal_array=[]
for f in range(0,6):
    i=5*f+3
    zonal = lines[i].split()
    zonal_array.append(zonal)
 
      
i=-1
for lines in zonal_array:
    i=i+1
    for j in range (1,25):
        zonal_matrix[i,j-1]=lines[j]
        
        
####################################################################
#creating the merid matrix

#read the text file
text_fil = open('hw20150120sodankyla.txt', 'r')
#read each line
lines=text_fil.readlines()

merid_matrix = np.zeros((6,24))
merid_array=[]
for f in range(0,6):
    i=5*f+4
    merid = lines[i].split()
    merid_array.append(merid)
 
      
i=-1
for lines in merid_array:
    i=i+1
    for j in range (1,25):
        merid_matrix[i,j-1]=lines[j]

####################################################################
#creating the points matrix

text_fil = open('hw20150120sodankyla.txt', 'r')
#read each line
lines=text_fil.readlines()

points_matrix = np.zeros((6,24))
points_array=[]
for f in range(0,6):
    i=5*f+5
    points = lines[i].split()
    points_array.append(points)
 
      
i=-1
for lines in points_array:
    i=i+1
    for j in range (2,26):
        points_matrix[i,j-2]=lines[j]
        
        
        
        
##################################################################################################### 
##################################ploting part#################################
#Zonal Wind Velocity as a Function of Time and Altitude

x = height_matrix
y = times_matrix
z = zonal_matrix



#x axis is zonal wind velocity, y axis is time, and color-map indicates height (altitude)
plt.figure(figsize=(30,25))
plt.title("Zonal Wind Velocity as a Function of Time and Altitude", fontsize='14')	#title
plt.scatter(z,y,c=x, cmap="jet",marker='o',linewidths=11)	#plot the points
plt.xticks(np.arange(-60, 1000, step=50))
plt.yticks(np.arange(0, 25, step=1))
plt.colorbar(label="Altitude (km)", orientation="vertical")
plt.xlabel("Zonal Wind Velocity (m/s)",fontsize='11')	#adds a label in the x axis
plt.ylabel("Time (h)",fontsize='11')	#adds a label in the y axis
plt.savefig('Zonal Wind Velocity, x axis= zonal wind, y axis= time.png')	#saves the figure in the present directory
plt.show()


#x axis is time, y axis is height (altitude), and colormap indicates zonal wind velocity
plt.figure(figsize=(30,25))
plt.title("Zonal Wind Velocity as a Function of Time and Altitude", fontsize='11')	
plt.scatter(y,x,c=z, cmap="jet",marker='o',linewidths=11)	#plot the points
plt.yticks(np.arange(80, 100, step=1))
plt.xticks(np.arange(0, 25, step=1))
plt.colorbar(label="Zonal Wind Velocity (m/s)", orientation="vertical")
plt.xlabel("Time (h)",fontsize='11')	#adds a label in the x axis
plt.ylabel("Altitude (km)",fontsize='11')	#adds a label in the y axis
plt.savefig('Zonal Wind Velocity, x axis= time, y axis= altitude.png')	#saves the figure in the present directory
plt.show()



#x axis is height (altitude),y axis is time, and colormap indicates zonal wind velocity
plt.figure(figsize=(30,25))
plt.title("Zonal Wind Velocity as a Function of Time and Altitude", fontsize='11')
plt.scatter(x,y,c=z, cmap="jet",marker='o',linewidths=11)	#plot the points
plt.xticks(np.arange(80, 100, step=1))
plt.yticks(np.arange(0, 25, step=1))
plt.colorbar(label="Zonal Wind Velocity (m/s)", orientation="vertical")
plt.xlabel("Altitude (km)",fontsize='11')	#adds a label in the x axis
plt.ylabel("Time (h)",fontsize='11')	#adds a label in the y axis
plt.savefig('Zonal Wind Velocity, x axis= altitude,y axis= time.png')	#saves the figure in the present directory
plt.show()


#x axis is zonal wind volecity,y axis is height (alititude), and colormap indicates time
plt.figure(figsize=(30,25))
plt.title("Zonal Wind Velocity as a Function of Time and Altitude", fontsize='11')
plt.scatter(z,x,c=y, cmap="jet",marker='o',linewidths=11)	#plot the points
plt.yticks(np.arange(80, 100, step=5))
plt.xticks(np.arange(-60, 1000, step=50))
plt.colorbar(label="time", orientation="vertical")
plt.xlabel("wind",fontsize='11')	#adds a label in the x axis
plt.ylabel("altitude",fontsize='11')	#adds a label in the y axis
plt.savefig('Zonal Wind Velocity, x axis= zonal wind volecity,y axis= alititude.png')	#saves the figure in the present directory
plt.show()



##################################################################################################### 
##################################ploting part#################################


#Meridional Wind Velocity as a Function of Time and Altitude

#x axis is Meridional wind volecity, y axis is time, and colormap indicates height (alititude)
plt.figure(figsize=(30,25))
plt.title("Meridional Wind Velocity as a Function of Time and Altitude", fontsize='14')	#title
plt.scatter(z,y,c=x, cmap="jet",marker='o',linewidths=11)	#plot the points
plt.xticks(np.arange(-60, 1000, step=50))
plt.yticks(np.arange(0, 25, step=1))
plt.colorbar(label="Altitude (km)", orientation="vertical")
plt.xlabel("Meridional Wind Velocity (m/s)",fontsize='11')	#adds a label in the x axis
plt.ylabel("Time (h)",fontsize='11')	#adds a label in the y axis
plt.savefig('Meridional Wind Velocity, x axis= Meridional wind, y axis= time.png')	#saves the figure in the present directory
plt.show()


#x axis is time, y axis is height (alititude), and colormap indicates Meridional wind volecity
plt.figure(figsize=(30,25))
plt.title("Meridional Wind Velocity as a Function of Time and Altitude", fontsize='11')	
plt.scatter(y,x,c=z, cmap="jet",marker='o',linewidths=11)	#plot the points
plt.yticks(np.arange(80, 100, step=5))
plt.xticks(np.arange(0, 25, step=1))
plt.colorbar(label="Wind", orientation="vertical")
plt.xlabel("time",fontsize='11')	#adds a label in the x axis
plt.ylabel("alititude (h)",fontsize='11')	#adds a label in the y axis
plt.savefig('Meridional Wind Velocity, x axis= time, y axis= alititude.png')	#saves the figure in the present directory
plt.show()



#x axis is height (alititude),y axis is time, and colormap indicates Meridional wind volecity
plt.figure(figsize=(30,25))
plt.title("Meridional Wind Velocity as a Function of Time and Altitude", fontsize='11')
plt.scatter(x,y,c=z, cmap="jet",marker='o',linewidths=11)	#plot the points
plt.xticks(np.arange(80, 100, step=5))
plt.yticks(np.arange(0, 25, step=1))
plt.colorbar(label="Wind", orientation="vertical")
plt.xlabel("altitude",fontsize='11')	#adds a label in the x axis
plt.ylabel("time",fontsize='11')	#adds a label in the y axis
plt.savefig('Meridional Wind Velocity, x axis= alititude,y axis= time.png')	#saves the figure in the present directory
plt.show()


#x axis is Meridional wind volecity,y axis is height (alititude), and colormap indicates time
plt.figure(figsize=(30,25))
plt.title("Meridional Wind Velocity as a Function of Time and Altitude", fontsize='11')
plt.scatter(z,x,c=y, cmap="jet",marker='o',linewidths=11)	#plot the points
plt.yticks(np.arange(80, 100, step=5))
plt.xticks(np.arange(-60, 1000, step=50))
plt.colorbar(label="time", orientation="vertical")
plt.xlabel("wind",fontsize='11')	#adds a label in the x axis
plt.ylabel("altitude",fontsize='11')	#adds a label in the y axis
plt.savefig('Meridional Wind Velocity, x axis= Meridional wind volecity,y axis= alititude.png')	#saves the figure in the present directory
plt.show()

