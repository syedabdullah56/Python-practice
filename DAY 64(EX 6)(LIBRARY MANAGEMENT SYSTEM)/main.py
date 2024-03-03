class MYLIBRARY:
    def __init__(self):
        self.noboks=0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)
    def showinfo(self):
        print(f'The library has {self.nobooks} books and they are')
        for book in self.books:
            print(book)

a=MYLIBRARY()
a.addbook("RICH DAD POOR DAD")
a.addbook("THINK AND GROW RICH")
a.addbook("INTRODUCTION TO ALGORITHMS")
a.addbook("THE 7 HABITS OF HIGHLY EFFECTIVE PEOPLE")
a.showinfo()