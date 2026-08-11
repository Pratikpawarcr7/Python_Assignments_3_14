# ==========================================================
# 1. BookStore Class
# ==========================================================

# Problem:
# Write a Python program to implement a class named BookStore
# with the following specifications:
#
# 1. The class should contain two instance variables:
#    Name   - Book Name
#    Author - Book Author
#
# 2. The class should contain one class variable:
#    NoOfBooks - Initialize it to 0.
#
# 3. Define a constructor __init__() that accepts Name and
#    Author and initializes the instance variables.
#
# 4. Inside the constructor, increment the class variable
#    NoOfBooks by 1 whenever a new object is created.
#
# 5. Implement the following instance method:
#
#    Display()
#    - Displays the book details in the following format:
#
#    <BookName> by <Author>. No of books: <NoOfBooks>
#
#    Example:
#   
#    Obj1 = BookStore("Linux System Programming", "Robert Love")
#    Obj1.Display()
#   
#    Output:
#    Linux System Programming by Robert Love. No of books: 1
#   
#    Obj2 = BookStore("C Programming", "Dennis Ritchie")
#    Obj2.Display()
#   
#    Output:
#    C Programming by Dennis Ritchie. No of books: 2
#   
# ==========================================================

class BookStore:

    noOfBooks = 0

    def __init__(self,b_Name,a_Name):
        self.Name = b_Name
        self.Author = a_Name

        BookStore.noOfBooks = BookStore.noOfBooks + 1

    def Display(self):

        print(self.Name,"is",self.Author,". No of Books : ",BookStore.noOfBooks)


def main():
    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display()


    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display()
if __name__ == "__main__":
    main()