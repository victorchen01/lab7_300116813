def create_books_2Dlist(file_name):

    temp = open(file_name).read().splitlines()

    book_table = []

    for book in temp:
        book = book.split("\t")
        title = book[0].strip()
        name = book[1].strip()
        publisher = book[2].strip()
        a = book[3].strip().split("/")
        year = a[2] + "-" + a[0] + "-" + a[1]
        genre = book[4].strip()
        book_table.append( [year, title, name, publisher, genre] )

    return book_table

def search_by_year(books, year1, year2):

    for i in range(len(books)):
        if(int(books[i][0].split("-")[0]) <= year2 and int(books[i][0].split("-")[0]) >= year1):
            print(books[i])
    

book_table = create_books_2Dlist("NYT_long.txt")
search_by_year(book_table, 1980, 2000)    
