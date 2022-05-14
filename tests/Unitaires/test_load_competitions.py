from server import load_competitions


expected = [
    {'name': 'Spring Festival', 'date': '2020-03-27 10:00:00', 'numberOfPlaces': '25'},
    {'name': 'Fall Classic', 'date': '2022-10-22 13:30:00',
     'numberOfPlaces': '13'}]


def test_load_competitions():
    assert load_competitions() == expected
