# -*- coding: utf-8 -*-
# PPI/DPI calculation for mobile phones, screens

def PPI_calculation(resolution_x, resolution_y, screen_diagonal):
	import math
	resolution_x = float(resolution_x)
	resolution_y = float(resolution_y)
	return resolution_y / (screen_diagonal * math.cos(math.atan(resolution_x / resolution_y)))
	
print PPI_calculation(800, 480, 3.1)
