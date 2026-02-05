import time

def cine_match():
    print("--- 🎬 WELCOME TO CINEMATCH 🎬 ---")
    print("Let's find the perfect movie for your night.\n")

    # Input gathering
    group = input("Who are you watching with? (alone / friends / date): ").lower()
    mood = input("What's the vibe? (chill / high-energy): ").lower()
    
    print("\n--- 🕵️ Analyzing the cinematic database... ---")
    time.sleep(1.5)

    # The Decision Engine
    if group == "date":
        if mood == "chill":
            recommendation = "About Time (A heartwarming, time-travel romance)"
        else:
            recommendation = "La La Land (High-energy music and bittersweet love)"
            
    elif group == "friends":
        genre = input("Pick a genre (horror / comedy): ").lower()
        if genre == "horror":
            recommendation = "Barbarian (A wild ride with plenty of shocks)"
        else:
            recommendation = "Glass Onion (A fun, stylish whodunnit)"
            
    else: # This handles 'alone' or any other input
        if mood == "high-energy":
            recommendation = "Spider-Man: Across the Spider-Verse (A visual masterpiece)"
        else:
            recommendation = "The Banshees of Inisherin (Beautifully shot and thoughtful)"

    # The Result
    print("\n" + "="*30)
    print(f"✨ YOUR MATCH: {recommendation} ✨")
    print("="*30)
    print("Enjoy the show!")

cine_match()

