from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, item_id, title, author, year,):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.year = year
        self.available = True
       

    @abstractmethod
    def display_info(self): #the concept of inheritance: inheriting the abstract method and nothing more hence the term "pass"
        pass


class Book(LibraryItem):
    def __init__(self, item_id, title, author, year, genre):
        super().__init__(item_id, title, author, year)
        self.genre = genre

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"[BOOK] ID: {self.item_id} | Title: {self.title} | Author: {self.author} | "
              f"Year: {self.year} | Genre: {self.genre} | Status: {status}")


class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, year, issue_number):
        super().__init__(item_id, title, author, year)
        self.issue_number = issue_number

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"[MAGAZINE] ID: {self.item_id} | Title: {self.title} | Author: {self.author} | "
              f"Year: {self.year} | Issue: {self.issue_number} | Status: {status}")


class Library:
    def __init__(self):
        # Using a dictionary: key = item_id, value = LibraryItem object
        self.items = {}

    def add_item(self, item):
        if item.item_id in self.items:
            print("An item with this ID already exists.")
        else:
            self.items[item.item_id] = item
            print("Item added successfully.")

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item removed successfully.")
        else:
            print("Item not found.")

    def borrow_item(self, item_id):
        if item_id not in self.items:
            print("Item not found.")
            return

        item = self.items[item_id]
        if not item.available:
            print("Item is currently not available.")
        else:
            item.available = False
            print(f"You have borrowed: {item.title}")

    def return_item(self, item_id):
        if item_id not in self.items:
            print("Item not found.")
            return

        item = self.items[item_id]
        if item.available:
            print("This item was not borrowed.")
        else:
            item.available = True
            print(f"You have returned: {item.title}")

    def view_available_items(self):
        print("\n--- Available Items ---")
        found = False
        for item in self.items.values():
            if item.available:
                item.display_info()
                found = True
        if not found:
            print("No available items at the moment.")

            print("No items in the library.")
            return
        for item in self.items.values():
            item.display_info()

    def search_items(self, keyword):
        print(f"\n--- Search Results for '{keyword}' ---")
        keyword_lower = keyword.lower()
        found = False
        for item in self.items.values():
            if keyword_lower in item.title.lower() or keyword_lower in item.author.lower():
                item.display_info()
                found = True
        if not found:
            print("No items matched your search.")


def print_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Add Magazine")
    print("3. Remove Item")
    print("4. Borrow Item")
    print("5. Return Item")
    print("6. View Available Items")
    print("7. View All Items")
    print("8. Search Items")
    print("9. Exit")


def main():
    library = Library()

    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            # Add Book
            item_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            year = input("Enter Year: ").strip()
            genre = input("Enter Genre: ").strip()
            book = Book(item_id, title, author, year, genre)
            library.add_item(book)

        elif choice == "2":
            # Add Magazine
            item_id = input("Enter Magazine ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            year = input("Enter Year: ").strip()
            issue_number = input("Enter Issue Number: ").strip()
            magazine = Magazine(item_id, title, author, year, issue_number)
            library.add_item(magazine)

        elif choice == "3":
            # Remove Item
            item_id = input("Enter Item ID to remove: ").strip()
            library.remove_item(item_id)

        elif choice == "4":
            # Borrow Item
            item_id = input("Enter Item ID to borrow: ").strip()
            library.borrow_item(item_id)

        elif choice == "5":
            # Return Item
            item_id = input("Enter Item ID to return: ").strip()
            library.return_item(item_id)

        elif choice == "6":
            # View Available Items
            library.view_available_items()

        elif choice == "7":
            # View All Items
            library.view_all_items()

        elif choice == "8":
            # Search Items
            keyword = input("Enter title or author to search: ").strip()
            library.search_items(keyword)

        elif choice == "9":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()

    #application may run on port=5000)
