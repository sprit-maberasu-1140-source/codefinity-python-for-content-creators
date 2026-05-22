def generate_greetings(names):
    greetings = []
    for name in names:
        greeting = f"Hello, {name}! Thanks for subscribing."
        greetings.append(greeting)
    for greeting in greetings:
        print(greeting)

names_list = ["Alice", "Bob", "Charlie"]
generate_greetings(names_list)