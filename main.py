# Simple E-commerce Shopping Cart

products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Smartphone", "price": 20000},
    3: {"name": "Headphones", "price": 1500},
    4: {"name": "Keyboard", "price": 800},
    5: {"name": "Mouse", "price": 500}
}

cart = {}

def show_products():
    print("\nAvailable Products:")
    for pid, details in products.items():
        print(f"{pid}. {details['name']} - ₹{details['price']}")

def show_cart():
    if not cart:
        print("\nYour cart is empty.")
    else:
        print("\nYour Cart:")
        total = 0
        for pid, qty in cart.items():
            item_total = products[pid]['price'] * qty
            total += item_total
            print(f"{products[pid]['name']} (x{qty}) - ₹{item_total}")
        print(f"Total Amount: ₹{total}")

def add_to_cart():
    show_products()
    try:
        pid = int(input("Enter Product ID to add: "))
        if pid in products:
            qty = int(input("Enter quantity: "))
            cart[pid] = cart.get(pid, 0) + qty
            print(f"{products[pid]['name']} added to cart.")
        else:
            print("Invalid product ID.")
    except ValueError:
        print("Invalid input!")

def remove_from_cart():
    show_cart()
    try:
        pid = int(input("Enter Product ID to remove: "))
        if pid in cart:
            qty = int(input("Enter quantity to remove: "))
            if qty >= cart[pid]:
                del cart[pid]
                print("Item removed from cart.")
            else:
                cart[pid] -= qty
                print(f"{qty} removed from {products[pid]['name']}.")
        else:
            print("Item not in cart.")
    except ValueError:
        print("Invalid input!")

def checkout():
    show_cart()
    if cart:
        print("\nThank you for shopping with us!")
        print("Order placed successfully.")
        cart.clear()
    else:
        print("Your cart is empty. Nothing to checkout.")

# Main Menu
while True:
    print("\n--- E-Commerce Shopping Cart ---")
    print("1. View Products")
    print("2. View Cart")
    print("3. Add to Cart")
    print("4. Remove from Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_products()
    elif choice == '2':
        show_cart()
    elif choice == '3':
        add_to_cart()
    elif choice == '4':
        remove_from_cart()
    elif choice == '5':
        checkout()
    elif choice == '6':
        print("Thank you! Visit again.")
        break
    else:
        print("Invalid choice! Please try again.")
