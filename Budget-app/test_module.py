import unittest
from budget import Category, create_spend_chart


class TestCategory(unittest.TestCase):

  def setUp(self):
    self.food_category = Category("Food")
    self.clothing_category = Category("Clothing")
    self.entertainment_category = Category("Entertainment")

  def test_deposit(self):
    self.food_category.deposit(1000, "initial deposit")
    self.assertEqual(self.food_category.get_balance(), 1000)

  def test_withdraw(self):
    self.food_category.deposit(1000, "initial deposit")
    self.food_category.withdraw(10.15, "groceries")
    self.assertEqual(self.food_category.get_balance(), 989.85)

  def test_get_balance(self):
    self.food_category.deposit(1000, "initial deposit")
    self.food_category.withdraw(10.15, "groceries")
    self.food_category.withdraw(15.89, "restaurant and more foo")
    self.assertEqual(self.food_category.get_balance(), 973.96)

  def test_transfer(self):
    self.food_category.deposit(1000, "initial deposit")
    self.food_category.transfer(50, self.clothing_category)
    self.assertEqual(self.food_category.get_balance(), 950)
    self.assertEqual(self.clothing_category.get_balance(), 50)


class TestCreateSpendChart(unittest.TestCase):

  def test_create_spend_chart(self):
    food_category = Category("Food")
    food_category.deposit(1000, "initial deposit")
    food_category.withdraw(10.15, "groceries")
    food_category.withdraw(15.89, "restaurant and more foo")

    clothing_category = Category("Clothing")
    clothing_category.deposit(500, "initial deposit")
    clothing_category.withdraw(50.75, "shoes")
    clothing_category.withdraw(100, "jacket")

    entertainment_category = Category("Entertainment")
    entertainment_category.deposit(1000, "initial deposit")
    entertainment_category.withdraw(15, "movies")
    entertainment_category.withdraw(35.56, "concert")

    categories = [food_category, clothing_category, entertainment_category]
    expected_output = "Percentage spent by category\n" \
                      "100|          \n" \
                      " 90|          \n" \
                      " 80|          \n" \
                      " 70|          \n" \
                      " 60| o        \n" \
                      " 50| o        \n" \
                      " 40| o        \n" \
                      " 30| o        \n" \
                      " 20| o  o     \n" \
                      " 10| o  o  o  \n" \
                      "  0| o  o  o  \n" \
                      "    ----------\n" \
                      "     F  C  E  \n" \
                      "     o  l  n  \n" \
                      "     o  o  t  \n" \
                      "     d  t  e  \n" \
                      "        h  r  \n" \
                      "        i  t  \n" \
                      "        n  a  \n" \
                      "        g  i  \n" \
                      "           n  \n" \
                      "           m  \n" \
                      "           e  \n" \
                      "           n  \n" \
                      "           t  \n"

    self.assertEqual(create_spend_chart(categories), expected_output)


if __name__ == '__main__':
  unittest.main()
