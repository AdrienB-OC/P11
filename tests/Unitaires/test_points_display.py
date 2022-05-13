def test_points_display(client):
    response = client.get('/points')
    assert response.status_code == 200
    assert b"Simply Lift : 13" in response.data
    assert b"Iron Temple : 4" in response.data
    assert b"She Lifts : 12" in response.data
