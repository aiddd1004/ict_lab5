def add_product(products, name, price):
    products[name] = price
    print("Product added.")

def remove_product(products, name):
    if name in products:
        del products[name]
        print(f"Product '{name}' removed.")
    else:
        print(f"Product '{name}' not found.")

def view_products(products):
    if not products:
        print("No products in the inventory.")
    else:
        for name, price in products.items():
            print(f"{name}: {price}")

def main():
    products = {}
    
   
    while True:
        action = input("Choose action: add, remove, view, quit > ").lower().strip()
        
        if action == "add":
            name = input("Enter product name: ")
            try:
                price = float(input("Enter product price: "))
                add_product(products, name, price)
            except ValueError:
                print("Invalid price. Please enter a number.")
        
        elif action == "remove":
            name = input("Enter product name: ")
            remove_product(products, name)
        
        elif action == "view":
            view_products(products)
        
        elif action == "quit":
            print("Quitting program. ")
            break
        
        else:
            print("Invalid action. Please choose add, remove, view, or quit.")


if __name__ == "__main__":
    main()
