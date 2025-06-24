# allow a user to enter their user name and authentiate their password

print("enter your user name")
user_name = input()
print("enter your password")
password = input()
if user_name == "Francis" and password == "123456789":
    print("Authentication successful")
else:
    print("Authentication failed")

while user_name != "Francis" or password != "123456789":
    print("Authentication failed, please try again")
    print("enter your user name")
    user_name = input()
    print("enter your password")
    password = input()



# != is not equal to
# == is equal to
# () is used to group conditions "parentheses"