import csv

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
