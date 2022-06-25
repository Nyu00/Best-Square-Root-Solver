import os


def main():
    os.system("cls")

    try:
        print(f"""Welcome to the best Square Root Solver of the world
        """)

        choice_between_methods = int(input("""But we need to you select a method to resolve it
Press 1 to use the method proximity or press 2 to use the method binary search: """))

        assert choice_between_methods > 0 and choice_between_methods < 3, "problemon"

        


        print(f"Ok, you pressed {choice_between_methods}")

        if choice_between_methods == 1:
            metodo_1()
        elif choice_between_methods == 2:
                metodo_2()
    
    except AssertionError:
        print("Try again and choose a number between 1 or 2")



def metodo_2():
    goal_2 = int(input("Write a number: "))
    epsilon_2 = 0.01
    down = 0.0
    up= max(1.0,goal_2)
    answer_2 = ( up + down ) / 2

    while abs (answer_2 **2 - goal_2) >= epsilon_2:
    #optional        print(f"up = {up} down = {down} ,answer = {answer_2}")
        if answer_2 **2 < goal_2:
            down = answer_2
        else:
            up = answer_2

        answer_2 = (up + down) / 2
        answer_2 = round(answer_2,3)

    print(f"The square root of {goal_2} is {answer_2}")

def metodo_1():
    
    goal = int(input("Choose a interal number: "))
    epsilon = 0.01
    step = epsilon ** 2
    answer = 0.0


    while abs(answer**2 - goal) >= epsilon and answer <= goal:

        answer += step
    #optional too        print(answer)

    if abs(answer ** 2 - goal) >= epsilon:
        print(f"Not fount square root of {goal}")
    else:
        answer = round(answer,3)
        print(f"The square root of {goal} is {answer}")


if __name__ == '__main__':
    main()
