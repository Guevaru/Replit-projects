import unittest
from arithmetic_arranger import arithmetic_arranger

class TestArithmeticArranger(unittest.TestCase):
    def test_arrangement(self):
        problems = ["235 + 52", "3801 - 2", "45 + 43", "123 + 49"]
        expected_output = "  235      3801      45      123\n+  52    -    2    + 43    +  49\n-----    ------    ----    -----\n"
        self.assertEqual(arithmetic_arranger(problems), expected_output)

    def test_arrangement_with_answers(self):
        problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
        expected_output = "  32         1      9999      523\n+  8    - 3801    + 9999    -  49\n----    ------    ------    -----\n  40     -3800     19998      474\n"
        self.assertEqual(arithmetic_arranger(problems, show_answers=True), expected_output)

    def test_too_many_problems(self):
        problems = ["1 + 1", "2 + 2", "3 + 3", "4 + 4", "5 + 5", "6 + 6"]
        expected_output = "Error: Too many problems."
        self.assertEqual(arithmetic_arranger(problems), expected_output)

    def test_invalid_operator(self):
        problems = ["1 + 1", "2 x 2", "3 - 3", "4 + 4"]
        expected_output = "Error: Operator must be '+' or '-'."
        self.assertEqual(arithmetic_arranger(problems), expected_output)

    def test_invalid_numbers(self):
        problems = ["1 + 1", "2 + a", "3 - 3", "4 + 4"]
        expected_output = "Error: Numbers must only contain digits."
        self.assertEqual(arithmetic_arranger(problems), expected_output)

    def test_number_width_exceeded(self):
        problems = ["1234 + 5678", "9999 - 8888", "12 + 34", "123456789 + 987654321"]
        expected_output = "Error: Numbers cannot be more than four digits."
        self.assertEqual(arithmetic_arranger(problems), expected_output)

if __name__ == "__main__":
    unittest.main()
