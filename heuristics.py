def calculate_manhanttan_heuristics(current_cell, end_cell):
	return abs(current_cell.i - end_cell.i) + abs(current_cell.j - end_cell.j)