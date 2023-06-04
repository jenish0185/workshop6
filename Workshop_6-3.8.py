def sort_books(books):

    sorted_books = sorted(books, key=lambda book: book[1])
    return sorted_books

books = [('book by jenish', 'Jenish'),
         ('What is a woman?', 'Matt Walsh'),
         ('The Great Gatsby', 'F. Scott Fitzgerald')
         ]
sorted_books = sort_books(books)
print(sorted_books)