clear()
world_size = get_world_size()
def setup_pumpkin():
	for x in range(world_size):
		for y in range(world_size):
			till()
			plant(Entities.Pumpkin)
			move(North)
		move(East)
			
def get_megapumpkin():
	while True:
		for i in range(5):
			do_a_flip()
		count = 0
		for x in range(world_size):
			for y in range(world_size):
				if get_entity_type() != Entities.Pumpkin:
					plant(Entities.Pumpkin)
				else:
					count += 1
				move(North)
			move(East)
		if count == 25:
			harvest()
			break
		
			
	
setup_pumpkin()
get_megapumpkin()
while True:
	do_a_flip()

first = True

pumpkin = True
while True:
	for x in range(world_size):
		to_plant = Entities.Grass
		to_till = False or pumpkin
		if x == 1 or x == 2:
			to_plant = Entities.Bush
		if x == 3:
			to_plant = Entities.Carrot
			to_till = True
		for y in range(world_size):
			if to_till and first:
				till()
			if can_harvest():
				harvest()
			if pumpkin:
				plant(Entities.Pumpkin)
			elif to_plant == Entities.Bush and (x + y) % 2 == 1:
				plant(Entities.Tree)
			else:
				plant(to_plant)
			water_level = get_water()
			if water_level < 1.0:
				use_item(Items.Water)
			move(North)
		move(East)
	first = False
	