def arithmetic_arranger(problems, val=False):
	# Initialize the result string
	arranged_problems = ''

	# Check for too many problems
	if len(problems) > 5:
    	arranged_problems = "Error: Too many problems."
    	return arranged_problems

	# List of all operators in the problems
	operations = []
	for i in problems:
    	parts = i.split()
    	operations.append(parts[1])

	# Check if all operators are either '+' or '-'
	if not all(op in ['+', '-'] for op in operations):
    	arranged_problems = "Error: Operator must be '+' or '-'."
    	return arranged_problems

	# List of all operands
	numbers = []
	for i in problems:
    	parts = i.split()
    	numbers.append(parts[0])
    	numbers.append(parts[2])

	# Check if all operands are digits
	for num in numbers:
    	if not num.isdigit():
        	arranged_problems = "Error: Numbers must only contain digits."
        	return arranged_problems

	# Check if any operand has more than 4 digits
	for num in numbers:
    	if len(num) > 4:
        	arranged_problems = "Error: Numbers cannot be more than four digits."
        	return arranged_problems

	# Calculate the results for the problems
	values = []
	for i in range(0, len(problems)):
    	parts = problems[i].split()
    	operand1 = int(parts[0])
    	operator = parts[1]
    	operand2 = int(parts[2])
   	 
    	if operator == '+':
        	values.append(operand1 + operand2)
    	elif operator == '-':
        	values.append(operand1 - operand2)

	# Build the top row
	top_row = ''
	dashes = ''
	solutions = ''
	for i in range(0, len(numbers), 2):
    	space_width = max(len(numbers[i]), len(numbers[i+1])) + 2
    	top_row += numbers[i].rjust(space_width)
    	dashes += '-' * space_width
    	solutions += str(values[i // 2]).rjust(space_width)
   	 
    	if i != len(numbers) - 2:
        	top_row += ' ' * 4
        	dashes += ' ' * 4
        	solutions += ' ' * 4

	# Build the bottom row (operator + operand2)
	bottom_row = ''
	for i in range(1, len(numbers), 2):
    	space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
    	bottom_row += operations[i // 2]
    	bottom_row += numbers[i].rjust(space_width)
   	 
    	if i != len(numbers) - 1:
        	bottom_row += ' ' * 4

	# Combine rows and optionally show answers
	if val:
    	arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
	else:
    	arranged_problems = '\n'.join((top_row, bottom_row, dashes))

	return arranged_problems

(Guided By chatGPT)
