def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_lines = []
    bottom_lines = []
    separator_lines = []
    answer_lines = []

    for problem in problems:
        elements = problem.split()

        if len(elements[0]) > 4 or len(elements[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if not elements[0].isdigit() or not elements[2].isdigit():
            return "Error: Numbers must only contain digits."

        if elements[1] != "+" and elements[1] != "-":
            return "Error: Operator must be '+' or '-'."

        width = max(len(elements[0]), len(elements[2]))

        top_line = elements[0].rjust(width + 2)
        bottom_line = elements[1] + elements[2].rjust(width + 1)
        separator_line = "-" * (width + 2)

        if show_answers:
            if elements[1] == "+":
                answer = str(int(elements[0]) + int(elements[2]))
            else:
                answer = str(int(elements[0]) - int(elements[2]))

            answer_line = answer.rjust(width + 2)

            answer_lines.append(answer_line)
        
        top_lines.append(top_line)
        bottom_lines.append(bottom_line)
        separator_lines.append(separator_line)

    arranged_problems = ""

    for i in range(len(problems)):
        arranged_problems += top_lines[i]
        arranged_problems += "    " * 4  # Four spaces between each problem
    arranged_problems += "\n"

    for i in range(len(problems)):
        arranged_problems += bottom_lines[i]
        arranged_problems += "    " * 4
    arranged_problems += "\n"

    for i in range(len(problems)):
        arranged_problems += separator_lines[i]
        arranged_problems += "    " * 4
    arranged_problems += "\n"

    if show_answers:
        for i in range(len(problems)):
            arranged_problems += answer_lines[i]
            arranged_problems += "    " * 4

    return arranged_problems.rstrip()


