class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = float(amount)

    def to_dict(self):
        """Convert expense object to dictionary for storage."""
        return {
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        }

    def display(self):
        """Return formatted string for display."""
        return (f"Date: {self.date} | Category: {self.category} | "
                f"Description: {self.description} | Amount: ₹{self.amount:.2f}")