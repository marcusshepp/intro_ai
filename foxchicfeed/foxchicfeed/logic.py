from item import Item
from dock import Dock

fox_data = {
    "can_be_eaten": False,
    "eaten": False,
    "side": "left",
    "name": "fox"
}
fox = Item(**fox_data)

chicken_data = {
    "can_be_eaten": True,
    "eaten": False,
    "side": "left",
    "name": "chicken"
}
chicken = Item(**chicken_data)

feed_data = {
    "can_be_eaten": True,
    "eaten": False,
    "side": "left",
    "name": "feed"
}
feed = Item(**feed_data)

left_dock = Dock(side="left", items=[fox, chicken, feed])
right_dock = Dock(side="right", items=[])

def move():
    """
    Takes in a list of items.
    puts them on other side.
    """
    print left_dock.valid_state()
