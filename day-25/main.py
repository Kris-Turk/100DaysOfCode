# import csv

# with open("./weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("./weather_data.csv")
# print(data["temp"])


# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average = data.temp.mean()
# print(f"Average temp is: {average}")

# max = data.temp.max()
# print(max)


# print(data[data.day == "Monday"])

# print(data[data.temp == max])

# monday = data[data.day == "Monday"]
# fh = monday.temp.apply(lambda x: (9/5) * x + 32)
# print(fh)

#create Dataframe

# data_dict = {
#     "students": ["Kris","Sapho","Mike"],
#     "scores": [99,95,95]
# }


# df = pandas.DataFrame(data_dict)
# print(df)
# df.to_csv("./new_data.csv")


data = pandas.read_csv("./squirrels.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

        
counts = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray, black, cinnamon]
}

df = pandas.DataFrame(counts)
df.to_csv("./counts.csv")
    


