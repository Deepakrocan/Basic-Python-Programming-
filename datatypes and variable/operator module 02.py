def get_user_input():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    score = int(input('Enter your score: '))
    department = input('Enter your department: ')
    return name,age,score,department
def print_user_info():
    print('My name is', name)
    print('My age is', age)
    print('My score is', score / 10)
    print('My department is', department)

name,age,score,department= get_user_input()
print_user_info=( name,age,score,department)
