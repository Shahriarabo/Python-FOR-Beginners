bank_user = { 'rasel': 50088, 'sakib': 3075, 'shahin': 3050}

print("Welcome to Bank ")

while True:
    print("What do you like to do ?")
    print('  ' + ' 1 => View Blance')
    print('  ' + ' 2 => View all bank info')
    print('  ' + ' 3 => Update Blance')
    print('  ' + ' 4 => Exit')

    desc = input()
    if desc == '1':
        print("Enter the Name. PLease: ")
        name = input()
        if name in bank_user.keys():
            print(name +' your Bank Blance is ' +  str(bank_user[name]))
        else:
            print("The uder can not found , Would like to add  user account?")
            desc= input()
            if desc == 'yes':
                name = ("Enter the Name. PLease: ")
                Blance = ("Enter the Blance. PLease: ")
                bank_user.update({name: Blance})
            else:
                print(" Would like to exit")
                desc= input()
                if desc == 'yes':
                    break


    elif desc == '2':
        
        desc= input()

        for name , Blance in bank_user.items():
            print("Username " + str(name)+"Blance " + str(Blance))

    elif desc == '3':
        
        desc= input()
        print("Enter the Name. PLease ")

        name = input()
        if name in bank_user.keys():
            print(" Do you want to add or subtract from your saving ?")

            desc = input()
            if desc== 'add':
                new_Blance = bank_user[name]
                add_Blance = input(" Please Enter your amount do you want  add :  ")
                bank_user[name]=new_Blance + int(add_Blance)
                print("Blance UPdate . it is :")
                print(bank_user[name])
                
            elif desc== 'sub':
                old_Blance = bank_user[name]
                sub_Blance = input(" Please Enter your amount do you want subtract :  ")
                bank_user[name]=old_Blance - int(sub_Blance)
                print("Blance UPdate . it is :")
                print(bank_use[name])

            else:
                print("There is no such account in the Bnak databess !")

    elif desc == '4':
        break

            
                
                
     
