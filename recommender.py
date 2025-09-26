# LDCW6123 - Group Project: Part 2 Interactive Program
# Program Title: Spotify Playlist Recommendation Assistant
# Description: An interactive program that suggests Spotify playlists based on user's mood.
# It runs in a loop, allowing multiple selections, and includes an exit option.

def recommend_playlist():
    """
    Main function to run the playlist recommender.
    It contains the primary loop and logic for the program.
    """
    
    # Display a one-time welcome message when the program starts.
    print("=====================================================")
    print(" Welcome to the Spotify Playlist Recommendation Assistant!")
    print("=====================================================")

    # The main program loop runs continuously until the user chooses to exit.
    while True:
        # Display the menu of options to the user in each loop iteration.
        print("Tell us your mood, and we'll suggest a playlist for you.")
        print("Choose from: Happy, Sad, Focus, Workout")
        print("(Type 'exit' to quit the program)\n")
        
        # Get and process user input, removing whitespace and converting to lowercase.
        user_mood = input("Enter your current mood: ").strip().lower()
        
        # Check for the exit condition to terminate the program.
        if user_mood == 'exit':
            print("\nExiting the recommendation assistant. Goodbye!")
            break
            
        print("\n--- Your Recommendation ---")
        
        # Process the user's choice and provide the corresponding recommendation.
        if user_mood == "happy":
            print("Playlist Suggestion: 'All-Time Happy Anthems'")
            print("Description: Timeless, feel-good classics that everyone knows.")
            print("Songs you might like:")
            print("  - 'Don't Stop Me Now' by Queen")
            print("  - 'Happy' by Pharrell Williams")
            print("  - 'Walking on Sunshine' by Katrina & The Waves")
            
        elif user_mood == "sad":
            print("Playlist Suggestion: 'Timeless Tearjerkers'")
            print("Description: Mellow and emotional tracks for reflective moments.")
            print("Songs you might like:")
            print("  - 'Someone Like You' by Adele")
            print("  - 'Lover, You Should've Come Over' by Jeff Buckley")
            print("  - 'Let Down' by Radiohead")

        elif user_mood == "focus":
            print("Playlist Suggestion: 'Iconic Instrumentals'")
            print("Description: Instrumental music to help you concentrate.")
            print("Songs you might like:")
            print("  - 'Test Drive' by John Powell (from HTTYD)")
            print("  - 'Duel of the Fates' by John Williams")
            print("  - 'Concerning Hobbits' by Howard Shore (from The Lord of the Rings)")
            
        elif user_mood == "workout":
            print("Playlist Suggestion: 'Ultimate Workout Anthems'")
            print("Description: High-energy tracks to power you through your workout.")
            print("Songs you might like:")
            print("  - 'Eye of the Tiger' by Survivor")
            print("  - 'Back in Black' by AC/DC")
            print("  - 'Sweet Child O' Mine' by Guns N' Roses")
            
        # Handle cases where the user input does not match any of the valid options.
        else:
            print(f"Sorry, '{user_mood}' is not a valid option.")
            print("Please try one of the suggested moods.")
            
        # Print a separator for better readability before the next loop iteration.
        print("\n=====================================================\n")


# This standard entry point runs the main function when the script is executed.
if __name__ == "__main__":
    recommend_playlist()