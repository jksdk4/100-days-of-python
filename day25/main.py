# # with open("weather_data.csv", "r") as wd:
# #     data = wd.readlines()
#
# # import csv
# #
# # with open("weather_data.csv") as wd:
# #     data = csv.reader(wd)   # csv object, loop for values
# #     temperatures = []
# #
# #     for row in data:
# #         if row[1] != "temp":
# #           temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # DataFrame to object
# data_dict = data.to_dict()
# print(data_dict)
#
# # List from Series object
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# avg = data['temp'].mean()
# max_temp = data['temp'].max()
# print(avg.round(2))
# print(max_temp)
#
# # get row data
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# print(monday.condition)
# print((monday.temp[0] * 9/5) + 32)  # using the index gets literal value rather than Series
#
# data_dict = {
#     "students": ['Amy', 'James', 'Angela'],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_count.csv")
