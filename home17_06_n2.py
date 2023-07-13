def contact_book() :
    contacts = {}
    n = True
    while n :
        a = """
        1. Add a new contact!
        2. Search for a contact!
        3. List all contacts!
        4. Exit

    """ 
        print(a)

        my_input = input("Select wanted action!")
        while not my_input.isnumeric():
            print('Please enter only numbers')
            my_input = input("Select wanted action!")

        my_input = int(my_input)

        if my_input == 4 :
            print("See you soon!")
            n = False
        if my_input == 1:
            name = input("Please , enter name of the contact! ")
            number = input("Please , enter number of contact! ")
            contacts[name] =  number
            print("Contact added successfully!")
        if my_input == 3:
            for name , number in contacts.items() :
                print(name , number)
        if my_input == 2 :
            name1 = input("Please , enter wanted name!")
            if name1 in contacts.keys():
                print(contacts[name1])
            else:
                print("Contact does not exist.")
contact_book()