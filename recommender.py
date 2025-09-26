# LDCW6123 - Group Project: Part 2 Interactive Program
# Program Title: Spotify Playlist Recommendation Assistant

def recommend_playlist():
    """
    Main function to run the playlist recommender.
    """

    # Welcome message and instructions for the user.
    print("=====================================================")
    print(" Welcome to the Spotify Playlist Recommendation Assistant!")
    print("=====================================================")
    print("Tell us your mood, and we'll suggest a playlist for you.")
    print("Choose from: Happy, Sad, Focus, Workout\n")

    # Get user input.
    user_mood = input("Enter your current mood: ").strip().lower()

# This line runs the main function when the script is executed.
if __name__ == "__main__":
    recommend_playlist()