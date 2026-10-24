#Faizan Library System
class Book :
    def __init__(self,title,author,__price,is_issued): #
        self.title=title
        self.author=author
        self.__price=__price
        self.is_issued=is_issued

    def display_info(self): 
     print("Title :",self.title)
     print("Author :",self.author)
     print("Rs .",self.__price)
     if self.is_issued:
        print("Status : Issued")
     else:
        print("Status : Available")   

    def issue_book(self): 
     if self.is_issued:
        print("Sorry, this book is already issued!")
     else:
        self.is_issued = True
        print("Book issued successfully!")

    def return_book(self): 
     if self.is_issued:
        self.is_issued = False
        print("Book returned successfully!")
     else:
        print("This book has not been issued!")

         
class LibraryInfo:
    student_id="Faizan@321"
    def __init__(self,library_name,books): 
        self.library_name=library_name
        self.books=books
        print("Welcome in ",self.library_name)

    @staticmethod
    def library_rules(): 
        print("LIBRARY RULES \n1.Return books on time \n2.Keep books safe \n3.Maintain Silence in Library") 
      

    def add_book(self): 
       print("1.Physical Book")
       print("2.EBook")
       choice=input("Choose an Option (1-2)")
       if choice == '1':   
         title=input("Book Title: ")
         author=input("Author : ")
         price=int(input("Price : "))
         is_issued=False
         new_book=Book(title,author,price,is_issued)
         self.books.append(new_book)
         print("Book Added Successfully")

       elif choice == '2':
        title=input("Book Title: ")
        author=input("Author : ")
        __price=int(input("Price : "))
        is_issued=False
        file_size=input("File_Size : ")
        new_ebook=EBook(title,author,__price,is_issued,file_size)
        self.books.append(new_ebook)
        print("Book Added Successfully")

       else:
         print("Invalid Choice ! Please Select 1 or 2.")
    
    def show_books(self): 
      if not self.books :
       print("No books Available in the library")
      else: 
       for book in self.books: 
        book.display_info()
    
        

    def find_book(self): 
     book_title=input("Enter Book Title : ").strip()
     found=False

     for book in self.books:
        if book.title.strip().lower() == book_title.lower():
           book.display_info()
           found=True
           break
     if not found:
           print("Book wasn't Found")   

    def issue_library_book(self):
     book_title=input("Enter Book Title : ").strip()
     for book in self.books:
      if book.title.strip().lower() == book_title.lower():
         book.issue_book()
         return
     print("Book wasn't Found")
 

    def return_library_book(self):
     book_title = input("Enter Book Title: ").strip()

     for book in self.books:
      if book.title.strip().lower() == book_title.lower():
         book.return_book()
         return

     print("Book wasn't Found")

    def library_menu(self):
       student_id=input("Enter Your ID # :")
       if student_id == self.student_id:
        while True:
         print("1.Library_rules.")
         print("2.Add_book.")
         print("3.Show_books.")
         print("4.Find_book.")
         print("5.Issue_library_book.")
         print("6.Return_library_book.")
         print("7.Exit.")
         choose=input("Select an Option (1-7) : ")
         if choose == '1' :
          self.library_rules()
       
         elif choose == '2':
          
          self.add_book()
       
         elif choose == '3':
          self.show_books()
       
         elif choose == '4' :
          self.find_book()

         elif choose == '5' :
          self.issue_library_book()

         elif choose == '6' :
          self.return_library_book()

         elif choose == '7' :
           print("Thanks ! Keep Learning // Take Care")   
           break        
         else:
          print("Incorrect Command , Please Try Again") 
       else:
         print("INVALID ID ! , TRY AGAIN ")

class EBook(Book):
   def __init__(self, title, author, __price, is_issued,file_size):
    super().__init__(title,author,__price,is_issued)
    self.file_size=file_size

   def display_info(self):
    super().display_info()
    print("File_size : ",self.file_size)

   
lb= LibraryInfo("Faizan Library System : ",[])
lb.library_menu()
