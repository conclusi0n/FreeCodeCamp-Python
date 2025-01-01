def arithmetic_arranger(problems, show_answers=False):
	if len(problems)>5:
    	return 'Error: Too many problems.'
	first_line = []
	second_line = []
	dashes = []
	answers = []
	for problems in problems:
    	parts=problem.split()

    	if len(parts)!=3:
        	return "Error: Operator must be '+' or '-'."

    	operand1, operator, operand2 = parts

    	if operator not in ['+','-']:
        	return "Error: Operator must be '+' or '-'."
   	 
    	if not operand1.isdigit() or not operand2.isdigit():
        	return "Error: Numbers must only contain digits."

    	if len(operand1)>4 or len(operand2)>4:
        	return 'Error: Numbers cannot be more than four digits.'

    	if operator=='+':
        	reasult=str(int(operand1)+int(operand2))
    	elif operator=='-':
        	reasult=str(int(operand1)-int(operand2))

    	first_line.append(f"{operand1:>{max(len(operand1), len(operand2))}}")
   	 
    	second_line.append(f"{operator} {operand2:>{max(len(operand1), len(operand2)) - 1}}")

    	dashes.append('-' * (max(len(operand1), len(operand2)) + 2))

    	if display_answers:
        	answers.append(f"{result:>{max(len(operand1), len(operand2)) + 2}}")
	arranged_problems = "	".join(first_line) + "\n" + "	".join(second_line) + "\n" + "	".join(dashes)

	if display_answers:
    	arranged_problems += "\n" + "	".join(answers)
    
	return arranged_problems
