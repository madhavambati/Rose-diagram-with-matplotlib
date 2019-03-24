import pandas as pd                             #for accessing DataFrames
import matplotlib.pyplot as plt                 #for graph plotting using class pyplot 
from math import radians                        #standard maths library
import numpy as np                              #for numpy.ndarray
from matplotlib.lines import Line2D             #for circle plotting in legend



#Data Manipulation
data = pd.read_excel('C:/Users/Madhava Ambati/Documents/Python/Scripts/file.xlsx')
data = data.fillna(0)
data = data[3:]
#print(data)

color = data['Unnamed: 2'].iloc[14:].values                      #list for color (represents PM10 conc)
wind_direction_angle = data['Unnamed: 44'].iloc[14:].values      #list for wind direction in angle (represents wind_direction)

wind_direction = []                                              #list for wind direction in radians
size = []                                                        #list for size of the points (represents Pt(fg/m3))
size_true = []


for angle in wind_direction_angle:                                
	wind_direction.append(radians(angle))
for s in data['Unnamed: 10'].iloc[14:].values:
	size.append(int(s*10)*2)
	size_true.append(int(s))


wind_speed = data['Unnamed: 45'].iloc[14:]                       #list for wind speed



print(wind_direction_angle)
print(wind_speed)
print(size_true)
print(color)



#code for plotting
ax = plt.subplot(111,polar=True)
scatter = ax.scatter(x=wind_direction, y=wind_speed, s=size, c=color, cmap='jet',edgecolors='Black', linewidths=0.7, alpha= 0.9)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
colorbar = plt.colorbar(scatter,cmap='jet')                      #for colorbar
colorbar.ax.set_xlabel('PM10 Conc(µg/m3)',labelpad=-465)         #for colorbar-label


legend_elements_1 = []
for radius in range(0,100,20):
	legend_elements_1.append(Line2D([0], [0], marker='o', color='w', label=str(radius/20),markerfacecolor='b', markersize=radius**0.5, alpha = 0.7))


legend_elements_2 = []
for radius in range(100,max(size)+150,150):
	if(radius < max(size)):

		legend_elements_2.append(Line2D([0], [0], marker='o', color='w', label=str(radius/20),markerfacecolor='b', markersize=radius**0.5, alpha = 0.7))
	if(radius >= max(size)):
		legend_elements_2.append(Line2D([0], [0], marker='o', color='w', label="  "+str(radius/20)+'  Pt/Rh',markerfacecolor='b', markersize=radius**0.5, alpha = 0.7))

legend_elements = legend_elements_1 + legend_elements_2

plt.legend(handles = legend_elements, loc='lower center',bbox_to_anchor=(0.50, -0.13), ncol = len(legend_elements), frameon=False)
#plt.xlabel('Radius')
plt.show()




