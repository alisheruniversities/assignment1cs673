def is_palindrome(s):
    return s == s[::-1]

def main():
    while True:
        user_input = input("Enter a string (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        if is_palindrome(user_input):
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")

if __name__ == "__main__":
    main()