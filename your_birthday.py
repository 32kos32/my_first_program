user_name=''
while len(user_name.strip())<1:
    print('hi what’s your name?')
    user_name = input()
    print('great', '' + user_name + '!')

global_years=''
while len(global_years.strip())<1:
    print('and what year is it?')
    global_years = input()
    print('thats', '', global_years)

your_birthday=''
while len(your_birthday.strip())<1:
    print('in what year you were born?')
    your_birthday = input()
    print('yours', '', your_birthday)
    a = (int(global_years) - int(your_birthday))
    print(str('Youre') + str(' ') + str(a) + str(' ') + user_name)