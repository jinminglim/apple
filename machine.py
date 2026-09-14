"""
INF1103 - Week 3: Procedural Design and Functions
====================================================
Run this file section by section (or all at once) to see how each
concept works. Each section matches a part of the lecture slides.
"""

# ============================================================
# 1. WHY FUNCTIONS? (the "bad" way - repeated code)
# ============================================================
# This is the Shopee order example from the slides.
# Same 5 lines of logic copy-pasted 3 times = hard to maintain.

print("--- Without functions (repeated code) ---")

# Item 1
price = 20
discount = price * 0.10
subtotal = price - discount
gst = subtotal * 0.09
final_price = subtotal + gst
print(final_price)

# Item 2
price = 50
discount = price * 0.10
subtotal = price - discount
gst = subtotal * 0.09
final_price = subtotal + gst
print(final_price)

# Item 3 (imagine doing this 1,000,000 times...)
price = 10
discount = price * 0.10
subtotal = price - discount
gst = subtotal * 0.09
final_price = subtotal + gst
print(final_price)


# ============================================================
# 2. FUNCTION STRUCTURE
# ============================================================
#   def function_name(arguments):
#       '''docstring - optional comment'''
#       function_suite   <- must be indented
#       return [expression]   <- optional

def calculate_total(price):
    """Calculates final price after 10% discount and 9% GST."""
    discount = price * 0.10
    subtotal = price - discount
    gst = subtotal * 0.09
    return subtotal + gst

print("\n--- With a function (reused, no copy-paste) ---")
print(calculate_total(20))
print(calculate_total(50))
print(calculate_total(10))


# ============================================================
# 3. FORMAL vs ACTUAL ARGUMENTS
# ============================================================
# Formal argument = the placeholder name in the def line (e.g. "name")
# Actual argument = the real value you pass in when calling (e.g. "Nisha")

def greet(name):  # "name" is the formal argument
    print("Hello", name)

greet("Nisha")  # "Nisha" is the actual argument


# ============================================================
# 4. POSITIONAL ARGUMENTS
# ============================================================
# Matched by ORDER. Getting the order wrong changes the meaning!

def create_order(customer, product, quantity):
    print(customer, "ordered", quantity, product)

print("\n--- Positional arguments ---")
create_order("John", "Laptop", 2)   # correct order
create_order("Laptop", "John", 2)   # wrong order -> wrong (but valid) output


# ============================================================
# 5. KEYWORD ARGUMENTS
# ============================================================
# Matched by NAME, so order doesn't matter. More readable when
# there are many parameters.

print("\n--- Keyword arguments ---")
create_order(customer="John", product="Laptop", quantity=2)
create_order(quantity=2, product="Laptop", customer="John")  # same result


# ============================================================
# 6. TUPLES (needed to understand multiple return values)
# ============================================================
# - store multiple values in one variable
# - written with ( )
# - immutable (cannot be changed after creation)
# - can be "unpacked" into separate variables

numbers = (10, 20, 30)
print("\n--- Tuple ---")
print(numbers)

firstRank, secondRank, thirdRank = numbers  # unpacking
print(firstRank, secondRank, thirdRank)


# ============================================================
# 7. RETURN VALUES
# ============================================================
# - return stops the function immediately
# - if there's no return statement, the function returns None
# - a function can return multiple values as a tuple

def calculate_discount(price):
    discount = price * 0.10
    return discount

def calculate(a, b):
    return a + b, a * b  # returns a tuple: (sum, product)

print("\n--- Return values ---")
sum_value, product_value = calculate(4, 5)
print(sum_value)
print(product_value)


# ============================================================
# 8. *args - unknown number of positional arguments
# ============================================================
# Problem: what if a Shopee cart has 2 items? 5 items? 10 items?
# We don't want a different function for every possible cart size.
# *args collects all the extra positional arguments into a tuple.

def calculate_total_args(*prices):
    print(prices)          # prices is a tuple, e.g. (20, 15, 30)
    return sum(prices)

