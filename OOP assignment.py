class Product:
    supermarket_name = "SuperMarket"

    def __init__(self, product_ID, name, price, manufacturer, weight, expiration_date, year):
        self.__product_ID = product_ID
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.weight = weight
        self.expiration_date = expiration_date
        self.year = year

    def print_details(self):
        print("Supermarket Name:", self.supermarket_name)
        print("Product ID:", self.__product_ID)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Manufacturer:", self.manufacturer)
        print("Weight:", self.weight)
        print("Expiration Date:", self.expiration_date)
        print("Year:", self.year)

    def change_product_ID(self, new_ID):
        self.__product_ID = new_ID


class Healthy(Product):
    def __init__(self, product_ID, name, price, manufacturer, weight, expiration_date, year):
        super().__init__(product_ID, name, price, manufacturer, weight, expiration_date, year)
        self.calories = 0
        self.components = ""

    def add_calories(self, calories):
        self.calories += calories

    def change_weight(self, new_weight):
        self.weight = new_weight

    def print_details(self):
        super().print_details()
        print("Calories:", self.calories)
        print("Components:", self.components)

    def compute_total_calories(self):
        total_calories = self.calories * self.weight
        return total_calories


def main():
    while True:
        print("Welcome to Supermarket Cashier System")
        print("1. Product")
        print("2. Healthy")
        print("3. Exit")

        choice = input("Choose the subsystem: ")

        if choice == "1":
            product = Product("P001", "Apple", 1.50, "Farmers Inc.", 100, "2024-05-31", 2024)
            while True:
                print("\nOptions:")
                print("1. Add new Product")
                print("2. Display Product Details")
                print("3. Change/Edit product_ID")
                print("4. Exit the sub-system")
                print("5. Exit the Supermarket cashier system")

                option = input("Choose an option: ")

                if option == "1":
                    pass
                elif option == "2":
                    product.print_details()
                elif option == "3":
                    new_ID = input("Enter new product ID: ")
                    product.change_product_ID(new_ID)
                    print("Product ID changed successfully!")
                elif option == "4":
                    break
                elif option == "5":
                    exit()
                else:
                    print("Invalid option")

        elif choice == "2":
            healthy_product = Healthy("Milk", "Eggs" "Chicken")
            while True:
                print("\nOptions:")
                print("1. Add new Healthy Product")
                print("2. Display Healthy Product Details")
                print("3. Change/Edit calories")
                print("4. Check calories and components of Healthy Product")
                print("5. Compute total calories of the Healthy Product based on the weight")
                print("6. Exit the sub-system")
                print("7. Exit the Supermarket cashier system")

                option = input("Choose an option: ")

                if option == "1":
                    pass
                elif option == "2":
                    healthy_product.print_details()
                elif option == "3":
                    calories = int(input("Enter additional calories: "))
                    healthy_product.add_calories(calories)
                    print("Calories updated successfully!")
                elif option == "4":
                    print("Calories:", healthy_product.calories)
                    print("Components:", healthy_product.components)
                elif option == "5":
                    weight = int(input("Enter weight in grams: "))
                    total_calories = healthy_product.compute_total_calories()
                    print("Total calories based on weight:", total_calories)
                elif option == "6":
                    break
                elif option == "7":
                    exit()
                else:
                    print("Invalid option")

        elif choice == "3":
            exit()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
