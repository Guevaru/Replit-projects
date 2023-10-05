from budget import Category, create_spend_chart

# Testing the Category class
food_category = Category("Food")
clothing_category = Category("Clothing")  # Create a clothing_category instance
food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more foo")
food_category.transfer(50, clothing_category)  
print(food_category)

# Testing the create_spend_chart function
entertainment_category = Category("Entertainment")
categories = [food_category, clothing_category, entertainment_category]
print(create_spend_chart(categories))
