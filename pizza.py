import math
import sys
from copy import copy,deepcopy
sys.setrecursionlimit(10000)

header = 0

# Count number of ingredients in slice
def ingredients_count(row_init, col_init, row_end, col_end, matrix):
	# Result 0 -> Tomato 1 -> Mushroom
	result = [0, 0]
	i = row_init
	while i <= row_end:
		j = col_init
		while j <= col_end:
			if matrix[i][j] == 'T':
				result[0] = result[0] + 1
			else:
				result[1] = result[1] + 1
			j = j + 1
		i = i + 1
	return result

# Heuristic of the given solution
def heuristic(posible_solution, matrix):
	i = 0
	result = 0
	while i < len(posible_solution):
		result = result + ((posible_solution[i][2] - posible_solution[i][0] + 1) * (posible_solution[i][3] - posible_solution[i][1] + 1))
		i = i + 1
	return result

# Check if the solution is plausible
def check_solution(posible_solution, matrix):
	for k in posible_solution:
		if k[0] >= len(matrix) or k[1] >= len(matrix[0]) or k[2] >= len(matrix) or k[3] >= len(matrix[0]):
			return 0
	return 1

# Check if the number of ingredients is correct
def check_ingredients(posible_solution, matrix):
	for k in posible_solution:
		result = ingredients_count(k[0], k[1], k[2], k[3], matrix)
		if header[2] > result[0] or header[2] > result[1] or header[3] < result[0] + result[1]:
			return 0
	return 1

# Check if the slice is too big
def check_ingredients_count(posible_solution, matrix):
	for k in posible_solution:
		result = ingredients_count(k[0], k[1], k[2], k[3], matrix)
		if header[3] < result[0] + result[1]:
			return 0
	return 1

# Choose new slice to cut the solution
def choose_new_slice(posible_solution, matrix):
	i = 0
	while i < len(matrix[0]):
		j = 0
		while j < len(matrix):
			can = 1
			for k in posible_solution:
				if (j >= k[0] and j <= k[2]) and (i >= k[1] and i <= k[3]):
					can = 0
			if can == 1:
				posible_solution.append([j,i,j,i])
				return posible_solution
			j = j + 1
		i = i + 1
	return []

# Recursive methode to search the tree
def tree_recursive(posible_solution, matrix):
	solution = []
	max = 0

	aux = deepcopy(posible_solution)
	aux[len(aux)-1][2] = aux[len(aux)-1][2] + 1
	# Check if the mov is plausible
	if check_solution(aux, matrix) == 1 and check_ingredients_count(aux, matrix) == 1:
		aux2 = tree_recursive(aux, matrix)
		if len(aux2) != 0:
			aux = aux2

		value = heuristic(aux, matrix)
		if value > max and check_ingredients(aux, matrix) == 1:
			max = value
			solution = aux

	aux = deepcopy(posible_solution)
	aux[len(aux)-1][3] = aux[len(aux)-1][3] + 1
	# Check if the mov is plausible
	if check_solution(aux, matrix) == 1 and check_ingredients_count(aux, matrix) == 1:
		aux2 = tree_recursive(aux, matrix)
		if len(aux2) != 0:
			aux = aux2

		value = heuristic(aux, matrix)
		if value > max and check_ingredients(aux, matrix) == 1:
			max = value
			solution = aux

	aux = deepcopy(posible_solution)
	if check_ingredients(aux, matrix) == 1:
		aux = choose_new_slice(aux, matrix)
		# Check if the mov is plausible
		if check_solution(aux, matrix) == 1 and len(aux) > 0:
			aux2 = tree_recursive(aux, matrix)
			if len(aux2) != 0:
				aux = aux2

			value = heuristic(aux, matrix)
			if value > max:
				max = value
				solution = aux

	return solution

# Open files
file_in = open(sys.argv[1], 'r')
file_out = open('result.txt', 'w')

# Read header from file_in
header = [int(i) for i in file_in.readline().split()]
print header

# Trasnform data from file to matrix
matrix = []
i = 0
for line in file_in:
	line = line.strip()
	if len(line) > 0:
		matrix.append(list(line))
	i = i + 1

# Count the number of ingredients
ingredients_total = ingredients_count(0, header[0]-1, 0, header[1]-1, matrix)

posible_solution = [[0,0,0,0]]
solution = tree_recursive(posible_solution, matrix)
print "----Solucion----"
print solution
print heuristic(solution, matrix)

file_out.write(str(len(solution))+'\n')
for k in solution:
	file_out.write(str(k[0])+" "+str(k[1])+" "+str(k[2])+" "+str(k[3])+'\n')