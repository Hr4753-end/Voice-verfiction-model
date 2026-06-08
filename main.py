from recorder import record_audio
from enroll import enroll_user
from verify import verify_user

SAMPLE_RATE = 16000
DURATION_SECONDS = 5


def main():
    print("1. Enroll")
    print("2. Verify")

    choice = input("Choose: ")
    username = input("Username: ")

    if choice == "1":
        filename = f"{username}_enroll.wav"
        record_audio(filename, DURATION_SECONDS, SAMPLE_RATE)
        print(enroll_user(username, filename))
    elif choice == "2":
        filename = f"{username}_verify.wav"
        record_audio(filename, DURATION_SECONDS, SAMPLE_RATE)
        result = verify_user(username, filename)
        print(result)
    else:
        print("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