print("\n--- *args ---")
print(calculate_total_args(20, 15, 30))
print(calculate_total_args(10, 15, 30, 40, 50))


# ============================================================
# 9. **kwargs - unknown number of keyword arguments
# ============================================================
# Packs keyword arguments into a dictionary.

def print_order_details(**kwargs):
    print(kwargs)  # kwargs is a dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n--- **kwargs ---")
print_order_details(customer="John", product="Laptop", quantity=2)


# ============================================================
# 10. SCOPE OF A VARIABLE
# ============================================================
# A variable created INSIDE a function is "local" - it only exists
# while that function is running, and disappears once it returns.

def calculate_discount_scope(price):
    discount = price * 0.10  # local variable
    return discount

print("\n--- Scope ---")
print(calculate_discount_scope(100))
# print(discount)  # <-- Uncommenting this line causes:
# NameError: name 'discount' is not defined
# because 'discount' only exists inside the function.


# ============================================================
# 11. FUNCTIONS AS OBJECTS
# ============================================================
# A function can be assigned to a variable, or passed into
# another function as an argument.

def greet2():
    print("Hello")

message = greet2   # no () -> just refers to the function itself
message()           # () -> now we actually call it

def square(x):
    return x * x

def apply_function(func, value):
    return func(value)  # func is a function passed in as an argument

print("\n--- Functions as objects ---")
print(apply_function(square, 5))


# ============================================================
# 12. MODULES (putting related functions in their own file)
# ============================================================
# In real projects you'd put functions like apply_discount() and
# calculate_gst() into a separate file, e.g. billing.py, then:
#
#   import billing
#   price = billing.apply_discount(price)
#   price = billing.calculate_gst(price)
#
# This keeps code organized and reusable across multiple programs.


# ============================================================
# PRACTICE 1: Parking-charge system (from "Task for the day")
# ============================================================
# Rules: first 2 hours free, then $2/hour after that.
# Try writing this yourself first! A sample solution is below.

def calculate_parking_fee(hours):
    """Return parking fee: first 2 hours free, then $2/hour."""
    free_hours = 2
    rate_per_hour = 2

    if hours <= free_hours:
        return 0
    else:
        chargeable_hours = hours - free_hours
        return chargeable_hours * rate_per_hour

print("\n--- Practice 1: Parking fee ---")
print(calculate_parking_fee(1))   # 0 (still free)
print(calculate_parking_fee(2))   # 0 (exactly free limit)
print(calculate_parking_fee(5))   # 3 hours * $2 = 6
print(calculate_parking_fee(10))  # 8 hours * $2 = 16


# ============================================================
# PRACTICE 2: Smart Vending Machine (from "Task for the day")
# ============================================================
# TODO: this is left mostly blank for you to complete.
# Rules:
#   "Coke"  -> print "Dispensing Coke"

#   "Water" -> print "Dispensing Water"

#   "Juice" -> print "Dispensing Juice"

#   anything else -> print "Drink Not Available"

#
# Challenge: also keep track of how many drinks have been dispensed.


drink_count = 0

inventory = {
    "Coke": {"price": 1.50, "stock": 50},
    "Juice": {"price": 2.00, "stock": 35},
    "Water": {"price": 1.00, "stock": 200},
}

def dispense_drink(drink_name):
    global drink_count

    if drink_name not in inventory:
        print("Drink Not Available")
        return

    if inventory[drink_name]["stock"] <= 0:
        print(f"{drink_name} is out of stock")
        return

    inventory[drink_name]["stock"] -= 1
    drink_count += 1
    price = inventory[drink_name]["price"]
    remaining = inventory[drink_name]["stock"]
    print(f"Dispensing {drink_name} - ${price} - Remaining stock {remaining}")

dispense_drink("Coke")
dispense_drink("Juice")
dispense_drink("Water")
dispense_drink("Sprite")

print("Total drinks dispensed:", drink_count)