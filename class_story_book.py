class StoryBook:

    number_of_book= 0

    discount = 0.5
    
    def __init__(self, name, price, pages):
        self.name = name
        self.price = price
        self.pages = pages
        self.pub = 2023
        StoryBook.number_of_book+=1

    def get_book_info(self):
        print(f'This is book name is: {self.name}, book price is:  {self.price}, book pages is {self.pages}')

    def apply_discount(self):
        self.price = int(self.price - self.price*self.discount)
        
book_one = StoryBook('Mukto bataser khoje', 900, 3000)
book_two = StoryBook('Mukto bataser khoje', 300, 9000)

#print("book  pub is ", book_one.pub)




#book_one.get_book_info()
#StoryBook.get_book_info(book_one)

# book_one.price = '400'

# book_two.name ='Aso shilhi'
# book_two.price = '400'


# print(book_one.name)
# print(book_two.name)


print(book_one.number_of_book)

print(book_one.price)
book_one.apply_discount()
print(book_one.price)
