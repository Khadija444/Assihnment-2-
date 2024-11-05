#A class that represents a costumer in the e-book store
class Customer:

    def __init__(self, name, email, phone_number, shopping_cart=None):
        # Aggregation: A customer "has a" shopping cart, but the shopping cart can exist independently.
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__shopping_cart = shopping_cart

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_shopping_cart(self):
        return self.__shopping_cart

    def set_shopping_cart(self, shopping_cart):
        self.__shopping_cart = shopping_cart

    def __str__(self):
        return f"Customer: {self.__name}, Email: {self.__email}, Phone: {self.__phone_number}"

# A class child class of the Costumer representing the loyalty membership for the costumer
class LoyaltyMember(Customer):

    # Inheritance of LoyaltyMember "is a" Customer.
    def __init__(self, name, email, phone_number, loyalty_points=0, membership_id=None, shopping_cart=None):
        # Inheritance is indicated by the use of super() to inherit from the Customer class.
        super().__init__(name, email, phone_number, shopping_cart)
        self.__loyalty_points = loyalty_points
        self.__membership_id = membership_id

    # Getters and Setters
    def get_loyalty_points(self):
        return self.__loyalty_points

    def set_loyalty_points(self, loyalty_points):
        self.__loyalty_points = loyalty_points

    def get_membership_id(self):
        return self.__membership_id

    def set_membership_id(self, membership_id):
        self.__membership_id = membership_id

    def __str__(self):
        return f"LoyaltyMember: {self.get_name()}, Email: {self.get_email()}, Points: {self.__loyalty_points}, Membership ID: {self.__membership_id}"

#A class that represents the shopping cart in the store and contains a lost of E-books
class ShoppingCart:

    def __init__(self, customer):
        # Aggregation: The shopping cart is associated with a customer, but both can exist independently.
        self.__ebooks = []
        self.__customer = customer

    # Getters and Setters
    def get_ebooks(self):
        return self.__ebooks
    # Composition relationship: The shopping cart "contains" e-books. If the cart is deleted, the e-books in that cart are also removed.
    def add_ebook(self, ebook):
        if isinstance(ebook, Ebook):
            self.__ebooks.append(ebook)

    def remove_ebook(self, ebook):
        if ebook in self.__ebooks:
            self.__ebooks.remove(ebook)

    def get_customer(self):
        return self.__customer

    def __str__(self):
        ebook_list = "\n".join([str(ebook) for ebook in self.__ebooks])
        return f"ShoppingCart for {self.__customer.get_name()}:\n{ebook_list}"

# a class that represents the e-books that are in the store and their details
class Ebook:

    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getters and Setters
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"Ebook: {self.__title} by {self.__author}, Genre: {self.__genre}, Price: {self.__price}"

# A class that represents the order that would contain a list of e-books
class Order:
    def __init__(self, ebooks, order_date, discount=None):
        # Aggregation: The order "has" e-books, but the e-books exist independently of the order.
        self.__ebooks = ebooks
        self.__order_date = order_date
        self.__discount = discount
        self.__total_price = sum([ebook.get_price() for ebook in ebooks])

    # Getters and Setters
    def get_ebooks(self):
        return self.__ebooks

    def get_order_date(self):
        return self.__order_date

    def set_order_date(self, order_date):
        self.__order_date = order_date

    def get_total_price(self):
        return self.__total_price

    def apply_discount(self, discount):
        # Aggregation: The order "has" a discount, but the discount can exist independently.
        self.__discount = discount
        self.__total_price -= self.__total_price * (self.__discount.get_discount_percentage() / 100)

    def __str__(self):
        ebook_list = "\n".join([str(ebook) for ebook in self.__ebooks])
        discount_str = f"Discount: {self.__discount}" if self.__discount else "No Discount"
        return f"Order Date: {self.__order_date}\nE-books:\n{ebook_list}\nTotal Price: {self.__total_price}\n{discount_str}"

#A class for the discount for the loyalty memebership costumer orders
class Discount:
    def __init__(self, discount_percentage, discount_type):
        self.__discount_percentage = discount_percentage
        self.__discount_type = discount_type

    # Getters and Setters
    def get_discount_percentage(self):
        return self.__discount_percentage

    def get_discount_type(self):
        return self.__discount_type

    def __str__(self):
        return f"Discount: {self.__discount_percentage}% ({self.__discount_type})"

# A class to represent the payment for the order
class Payment:

    def __init__(self, payment_amount, payment_method, payment_success=True):
        # Aggregation: Payment "belongs to" an order, but payments can exist independently.
        self.__payment_amount = payment_amount
        self.__payment_method = payment_method
        self.__payment_success = payment_success

    # Getters and Setters
    def get_payment_amount(self):
        return self.__payment_amount

    def get_payment_method(self):
        return self.__payment_method

    def set_payment_method(self, payment_method):
        self.__payment_method = payment_method

    def is_payment_successful(self):
        return self.__payment_success

    def __str__(self):
        return f"Payment of {self.__payment_amount} via {self.__payment_method} - Success: {self.__payment_success}"

# a class to represent the invoice that is generated after a payment for the order
class Invoice:
    def __init__(self, invoice_number, payment):
        # Composition: Invoice "owns" the payment details; deleting the invoice would delete its payment data.
        self.__invoice_number = invoice_number
        self.__payment = payment
        self.__total_amount = payment.get_payment_amount()

    # Getters and Setters
    def get_invoice_number(self):
        return self.__invoice_number

    def get_payment(self):
        return self.__payment

    def get_total_amount(self):
        return self.__total_amount

    def __str__(self):
        return f"Invoice #{self.__invoice_number}\nPayment Details: {self.__payment}\nTotal Amount: {self.__total_amount}"


# test cases to cover different scenarios
if __name__ == "__main__":
    # Create some e-books
    ebook1 = Ebook("The Great Gatsby", "F. Scott Fitzgerald", "1925", "Fiction", 10.99)
    ebook2 = Ebook("1984", "George Orwell", "1949", "Dystopian", 8.99)
    ebook3 = Ebook("To Kill a Mockingbird", "Harper Lee", "1960", "Fiction", 12.50)

    # Create a customer
    customer = Customer("Khadija", "Khadijaalhammadi@gmail.com", "0512341234")

    # Create a shopping cart for the customer and add e-books
    cart = ShoppingCart(customer)
    cart.add_ebook(ebook1)
    cart.add_ebook(ebook2)
    print(cart)

    # Remove an e-book from the cart
    cart.remove_ebook(ebook1)
    print("After removing one e-book from the cart:")
    print(cart)

    # Add a new e-book to the cart
    cart.add_ebook(ebook3)
    print("After adding a new e-book to the cart:")
    print(cart)

    # Create an order for the customer
    order = Order(cart.get_ebooks(), "2024-10-04")
    print("Order without discount:")
    print(order)

    # Apply a discount to the order
    discount = Discount(10, "loyalty")
    order.apply_discount(discount)
    print("Order with 10% loyalty discount applied:")
    print(order)

    # Process payment for the order
    payment = Payment(order.get_total_price(), "credit card")
    print("Payment details:")
    print(payment)

    # Generate an invoice for the order
    invoice = Invoice("INV - 123", payment)
    print("Invoice details:")
    print(invoice)

    # Test modifying customer information
    customer.set_email("Khadija111@gmail.com")
    customer.set_phone_number("052222222")
    print("Updated customer details:")
    print(customer)

    # Test LoyaltyMember inheritance
    loyalty_member = LoyaltyMember("Mahra", "Mahra@Gmail.com", "056662666", loyalty_points=200, membership_id="Loyal123")
    print(loyalty_member)