number = int(input('Enter number to print multiplication of table:'))

print('the multiplication of table:', number)

for count in range(1, 11):
	print(number, 'x', count, '=', number * count)
