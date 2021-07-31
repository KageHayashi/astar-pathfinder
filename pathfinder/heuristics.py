from math import sqrt

def calculate_manhanttan_heuristics(current_cell, finish):
	return abs(current_cell.col - finish.col) + abs(current_cell.row - finish.row)

def calculate_diagonal_heuristics(current_cell, finish):
	return max(abs(current_cell.col - finish.col), abs(current_cell.row - finish.row))

def calculate_euclidean_heuristics(current_cell, finish):
	return sqrt((current_cell.col - finish.col)**2 + (current_cell.row - finish.row)**2)