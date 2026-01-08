def library_details(ID, title, Author, Year):
    result = (
        "Book ID: {ID}\n",
        "Book Title: {title}\n",
        "Author Name: {Author}\n",
        "Year Of Publication: {Year}\n"
    )
    return result

if __name__ == "__main__" :
    ID = "1001"
    title = "Train Dreams"
    Author = "Dennis J"
    Year = "2015"
    print(library_details(ID, title, Author, Year))