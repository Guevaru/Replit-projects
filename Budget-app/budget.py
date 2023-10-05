class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for transaction in self.ledger:
            total += transaction["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name}".center(30, '*') + '\n'
        items = ''
        total = 0
        for transaction in self.ledger:
            description = transaction["description"][:23].ljust(23)
            amount = str(format(transaction["amount"], ".2f")).rjust(7)
            items += f"{description}{amount}\n"
            total += transaction["amount"]
        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    total_withdrawals = 0
    category_names = []
    spent_percentages = []

    for category in categories:
        total_withdrawals += sum(
            [transaction["amount"] for transaction in category.ledger if transaction["amount"] < 0]
        )
        category_names.append(category.name)

    for category in categories:
        spent_percentage = (
            sum(
                [transaction["amount"] for transaction in category.ledger if transaction["amount"] < 0]
            )
            / total_withdrawals
        )
        spent_percentages.append(spent_percentage * 100)

    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in spent_percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += '\n'

    chart += "    " + "-" * (3 * len(category_names) + 1) + '\n'

    max_name_length = max([len(name) for name in category_names])

    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += '\n'

    return chart
#valamogul nem jo a kimenet, de nem tudom miert