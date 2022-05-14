def test_summary_ok(client):
    response = client.post('/showSummary',
                           data={"email": "john@simplylift.co"})

    assert response.status_code == 200
    assert b"Welcome, john@simplylift.co" in response.data
    assert b"Book Places" in response.data
    assert b"book/Fall%20Classic/Simply%20Lift" in response.data


def test_summary_invalid_email(client):
    response = client.post('/showSummary',
                           data={"email": "wrong@email.com"})

    assert response.status_code == 200
    assert b"Error : Unregistered email" in response.data
