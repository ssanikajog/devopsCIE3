from library import library_details

def test_library_details():
    expected_output = (
        "Book ID: 1001\n",
        "Book Title: Train Dreams\n",
        "Author Name: Dennis J\n",
        "Year Of Publication: 2015\n"
    )

    assert (library_details("1001", "Train Dreams", "Dennis J", "2015")) == expected_output
