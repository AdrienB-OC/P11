from server import load_clubs


expected = [
    {'name': 'Simply Lift', 'email': 'john@simplylift.co', 'points': '13'},
    {'name': 'Iron Temple', 'email': 'admin@irontemple.com', 'points': '4'},
    {'name': 'She Lifts', 'email': 'kate@shelifts.co.uk', 'points': '12'}]


def test_load_clubs():
    assert load_clubs() == expected
