from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a book
- 'l' to list all the books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Enter Choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_book()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown Command. Please try again.")

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input("Enter the new book name: ")
    author = input("Enter the new book author: ")
    database.add_book(name, author)


def list_book():
    books = database.get_all_books()
    for book in books:
        print(f"{book['name']} by {book['author']}, read: {book['read']}")


def prompt_read_book():
    name = input("Enter the name of the book you just read: ")
    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the name of the book you just finished reading: ")
    database.delete_book(name)


menu()
# def prompt_add_book() ask for book name and author
# def list_book() show all the books
# def prompt_read_book() change the status to read
# def prompt_delete_book() to delete a book
