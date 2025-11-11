class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"✅ Added {coffee.name} to your order.")

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print("🛒 No items in your order.")
            return
        print("\n☕ Your Order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")
        print(f"Total: ${self.total():.2f}\n")

    def checkout(self):
        if not self.items:
            print("⚠️ Your cart is empty.")
            return
        self.show_order()
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("🎉 Order Confirmed! Thank you.")
            self.items.clear()
        else:
            print("❌ Checkout cancelled.")


def main():
    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Cappuccino", 3),
        Coffee("Latte", 4.2),
        Coffee("Americano", 5.0),
        Coffee("Cold Coffee", 5.5),
        Coffee("Filter Coffee", 6.0),
        Coffee("Mocha", 7.0),
        Coffee("Macchiato", 8),
        Coffee("Dalgona Coffee", 8.75),
        Coffee("Turkish Coffee", 10)
    ]

    order1 = Order()

    while True:
        print("\n--- ☕ Coffee Menu ---")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item.name} - ${item.price}")

        print("\n11. View Order")
        print("12. Checkout")
        print("13. Exit")

        try:
            choice = int(input("\nEnter your choice (1–13): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        if 1 <= choice <= len(menu):
            order1.add_item(menu[choice - 1])
        elif choice == 11:
            order1.show_order()
        elif choice == 12:
            order1.checkout()
        elif choice == 13:
            print("👋 Thank you for visiting! Have a great day!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
