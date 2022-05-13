def test_comp_places_update(client):
    resp = client.get('/points')

    assert resp.status_code == 200
    assert b"<td>Simply Lift</td>\n                    <td>13</td>" \
           in resp.data
    assert b"<td>Iron Temple</td>\n                    <td>4</td>" \
           in resp.data
    assert b"<td>She Lifts</td>\n                    <td>12</td>" \
           in resp.data

    response = client.post('/showSummary',
                           data={"email": "john@simplylift.co"})

    assert response.status_code == 200
    assert b"Welcome, john@simplylift.co" in response.data
    assert b"Book Places" in response.data
    assert b"book/Fall%20Classic/Simply%20Lift" in response.data
    assert b'Number of Places: 13' in response.data
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
    assert b'Number of Places: 10' in response_3.data
    assert b'Points available: 10' in response_3.data

    response_4 = client.get('/logout')
    assert response_4.status_code == 302

    response_5 = client.get('/points')

    assert response_5.status_code == 200
    assert b"<td>Simply Lift</td>\n                    <td>10</td>" \
           in response_5.data
    assert b"<td>Iron Temple</td>\n                    <td>4</td>" \
           in response_5.data
    assert b"<td>She Lifts</td>\n                    <td>12</td>" \
           in response_5.data
