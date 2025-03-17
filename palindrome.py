a = input("Enter a string").lower()
b = a[-1::-1]

if b == a:
    print("It is a palindrome:", b)
else:
    print("Not a palindrome")
