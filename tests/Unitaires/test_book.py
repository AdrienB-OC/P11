def test_book_ok(client):
    response = client.get('/book/Fall Classic/Simply Lift')

    assert response.status_code == 200
    assert b'Booking for Fall Classic' in response.data


def test_book_error(client):
    response = client.get('/book/Wrong Comp/Wrong Club')

    assert response.status_code == 200
    assert b'Booking for Wrong Comp' not in response.data
