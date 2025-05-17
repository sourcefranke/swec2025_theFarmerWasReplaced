clear()
first = False
while True:
	for x in range(3):
		to_plant = Entities.Grass
		to_till = False
		if x == 1 or x == 2:
			to_plant = Entities.Bush
		if x == 3:
			to_plant = Entities.Carrot
			to_till = True
		for y in range(3):
			if to_till and first:
				till()
			if can_harvest():
				harvest()
			plant(to_plant)
			move(North)
		move(West)
	first = False
	