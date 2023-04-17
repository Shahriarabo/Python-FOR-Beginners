
#def fibo(n):
 #   if n == 0:
  #      return 0
   # return 1 + fibo (n//10)

#print(fibo(1234567891011121314151617181920))


#def expolad(x ,y):
#   if y == 0:
 #       return 1
  #  return x * expolad(x ,y-1)

#print(expolad(2,3))




def expolad(x ,y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return expolad(x,y//2)*expolad(x,y//2)
    else:
        return x*expolad(x,y//2)*expolad(x,y//2)

print(expolad(9,4))
