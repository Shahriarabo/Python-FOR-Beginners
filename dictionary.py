contact = { 'rasel': 50088, 'sakib': 3075, 'shahin': 3050}
x= 0

while x < 5:
    print("Enter the Name (pess ENTER to exit) ")
    name = input()

    if name == '':
        break

    if name in contact:
        print("The contact number of "+ name + "  is  " + str(contact[name]))
    else:
        print(" There are no sure name in the Phnoe_book . Do you want to add it ?")
        disc= input()

        if disc == 'yes':
            print("Enter the Number ")
            num = input()
            contact[name]= num
            print("DICtionary Update")

        elif disc == 'no':
            print("Do you want to quit? ")
            disc= input()

            if disc == 'yes':
                break
            else:
                print("Keep sreaching")

    x= x+1
            
    
        
    

