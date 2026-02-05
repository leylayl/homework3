import random
import time

def get_computer_choice():
    """Returns a random choice for the computer."""
    choices = ["🪨", "📜", "✂️"]
    return random.choice(choices)

def get_player_choice():
    """Gets and validates input from the player."""
    mapping = {"r": "🪨", "p": "📜", "s": "✂️"}
    
    while True:
        user_input = input("Enter (R)ock, (P)aper, or (S)cissors: ").lower()
        if user_input in mapping:
            return mapping[user_input]
        print("❌ Invalid choice! Please enter R, P, or S.")

def determine_winner(player, computer):
    """Logic to decide the winner of a single round."""
    if player == computer:
        return "tie"
    
    # Winning conditions for the player
    win_conditions = [
        (player == "🪨" and computer == "✂️"),
        (player == "📜" and computer == "🪨"),
        (player == "✂️" and computer == "📜")
    ]
    
    if any(win_conditions):
        return "player"
    else:
        return "computer"

def play_round():
    """Executes one round and returns the result."""
    print("\n--- 🥊 NEW ROUND ---")
    player = get_player_choice()
    computer = get_computer_choice()
    
    print(f"You: {player}  VS  CPU: {computer}")
    time.sleep(0.5)
    
    result = determine_winner(player, computer)
    
    if result == "tie":
        print("🤝 It's a draw!")
    elif result == "player":
        print("🎉 You won this round!")
    else:
        print("💀 The machines are winning...")
        
    return result

def play_game():
    """The 'Boss' function: Manages the tournament and score."""
    player_score = 0
    computer_score = 0
    rounds_to_win = 3
    
    print("🏆 WELCOME TO THE RPS ULTIMATE TOURNAMENT 🏆")
    print(f"First to {rounds_to_win} points wins the trophy!")
    
    # Loop until someone wins the tournament
    while player_score < rounds_to_win and computer_score < rounds_to_win:
        outcome = play_round()
        
        if outcome == "player":
            player_score += 1
        elif outcome == "computer":
            computer_score += 1
            
        print(f"📊 SCORE: You {player_score} | CPU {computer_score}")
    
    # Final Result
    print("\n" + "="*30)
    if player_score == rounds_to_win:
        print("👑 YOU ARE THE CHAMPION! 👑")
    else:
        print("🤖 CPU WINS THE TOURNAMENT. BETTER LUCK NEXT TIME! 🤖")
    print("="*30)

# --- MAIN PROGRAM ---
if __name__ == "__main__":
    play_game()
    