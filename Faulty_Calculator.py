print("Calculator made by Ashish")
restart = ('Y')

while restart != ['n', 'no', 'N', 'NO']:
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    print("Press Option 1 for Addition \n ")
    print("Press Option 2 for subtraction \n ")
    print("Press Option 3 for Multiplication \n ")
    print("Press Option 4 for Division \n ")
    print("Press Option 5 for Modules \n ")
    print("Press Option 6 for Power \n ")

    option = int(input("Enter your option : "))
    if a == 45 or 3 and b == 3 or 45 and option == 3:  # gives wrong answer if a = 45,3 and b = 3,45 and option is multiplication
        print(a," * ",b," = ",555)
        restart = input('Press Y to go back : ')
        if restart in ['n', 'no', 'N', 'NO']:
            print('Thank You')
            break

    elif a == 56 and b == 6 and option == 4:  # gives wrong answer if a = 56 and b = 6 and option is division
        print(a," / ",b," = ",4)
        restart = input('Press Y to go back : ')
        if restart in ['n', 'no', 'N', 'NO']:
            print('Thank You')
            break

    elif a == 56 or 9 and b == 9 or 56 and option == 1:  #gives wrong answer if a = 56,9 and b = 9,56 and option is addition
        print(a," + ",b," = ",77)
        restart = input('Press Y to go back : ')
        if restart in ['n', 'no', 'N', 'NO']:
            print('Thank You')
            break

    else:
        if option == 1:
            print(a, "+ ", b" is : ", a + b)
            restart = input('Press Y to go back : ')
            if restart in ['n', 'no', 'N', 'NO']:
                print('Thank You')
                break

        elif option == 2:
            print(a, " - ", b, " is : ", a - b)
            restart = input('Press Y to go back : ')
            if restart in ['n', 'no', 'N', 'NO']:
                print('Thank You')
                break

        elif option == 3:
            print(a, " * ", b, " is : ", a * b)
            restart = input('Press Y to go back : ')
            if restart in ['n', 'no', 'N', 'NO']:
                print('Thank You')
                break

        elif option == 4:
            print(a, " / ", b, " is : ", a / b)
            restart = input('Press Y to go back : ')
            if restart in ['n', 'no', 'N', 'NO']:
                print('Thank You')
                break

        elif option == 5:
            print(a, " % ", b, " is : ", a % b)
            restart = input('Pres Y to go back : ')
            if restart in ['n', 'no', 'N', 'NO']:
                print('Thank You')
                break

        elif option == 6:
            print(a, " ^ ", b, " is : ", a ** b)
            restart = input('Press Y to go back : ')
            if restart in ['n', 'no', 'N', 'NO']:
                print('Thank You')
                break
        else:
            print('Enter a Invalid Option \n')
            restart = ('Y')