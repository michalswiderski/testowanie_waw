from klasy import Car


def test_Car_init():
    car = Car("BMW", "black")
    assert car.name == "BMW"


def test_Car_change_color():
    car = Car("BMW", "black")
    car.change_color("red")
    assert car.color == "red"

