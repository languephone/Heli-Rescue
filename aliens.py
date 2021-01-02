import csv, time

filename = 'enemy_map.csv'
with open(filename, encoding='utf-8-sig') as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get list of values from the file.
	aliens = []
	for row in reader:
		alien = {}
		for i in range(len(header_row)):
			alien[header_row[i]] = row[i]
		aliens.append(alien)

	print(aliens)

	start_values = []
	for alien in aliens:
		start_values.append(int(alien['Start']))
	print(start_values)

t0 = time.time()

max_x = max(start_values)
x = 0
while x <= max_x:
	print(x)
	for i in range(len(start_values.copy())):
		if start_values[i] <= x:
			print(f'Creating an alien with {aliens[i]} attributes')
			start_values.remove(start_values[i])
			break

	x += 1

t1 = time.time()

total_time = t1 - t0
print(total_time)