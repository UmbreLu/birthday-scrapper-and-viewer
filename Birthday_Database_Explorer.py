import json
import re
from matplotlib import pyplot as plt


# input handler for action choice
def input1():
    print('''

Enter an option:
(1) Consult scientist birthdays, view a list of all
scientists in the database and/or remove entries;
(2) Insert new scientist birthdays in the database;
(3) Visualize an histogram of birthdays per month;
(4) Exit the program.''')
    while True:
        valid_options = {'1', '2', '3', '4'}
        raw = input('<1/2/3/4> ')
        if raw in valid_options:
            return raw
        else:
            print('Not a valid option. Please insert a number from 1 through 4.')

def consult_function():
    consulting = True
    while consulting:
        raw = input('''

[Consulting]
(name) Type the name of the scientist you want to know
the birthday of.
(2) Type "2" to see a list all scientist names in
the database.
(3) Type "3" to remove an entry from the database.
(4) Type "4" to exit this consulting section.

<name/2/3/4> ''')
        if raw not in '234':
            scientist_name = raw.title()
            if scientist_name in bdays.keys():
                print(f'\n  {scientist_name} was born is {bdays[scientist_name]}.')
            else:
                print('This name wasn\'t found in the scientist birthday\ndatabase or you did\'t type ir correctly.')
        elif raw == '2':
            for name in bdays.keys():
                print('       ' + name)
        elif raw == '3':
            while True:
                raw2 = input('(name) Type the name of the scientist entry you want to remove.\n(2) Or type "2" to get to the previous options.\n<name/2> ').title()
                if raw2 in bdays.keys():
                    while True:
                        confirm = input(f'"{raw2}: born in {bdays[raw2]}".\nAre you sure you want to remove this entry?\n<yes/no> ')
                        if confirm == 'yes':
                            bdays.pop(raw2)
                            print('Entry removed from the database.\n')
                            break
                        elif confirm == 'no':
                            print('Discarted removal.\n')
                            break
                        else:
                            print('Invalid input. Type only "yes" or "no".\n')
                elif raw2 == '2':
                    break
                else:
                    print(f'{raw2} isn\'t found in the database.\n')
            with open('scientist_birthdays.json', 'w') as f:
                json.dump(bdays, f)
        else:
            consulting = False

def update_database():
    updating = True
    while updating:
        r_name = input('\n\n[Database Update]\nEnter a scientist name for new birthday entry:\n<name> ').title()
        r_bday = input(f'Enter {r_name}\'s birthday (e.g. 01/01/1900):\n<date> ')
        if re.search(r'^\d\d\/\d\d/\d\d\d\d$', r_bday) and re.search(r'^([a-zA-Zãáàäâéèêëíìîïóòõôöúùûü\'-]+)( /([a-zA-Zãáàäâéèêëíìîïóòõôöúùûü\'-]+))*', r_name):
            while True:
                confirmation = input(f'{r_name}: born in {r_bday}. Is it correct?\n<yes/no> ')
                if confirmation == 'yes':
                    bdays[r_name] = r_bday
                    print('Entry added to database.\n')
                    break
                elif confirmation == 'no':
                    print('Entry not added.\n')
                    break
                else:
                    print('Invalid input.')
        else:
            print('Invalid name or birthday.\nMake sure it\'s in the correct format (e.g. 01/01/1900)\n.')
                
        while True:
            again = input('\nWant to try a new entry?\n<yes/no> ')
            if again == 'no':
                updating = False
                break
            elif again == 'yes':
                break
            else:
                print('Invalid input.')
    with open('scientist_birthdays.json', 'w') as f:
        json.dump(bdays, f)

def view_data():
    data_array = []
    month_array = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    quantity_array = []
    for date in bdays.values():
        data_array.append(int(date[:2]))
    for x in range(1, 13):
        quantity_array.append(data_array.count(x))
    plt.bar(month_array, quantity_array, color='grey')
    plt.title('Birthdays Distribution')
    plt.xlabel('Month')
    plt.ylabel('Birthdays')
    plt.show()

        

# global scope ------------------------------------------------
print('''
===================================================
               Scientist Birthdays
===================================================

    Welcome! In Scientist Birthdays you can discover
your favorite scientist's birthday and also visualize
how they spread through the year.

    If you don't find you favorite scientist data,
don't worry, you can also add them yourself!

    Enjoy!

''')


# program main loop
exit_ = False # consult or feed or view
while not exit_:

    with open('scientist_birthdays.json', 'r') as f:
        bdays = json.load(f)


    # action choice
    choice = input1()
    if choice == '1':
        consult_function()
    elif choice == '2':
        update_database()
    elif choice == '3':
        view_data()
    else:
        exit_ = True
        print('See ya...')
