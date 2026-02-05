# Program A: For Loop Birthday Generator
guests = ["Alice", "Bob", "The Mystery Guest"]

for name in guests:
    print(f"\n--- Singing for {name} ---")
    for i in range(4):
        if i == 2:
            print(f"Happy Birthday dear {name}!")
        else:
            print("Happy Birthday to you!")
    print("And many mooooore! 🎂")
    