def test_comp_places_update(client):
    response = client.post('/showSummary',
                           data={"email": "john@simplylift.co"})

    assert response.status_code == 200
    assert b"Welcome, john@simplylift.co" in response.data
    assert b"Book Places" in response.data
    assert b"book/Fall%20Classic/Simply%20Lift" in response.data
    assert b'Points available: 13' in response.data

    response_2 = client.get('/book/Fall Classic/Simply Lift')

    assert response_2.status_code == 200
    assert b'Booking for Fall Classic' in response_2.data
    assert b'Places available: 13' in response_2.data

    response_3 = client.post('/purchasePlaces',
                             data={"competition": "Fall Classic",
                                   "club": "Simply Lift",
                                   "places": "3"})

    assert b'Great-booking complete!' in response_3.data
    assert b'Points available: 4' in response_3.data

