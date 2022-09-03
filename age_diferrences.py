import os


def main():

    user_1 = input('Hi whats popping whats your name?: ')

    print('Cute name :)')

    user_age1 = int(input('How old are you?: '))

#////////////////////////////////////////////////////////////////////////

    user_2 = input('and what is your friends name: ')

    print('Cute name too :)')

    user_age2 = int(input('and how old is your friend?: '))


    if user_age1 > user_age2 :

        print(f'{user_1} has {user_age1} years old and {user_2} has {user_age2} years old so {user_1} is older than {user_2} :) ')

    elif user_age1 < user_age2:

        print(f'{user_1} has {user_age1} years old and {user_2} has {user_age2} years old so {user_1} is younger than {user_2} :) ')

    else: 

        print(f'{user_1} and {user_2} have both {user_age1} years old thats so cool <3')




if __name__ == '__main__':
    os.system("cls")
    main()
