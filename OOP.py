class Product:
    supermarket_name = "Your Supermarket"

    def __init__(self, name, price, manufacturer, weight, expiration_date, year):
        self.__product_ID = None
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.weight = weight
        self.expiration_date = expiration_date
        self.year = year

    def set_product_ID(self, product_ID):
        self.__product_ID = product_ID

    def print_details(self):
        print("Supermarket:", self.supermarket_name)
        print("Product ID:", self.__product_ID)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Manufacturer:", self.manufacturer)
        print("Weight:", self.weight)
        print("Expiration Date:", self.expiration_date)
        print("Year:", self.year)


class Healthy(Product):
    def __init__(self, name, price, manufacturer, weight, expiration_date, year):
        super().__init__(name, price, manufacturer, weight, expiration_date, year)
        self.calories = 0
        self.components = []

    def add_calories(self, calories):
        self.calories += calories

    def print_details(self):
        super().print_details()
        print("Calories:", self.calories)
        print("Components:", ', '.join(self.components))

    def calculate_total_calories(self):
        return self.calories * self.weight


def main():
    while True:
        print("Welcome to", Product.supermarket_name)
        print("1. Product")
        print("2. Healthy")
        print("3. Exit")

        choice = input("Please choose an option: ")

        if choice == "1":
            manage_product()
        elif choice == "2":
            manage_healthy()
        elif choice == "3":
            print("Exiting Supermarket cashier system.")
            break
        else:
            print("Invalid choice. Please choose again.")


def manage_product():
    products = []
    while True:
        print("\nProduct Sub-system:")
        print("1. Add new Product")
        print("2. Display Product Details")
        print("3. Change/Edit product_ID")
        print("4. Exit the sub-system")

        choice = input("Please choose an option: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            manufacturer = input("Enter product manufacturer: ")
            weight = input("Enter product weight: ")
            expiration_date = input("Enter product expiration date: ")
            year = input("Enter product year: ")
            product = Product(name, price, manufacturer, weight, expiration_date, year)
            product.set_product_ID(len(products) + 1)
            products.append(product)
            print("Product added successfully!")
        elif choice == "2":
            if not products:
                print("No products added yet.")
            else:
                for product in products:
                    product.print_details()
        elif choice == "3":
            print("Functionality not implemented yet.")
        elif choice == "4":
            print("Exiting Product sub-system.")
            break
        else:
            print("Invalid choice. Please choose again.")


def manage_healthy():
    healthy_products = []
    while True:
        print("\nHealthy Sub-system:")
        print("1. Add new Healthy Product")
        print("2. Display Healthy Product Details")
        print("3. Change/Edit calories")
        print("4. Check calories and components of Healthy Product")
        print("5. Compute total calories of the Healthy Product based on the weight")
        print("6. Exit the sub-system")

        choice = input("Please choose an option: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            manufacturer = input("Enter product manufacturer: ")
            weight = float(input("Enter product weight: "))
            expiration_date = input("Enter product expiration date: ")
            year = input("Enter product year: ")
            healthy_product = Healthy(name, price, manufacturer, weight, expiration_date, year)
            healthy_products.append(healthy_product)
            print("Healthy product added successfully!")
        elif choice == "2":
            if not healthy_products:
                print("No healthy products added yet.")
            else:
                for product in healthy_products:
                    product.print_details()
        elif choice == "3":
            print("Functionality not implemented yet.")
        elif choice == "4":
            print("Functionality not implemented yet.")
        elif choice == "5":
            if not healthy_products:
                print("No healthy products added yet.")
            else:
                product_index = int(input("Enter the index of the healthy product: "))
                if 0 < product_index <= len(healthy_products):
                    product = healthy_products[product_index - 1]
                    print("Total calories:", product.calculate_total_calories())
                else:
                    print("Invalid index.")
        elif choice == "6":
            print("Exiting Healthy sub-system.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()