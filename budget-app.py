class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        # 30-character title
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            # Truncate description to 23 chars, and format amount to 2 decimal places (7 width)
            desc = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
def create_spend_chart(categories):
    # Calculate spending per category (excluding transfers)
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0 and "Transfer" not in item["description"]:
                spent += abs(item["amount"])
        spent_amounts.append(spent)

    total = sum(spent_amounts)
    
    # Calculate percentages
    percentages = [int((amount / total * 100) // 10) * 10 if total > 0 else 0 for amount in spent_amounts]

    # Build the chart string
    chart = "Percentage spent by category\n"
    
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percent in percentages:
            if percent >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    # Separation line
    dashes = "-" * (len(categories) * 3 + 1)
    chart += f"    {dashes}\n"

    # Category names vertically
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]

    for i in range(max_len):
        chart += "    "
        for name in names:
            chart += f" {name[i]} "
        chart += " \n"

    # Clean trailing newline to ensure tests pass
    return chart.rstrip("\n")
