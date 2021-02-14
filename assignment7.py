order = ["pizza", "dosa", "burger", "ice-cream", "coffee"]

menu_card = { "pizza" : 500,
"dosa" : 100,
"burger" : 250,
"ice-cream" : 150,
"coffee" : 50
}

total = 0
for orders in order:
  total = total + menu_card[orders]

print(total)

output

#1050
