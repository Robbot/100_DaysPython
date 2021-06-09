# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
import pandas
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
data = pandas.read_csv("weather_data.csv")
# temp_list = (data["temp"]).to_list()
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
# print((data["temp"]).mean())
# print((data["temp"]).max())
# print(data.temp.max())

print(data[data.temp == data.temp.max()])
