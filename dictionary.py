

credentials ={
    'username': "B334",
    'password': "1234"  
}

print(credentials['username'])

print('login system')

username = input('Enter your username: ')
password = input('Enter your password: ')

if username == credentials['username'] and password == credentials['password']:
    print('Login successful!')
else:
    print('Login failed. Please check your credentials.')




if username == credentials['username']:
    if password == credentials['password']:
        print('logged n successfully')
    else:
            print('Invalid password')
else:
    print('invalid username')





credentials ={
    'username': "B334",
    'password': "1234"  
}


print(f'initial dictionary:{credentials}')


# ####changing a value in a dictionary

credentials['username'] ="francs"


print(f'changed username:{credentials}')

# #adding another item to the dictionary

credentials["personal_email"] = "franciswagonda@gmail.com"

print(f'updated credential:{credentials}')



#### lists and dictionaries

students =[
    {'username': "B334", 'password': "123"},
    {'username': "B335", 'password': "12345"},
    {'username': "B336", 'password': "12346"},
    {'username': "B337", 'password': "12347"}
    
    ]

student = {
    'username': "B3323",
    'password': "1234"
}


students.append(student)
students.insert(1,student)

print(students)