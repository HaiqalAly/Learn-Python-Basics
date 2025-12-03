# functions are reusable blocks of code that perform a specific task.

def greet(name, age):
    """Function to greet a person with their name and age."""
    return f"Hello, {name}! You are {age} years old."

print(greet("Alice", 30))
print(greet("Bob", 25))
print(greet("Charlie", 35))

def invoice_total(items, tax_rate=0.07):
    """Function to calculate the total invoice amount including tax."""
    subtotal = sum(items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total
items = [19.99, 5.49, 3.50, 12.99]
print(f"Total invoice amount: ${invoice_total(items):.2f}")