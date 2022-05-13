def test_purchase_ok(client):
    response = client.post('/purchasePlaces',
                           data={"competition": "Spring Festival",
                                 "club": "Simply Lift",
                                 "places": "3"})

    assert b'Great-booking complete!' in response.data


def test_purchase_error_points(client):
    response = client.post('/purchasePlaces',
                           data={"competition": "Fall Classic",
                                 "club": "Iron Temple",
                                 "places": "10"})

    assert b'Great-booking complete!' not in response.data
    assert response.status_code == 200


def test_purchase_error_places(client):
    response = client.post('/purchasePlaces',
                           data={"competition": "Fall Classic",
                                 "club": "Iron Temple",
                                 "places": "15"})

    assert b'Great-booking complete!' not in response.data
    assert response.status_code == 200

