MAX_BOOK_NAME_TITLE_LENGTH = 30
#Handles the the strings by replacing unwanted characters with empty string
def handling_strings(the_string):
    non_wanted_characters = "#$,^%/()="
    for character in non_wanted_characters:
        the_string = the_string.replace(character,"")
    #Handling spaces that if user enters space before or after of input
    the_string=the_string.strip()
    #Handles lower case or upper case inputs
    the_string=the_string.lower()
    the_string=the_string.title()
    return the_string

class Library:
    #Consturctor
    def __init__(self,file="books.txt"):
        self.file = open("books.txt","a+")
    #Destructor
    def __del__(self):
        self.file.close()
    #Lists the books
    def list_books(self):
        print("Listed books:\n")
        #Opening the file in read mode
        self.file = open("books.txt","r")
        contents=self.file.read()
        lines=contents.splitlines()
        the_list=[]
        for line in lines:
            #Convert every lines into the list recognizing them by seperating value which is ,(comma)
            temp_list=line.split(sep=",")
            #Creating directory for practical uses
            temp_dict=[("Book Name",temp_list[0]),
                       ("Author",temp_list[1]),
                       ("Release Date",temp_list[2]),
                       ("Number Of Pages",temp_list[3]),
                       ]
            temp_dict=dict(temp_dict)
            the_list.append(temp_dict)
        
        print("Book    Author")
        for book in the_list:
            #For more aesthetic look
            length_book=len(book["Book Name"])
            length_space=MAX_BOOK_NAME_TITLE_LENGTH - length_book
            new_space=" " * length_space
            print(book["Book Name"],new_space,book["Author"])
        #Converting file mode back to a+
        self.file = open("books.txt","a+")


    def add_books(self):
        print("Adding Book:")
        #Taking prompts from user about title,author,release year and number of pages
        book_title=input("Enter the title of the book:")
        book_title=handling_strings(book_title)

        book_author=input("Enter the author of the book:")
        book_author=handling_strings(book_author)

        book_release_year=input("Enter the release year of the book:")
        book_release_year=handling_strings(book_release_year)

        book_number_of_pages=input("Enter number of pages of the book:")
        book_number_of_pages=handling_strings(book_number_of_pages)

        book_string=(f"{book_title},{book_author},{book_release_year},{book_number_of_pages}\n")
        self.file.write(book_string)

    def remove_books(self):
        remove_book_title=input("Enter the title of the book that will be removed from the database:")
        remove_book_title=handling_strings(remove_book_title)
        
        self.file = open("books.txt","r")
        contents=self.file.read()
        lines=contents.splitlines()
        the_list=[]
        for line in lines:
            temp_list=line.split(sep=",")
            temp_dict=[("Book Name",temp_list[0]),
                       ("Author",temp_list[1]),
                       ("Release Date",temp_list[2]),
                       ("Number Of Pages",temp_list[3]),
                       ]
            temp_dict=dict(temp_dict)
            the_list.append(temp_dict)

        is_book_found=False #Boolean variable for if the removed book is found or not
        for book in the_list:
            if(book["Book Name"]==remove_book_title):
                print("The book is found deleting it.")
                the_list.remove(book)
                is_book_found=True #Book is found setting boolean variable to True
                break

        if is_book_found:
            self.file = open("books.txt","w")
            self.file.truncate(0)
            for book in the_list:
                values_of_book=list(book.values())
                values_of_book=','.join(values_of_book)
                values_of_book=values_of_book+"\n"
                self.file.write(values_of_book)
            self.file = open("books.txt","a+")
        else:
            print("The book is not found or prompted book name is wrong")


lib = Library()
while True:
    #MENU
    print("***MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Quit the program")
    choice = input("Enter your choice:")
    #Choices
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_books()
    elif choice == "3":
        lib.remove_books()
    elif choice == "Q" or choice == "q":
        break
    else:
        print("Invalid Choice")

