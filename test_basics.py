from main import read_item

def test_the_universe_didnt_explode():
    assert 1 + 1 == 2

def test_read_item():
    assert read_item(5, "hello") == {"item_id": 5, "q": "hello"}
