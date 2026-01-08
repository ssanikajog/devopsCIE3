def library_details(id, title, Author, Year):
    result = (
        f"Book ID: {id}\n"
        f"Book Title: {title}\n"
        f"Author Name: {Author}\n"
        f"Year Of Publication: {Year}\n"
    )
    return result

if __name__ == "__main__" :
    id = "1001"
    title = "Train Dreams"
    Author = "Dennis J"
    Year = "2015"
    print(library_details(id, title, Author, Year))
