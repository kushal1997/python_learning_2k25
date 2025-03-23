
correct_pwd = "hello world"

while True:
    pwd = input("Enter a password: ")
    print("validating your password ")
    
    if pwd == correct_pwd:
        print("u guessed the correct one")
        break
    else:
        print("WRONG password, ----------> guess the correct one")


