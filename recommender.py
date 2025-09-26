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

    if user_ood == "happy":
        # Output for 'happy' mood
        print("Playlist Suggestion: 'Happy Hits!'")
        print("Description: Feel-good tracks to boost your mood and make you smile.")
        print("Songs you might like:")
        print("  - 'Happy' by Pharrell Williams")
        print("  - 'Good as Hell' by Lizzo")
        print("  - 'Walking on Sunshine' by Katrina & The Waves")

    elif user_mood == "sad":
        # Output for 'sad' mood
        print("Playlist Suggestion: 'Sad Indie'")
        print("Description: Mellow and emotional tracks for reflective moments.")
        print("Songs you might like:")
        print("  - 'To Build A Home' by The Cinematic Orchestra")
        print("  - 'I Will Follow You into the Dark' by Death Cab for Cutie")
        print("  - 'skinny love' by Bon Iver")

    elif user_mood == "focus":
        # Output for 'focus' mood
        print("Playlist Suggestion: 'Deep Focus'")
        print("Description: Ambient and instrumental music to help you concentrate.")
        print("Songs you might like:")
        print("  - 'Music for Airports 1/1' by Brian Eno")
        print("  - 'Nuvole Bianche' by Ludovico Einaudi")
        print("  - 'Clair de Lune' by Claude Debussy")

    elif user_mood == "workout":
        # Output for 'workout' mood
        print("Playlist Suggestion: 'Beast Mode'")
        print("Description: High-energy tracks to power you through your workout.")
        print("Songs you might like:")
        print("  - 'Till I Collapse' by Eminem")
        print("  - 'POWER' by Kanye West")
        print("  - 'Can't Hold Us' by Macklemore & Ryan Lewis")

    else:
        # This 'else' block handles cases where the user input doesn't match
        # the choices, which is part of good user experience/error handling.
        print(f"Sorry, we don't have a recommendation for '{user_mood}'.")
        print("Please try one of the suggested moods: Happy, Sad, Focus, Workout.")

    print("\n---------------------------")
    print("Enjoy your music!")


# This line runs the main function when the script is executed.
if __name__ == "__main__":
    recommend_playlist()