import sys

chrome_scale = [
		"C1", "#", "D1", "#", "E1", "F1", "#", "G1", "#", "A1", "#", "B1",
        "C2", "#", "D2", "#", "E2", "F2", "#", "G2", "#", "A2", "#", "B2",
        "C3", "#", "D3", "#", "E3", "F3", "#", "G3", "#", "A3", "#", "B3",
        "C4", "#", "D4", "#", "E4", "F4", "#", "G4", "#", "A4", "#", "B4",
        "C5", "#", "D5", "#", "E5", "F5", "#", "G5", "#", "A5", "#", "B5",
        "C6", "#", "D6", "#", "E6", "F6", "#", "G6", "#", "A6", "#", "B6",
        "C7", "#", "D7", "#", "E7", "F7", "#", "G7", "#", "A7", "#", "B7",
        "C8", "#", "D8", "#", "E8", "F8", "#", "G8", "#", "A8", "#", "B8"
        ]
a3 = chrome_scale.index("A3")

toneArray = []
filepath = str(sys.argv[1])  
with open(filepath) as f: 
	my_line = f.readline() 
	
	while my_line:
		accedental = ''
		duration = 0.000
		whole = 1.000
		duration_key = my_line[len(my_line)-4:-1]
		if duration_key == "1/8":
			duration = whole * 0.125
		elif duration_key == "1/4":
			duration =  whole * 0.25
		elif duration_key == "3/8":
			duration = whole * 0.375
		elif duration_key == "1/2":
			duration = whole * 0.5
		elif duration_key == "3/4":
			duration = whole * 0.75
		else:
			duration = whole


		if my_line[0] == "_":
			freqhz = 0
		else:
			if my_line[1] == 'b' or my_line[1] == '#':
				accedental = my_line[1]
				note = my_line[0] + my_line[2]
			else:
				accedental = ''
				note = my_line[0] + my_line[1]

			if chrome_scale.index(note) <= a3:
				distance = a3 - chrome_scale.index(note)
				if accedental == 'b':
					distance += 1
				elif accedental == '#':
					distance -= 1
				freqhz = round(440 * pow(2, (distance / 12.0)))
			else:
				distance = chrome_scale.index(note) - a3
				if accedental == 'b':
					distance -= 1
				elif accedental == '#':
					distance += 1
				freqhz = round(440 * pow(2, (distance / 12.0)))
		toneArray.append([freqhz, duration])
		my_line = f.readline()


for item in toneArray:
	print(item[0], item[1])

