numbers = [1,1,1,2,3,3,3,4,4,4,4,5,5,5,5,5,6]

number_dictionary = {}

for number in numbers:
  if number in number_dictionary:
    number_dictionary[number] = number_dictionary[number] + 1 
  else:
    number_dictionary[number] = 1
print(number_dictionary)

output

#{1: 3, 2: 1, 3: 3, 4: 4, 5: 5, 6: 1}
