from models.address_book import AddressBook
from models.record import Record

if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
    else:
        print("Contact not found")
    print(john)

    if john:
        found_phone = john.find_phone("5555555555")
    else:
        found_phone = None
    if john and found_phone:
        print(f"{john.name}: {found_phone}")
    else:
        print("Phone not found")

    book.delete("Jane")
