# LDCW6123 - Group Project: Part 2 Interactive Program
# Program Title: Spotify Playlist Recommendation Assistant

def recommend_playlist():
    """
    Main function to run the playlist recommender.
    """

    print("=====================================================")
    print(" Welcome to the Spotify Playlist Recommendation Assistant!")
    print("=====================================================")
    print("Tell us your mood, and we'll suggest a playlist for you.")
    print("Choose from: Happy, Sad, Focus, Workout\n")

    user_mood = input("Enter your current mood: ").strip().lower()

    print("\n--- Your Recommendation ---")

    if user_mood == "happy":
        print("Playlist Suggestion: 'Happy Hits!'")
        print("Description: Feel-good tracks to boost your mood and make you smile.")

    elif user_mood == "sad":
        print("Playlist Suggestion: 'Sad Indie'")
        print("Description: Mellow and emotional tracks for reflective moments.")

    print("\n---------------------------")
    print("Enjoy your music!")

if __name__ == "__main__":
    recommend_playlist()