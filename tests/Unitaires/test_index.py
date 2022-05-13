def test_status_ok(client):
    response = client.get('/')
    assert b"<h1>Welcome to the GUDLFT Registration Portal!</h1>" in \
           response.data
