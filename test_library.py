from library import library_details

def test_library_details():
    expected_output = (
        f"Book ID: 1001\n"
        f"Book Title: Train Dreams\n"
        f"Author Name: Dennis J\n"
        f"Year Of Publication: 2015\n"
    )

    assert library_details("1001", "Train Dreams", "Dennis J", "2015" == expected_output)
