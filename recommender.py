# LDCW6123 - Group Project: Part 2 Interactive Program
# Program Title: Spotify Playlist Recommendation Assistant
# This program recommends a Spotify playlist based on the user's mood.
# It demonstrates the core logic of personalization that helped Spotify disrupt
# the traditional music industry by offering curated, access-based listening
# experiences instead of just selling tracks.

def recommend_playlist():
    """
    Main function to run the playlist recommender.
    It takes user input for their mood and provides a playlist suggestion.
    This fulfills the requirement for a program with user inputs and outputs.
    """
    
    # Welcome message and instructions for the user for a good user experience.
    print("=====================================================")
    print(" Welcome to the Spotify Playlist Recommendation Assistant!")
    print("=====================================================")
    print("Tell us your mood, and we'll suggest a playlist for you.")
    print("Choose from: Happy, Sad, Focus, Workout\n")
    
    # Get user input. The .strip() and .lower() methods help handle user entry errors.
    user_mood = input("Enter your current mood: ").strip().lower()
    
    # This section uses if/elif/else statements to process user choices,
    # which is a core requirement of the assignment.
    
    print("\n--- Your Recommendation ---")
    
    if user_mood == "happy":
        # Output for 'happy' mood
        print("Playlist Suggestion: 'All-Time Happy Anthems'")
        print("Description: Feel-good tracks to boost your mood and make you smile.")
        print("Songs you might like:")
        print("  - 'Don't Stop Me Now' by Queen")
        print("  - 'Happy' by Pharrell Williams")
        print("  - 'Walking on Sunshine' by Katrina & The Waves")
            
    elif user_mood == "sad":
        # Output for 'sad' mood
        print("Playlist Suggestion: 'Timeless Tearjerkers'")
        print("Description: Mellow and emotional tracks for reflective moments.")
        print("Songs you might like:")
        print("  - 'Someone Like You' by Adele")
        print("  - 'Lover, You Should’ve Come Over' by Jeff Buckley")
        print("  - 'Let Down' by Radiohead")

    elif user_mood == "focus":
        # Output for 'focus' mood
        print("Playlist Suggestion: 'Iconic Instrumentals'")
        print("Description: Instrumental music to help you concentrate.")
        print("Songs you might like:")
        print("  - 'Test Drive' by John Powell (from HTTYD)")
        print("  - 'Duel of the Fates' by John Williams")
        print("  - 'Concerning Hobbits' by Howard Shore (from The Lord of the Rings)")
            
    elif user_mood == "workout":
        # Output for 'workout' mood
        print("Playlist Suggestion: 'Ultimate Workout Anthems'")
        print("Description: High-energy tracks to power you through your workout.")
        print("Songs you might like:")
        print("  - 'Eye of the Tiger' by Survivor")
        print("  - 'Back in Black' by AC/DC")
        print("  - 'Sweet Child O' Mine' by Guns N' Roses")
            
    # This 'else' block below is where the message for wrong input is handled.
    # It catches any input that is not 'happy', 'sad', 'focus', or 'workout'.
    else:
        print(f"Sorry, '{user_mood}' is not a valid option.")
        print("Please run the program again and choose one of the following moods:")
        print("Happy, Sad, Focus, or Workout.")
            
    print("\n---------------------------")
    print("Enjoy your music!")


# This line runs the main function when the script is executed.
if __name__ == "__main__":
    recommend_playlist()