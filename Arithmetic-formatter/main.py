from arithmetic_arranger import arithmetic_arranger

# Example usage
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arranged_problems = arithmetic_arranger(problems)
print(arranged_problems)

# Example usage with answers displayed
problems_with_answers = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
arranged_problems_with_answers = arithmetic_arranger(problems_with_answers, show_answers=True)
print(arranged_problems_with_answers)
