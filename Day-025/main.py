import pandas as pd
import csv


def f_to_c(temp):
    return (temp - 32) * 5 / 9


def c_to_f(temp):
    return (temp * 9 / 5) + 32


#data_file = 'weather_data.csv'
#
#data = pd.read_csv(data_file)
#
#temps = data['temp'].to_list()
#
#print(temps)
#
#print("\nAverage Temperateure")
#print(data['temp'].mean())
#
#print("\nMax Temp")
#print(data['temp'].max())
#
#
#print(data[data.day == 'Monday'])

#print(data[data.temp == data.temp.max()])
#
#print(c_to_f(data.temp.max()))
#print(c_to_f(int(data[data.day == "Monday"].temp)))

data_file = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'

data = pd.read_csv(data_file)

colors = ['Cinnamon', 'Gray', 'Black']
sq_count = []

for color in colors:
    #print(f"{color:20} {data[data['Primary Fur Color'] == color]['Unique Squirrel ID'].count()}")
    sq_count.append(data[data['Primary Fur Color'] == color]['Unique Squirrel ID'].count())

sq_data = pd.DataFrame({'Color': colors, 'Count': sq_count})

print(sq_data)
sq_data.to_csv('squirrel_counts.csv')