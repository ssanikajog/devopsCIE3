def library_details(id, title, Author, Year):
    result = (
        "Book ID: {id}\n",
        "Book Title: {title}\n",
        "Author Name: {Author}\n",
        "Year Of Publication: {Year}\n"
    )
    return result

if __name__ == "__main__" :
    id = "1001"
    title = "Train Dreams"
    Author = "Dennis J"
    Year = "2015"
    print(library_details(id, title, Author, Year))
