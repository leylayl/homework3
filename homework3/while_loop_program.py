# Program B: While Loop Calculator
print("--- Welcome to MathBot  ---")
print("Type 'exit' at any time to quit.")

active = True

while active:
    user_input = input("\nEnter an equation (e.g., 5 + 5) or 'exit': ").lower()

    if user_input == 'exit':
        print("Goodbye! Numbers will miss you.")
        active = False
    else:
        try:
            # eval() processes the string as a math equation
            result = eval(user_input)
            print(f"Result: {result}")
        except:
            print("Oops! That's not a valid math problem. Try again.")
            
