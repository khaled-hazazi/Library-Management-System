import getpass
import mysql.connector


def add_book(connection, cursor):
    title = input("Book title: ").strip()
    author = input("Author: ").strip()
    category = input("Category: ").strip()

    if not title or not author or not category:
        print("Please fill in all fields.")
        return

    if len(title) > 200 or len(author) > 150 or len(category) > 100:
        print("One of the fields is too long.")
        return

    cursor.execute(
        "INSERT INTO books (title, author, category) VALUES (%s, %s, %s)",
        (title, author, category)
    )
    connection.commit()
    print("Book added successfully.")


def display_books(cursor):
    cursor.execute(
        "SELECT book_id, title, author, category FROM books ORDER BY book_id"
    )
    show_results(cursor.fetchall())


def search_books(cursor):
    title = input("Enter a book title to search: ").strip()

    if not title:
        print("Please enter a title.")
        return

    cursor.execute(
        "SELECT book_id, title, author, category "
        "FROM books WHERE title LIKE %s ORDER BY book_id",
        ("%" + title + "%",)
    )
    show_results(cursor.fetchall())


def show_results(books):
    if not books:
        print("No books found.")
        return

    for book_id, title, author, category in books:
        print(f"\nID: {book_id}")
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Category: {category}")


def main():
    connection = None
    cursor = None

    try:
        password = getpass.getpass("MySQL password: ")

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=password,
            database="library_project"
        )
        cursor = connection.cursor()

        while True:
            print("\n--- Library Management ---")
            print("1. Add a book")
            print("2. Display all books")
            print("3. Search for a book")
            print("4. Exit")

            choice = input("Choose an option: ").strip()

            try:
                if choice == "1":
                    add_book(connection, cursor)
                elif choice == "2":
                    display_books(cursor)
                elif choice == "3":
                    search_books(cursor)
                elif choice == "4":
                    print("Goodbye!")
                    break
                else:
                    print("Please choose a number from 1 to 4.")
            except mysql.connector.Error as error:
                connection.rollback()
                print(f"Database error: {error}")

    except mysql.connector.Error as error:
        print(f"Connection error: {error}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    main()