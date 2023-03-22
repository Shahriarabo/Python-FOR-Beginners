Password_bank = { 'rasel': 50088, 'sakib': 3075, 'shahin': 3050}
matched = False
print("Enter the Name ")

x = 0

while x < 5 :
     name = input()
     if name in  Password_bank:
         for i in range(0,3):
             print("Emter the Password")
             password= input()
             if int(password) in Password_bank.values():
                 print(" Successfully ")
                 matched = True
                 break
             else:
                 print(" Don't Success")

     else:
        print(" Don't found . please try again ")
x=x+1
     
