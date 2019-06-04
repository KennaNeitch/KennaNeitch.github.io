numbers = [1,2,3,4,5]
data = []
for number in numbers:
    data.append(number - 10)

data

print(data)

number2 = [1,2,3,4,5]
data2 = []
for number in numbers:
    data2 = [number - 10 for number in numbers]

data2

print(data2)
