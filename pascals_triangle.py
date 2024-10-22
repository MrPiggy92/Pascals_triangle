from colorama import Fore, init
import copy
import re

init(autoreset=True)

def generate_pascals_triangle(num_rows):
    triangle = []
    for row_num in range(num_rows):
        row = [1] * (row_num + 1)  # Initialize row with 1s
        # Calculate values for inner elements of the row
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(row)

def save_pascals_triangle(triangle):
	with open("pascals_triangle.txt", 'w') as file:
		for row in triangle:
			file.write(row)
			file.write("\n")

def triangulate(ogtriangle, saved):
	triangle = copy.deepcopy(ogtriangle)
	for num, row in enumerate(triangle):
		for rownum, item in enumerate(row):
			if saved:
				row[rownum] = str(item)
			else:
				index = len(str(item))-1
				while index >= len(all_colours):
					index -= len(all_colours)
				row[rownum] = all_colours[index] + str(item)
		triangle[num] = ' '.join(row)
	size = max(len(re.sub(r'\x1b\[[0-9;]*m', '', ''.join(row))) for row in triangle)
	for num, row in enumerate(triangle):
		numSpaces = (size - len(re.sub(r'\x1b\[[0-9;]*m', '', ''.join(row)))) // 2
		triangle[num] = (' ' * numSpaces) + row + (' ' * numSpaces)
	return triangle
		

all_colours = [Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTYELLOW_EX, Fore.RED, Fore.MAGENTA, Fore.YELLOW, Fore.LIGHTRED_EX, Fore.RESET]

while True:
	num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))
	ogtriangle = generate_pascals_triangle(num_rows)[1:]
	
	printedtriangle = triangulate(ogtriangle, False)
	print_pascals_triangle(printedtriangle)
	
	savedtriangle = triangulate(ogtriangle, True)
	save_pascals_triangle(savedtriangle)
