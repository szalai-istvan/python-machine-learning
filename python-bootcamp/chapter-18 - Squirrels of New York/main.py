# This little project is basically playing around with pandas
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
furColors = data['Primary Fur Color']
furColorValues = furColors.unique()

furColorCount = {}
for color in furColorValues:
    furColorCount[color] = len(data[data['Primary Fur Color'] == color])

print(furColorCount)

colors = []
count = []
table = {}

for key in furColorCount:
    colors.append(key)
    count.append(furColorCount[key])

table['Fur Color'] = colors
table['Count'] = count
print(table)

df = pandas.DataFrame(table)
df = df[pandas.notna(df['Fur Color'])]

print(df)

df.to_csv('out.csv')