def test_points_display(client):
    response = client.get('/points')
    assert response.status_code == 200
    assert b"<td>Simply Lift</td>\n                    <td>13</td>" \
           in response.data
    assert b"<td>Iron Temple</td>\n                    <td>4</td>" \
           in response.data
    assert b"<td>She Lifts</td>\n                    <td>12</td>" \
           in response.data
