import pytest

from controller import get_field, get_post_simulation_cars
from models import Car, CollisionStatistics, Command, Direction, Position


def test_get_field_input_two_numbers_space_separated():
    position = get_field("1 1")
    assert position == Position(x=1, y=1)


def test_get_field_input_one_number():
    with pytest.raises(IndexError):
        get_field("1")


def test_get_field_input_non_numbers():
    with pytest.raises(ValueError):
        get_field("foo bar")


def test_get_field_input_no_input():
    with pytest.raises(ValueError):
        get_field("")


def test_get_field_input_more_than_two_numbers():
    position = get_field("1 2 3 4 5")
    assert position == Position(x=1, y=2)


@pytest.fixture
def field():
    return Position(10, 10)


def test_get_post_simulation_three_cars_no_crash(field):
    car_1 = Car(
        name="Car1",
        position=Position(0, 0),
        direction=Direction.NORTH,
        commands=[Command.FORWARD, Command.RIGHT, Command.FORWARD],
    )
    car_2 = Car(
        name="Car2",
        position=Position(7, 7),
        direction=Direction.SOUTH,
        commands=[Command.FORWARD, Command.LEFT, Command.FORWARD],
    )
    car_3 = Car(
        name="Car3",
        position=Position(5, 5),
        direction=Direction.NORTH,
        commands=[Command.FORWARD, Command.RIGHT, Command.FORWARD],
    )

    cars = [car_1, car_2, car_3]
    post_simulation_cars = get_post_simulation_cars(cars, field)

    assert post_simulation_cars[0] == Car(
        name="Car1",
        position=Position(1, 1),
        direction=Direction.EAST,
        commands=[Command.FORWARD, Command.RIGHT, Command.FORWARD],
    )
    assert post_simulation_cars[1] == Car(
        name="Car2",
        position=Position(8, 6),
        direction=Direction.EAST,
        commands=[Command.FORWARD, Command.LEFT, Command.FORWARD],
    )
    assert post_simulation_cars[2] == Car(
        name="Car3",
        position=Position(6, 6),
        direction=Direction.EAST,
        commands=[Command.FORWARD, Command.RIGHT, Command.FORWARD],
    )


def test_get_post_simulation_three_cars_two_crash_one_ok(field):
    car_1 = Car(
        name="Car1",
        position=Position(0, 0),
        direction=Direction.NORTH,
        commands=[
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
        ],
    )
    car_2 = Car(
        name="Car2",
        position=Position(7, 7),
        direction=Direction.SOUTH,
        commands=[Command.FORWARD, Command.LEFT, Command.FORWARD],
    )
    car_3 = Car(
        name="Car3",
        position=Position(0, 2),
        direction=Direction.SOUTH,
        commands=[
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
        ],
    )

    cars = [car_1, car_2, car_3]
    post_simulation_cars = get_post_simulation_cars(cars, field)

    assert post_simulation_cars[0] == Car(
        name="Car1",
        position=Position(0, 1),
        direction=Direction.NORTH,
        commands=[
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
        ],
        collision_statistics=CollisionStatistics(
            other_car_name="Car3", position=Position(x=0, y=1), step=1
        ),
    )
    assert post_simulation_cars[1] == Car(
        name="Car2",
        position=Position(8, 6),
        direction=Direction.EAST,
        commands=[Command.FORWARD, Command.LEFT, Command.FORWARD],
    )
    assert post_simulation_cars[2] == Car(
        name="Car3",
        position=Position(0, 1),
        direction=Direction.SOUTH,
        commands=[
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
        ],
        collision_statistics=CollisionStatistics(
            other_car_name="Car1", position=Position(x=0, y=1), step=1
        ),
    )


def test_get_post_simulation_three_cars_no_commands(field):
    car_1 = Car(
        name="Car1",
        position=Position(0, 0),
        direction=Direction.NORTH,
        commands=[],
    )
    car_2 = Car(
        name="Car2",
        position=Position(7, 7),
        direction=Direction.SOUTH,
        commands=[],
    )
    car_3 = Car(
        name="Car3",
        position=Position(0, 2),
        direction=Direction.SOUTH,
        commands=[],
    )

    cars = [car_1, car_2, car_3]
    post_simulation_cars = get_post_simulation_cars(cars, field)

    assert post_simulation_cars[0] == Car(
        name="Car1",
        position=Position(0, 0),
        direction=Direction.NORTH,
        commands=[],
    )
    assert post_simulation_cars[1] == Car(
        name="Car2",
        position=Position(7, 7),
        direction=Direction.SOUTH,
        commands=[],
    )
    assert post_simulation_cars[2] == Car(
        name="Car3",
        position=Position(0, 2),
        direction=Direction.SOUTH,
        commands=[],
    )


def test_get_post_simulation_three_cars_two_crash_one_ok_different_lengths(field):
    car_1 = Car(
        name="Car1",
        position=Position(0, 0),
        direction=Direction.NORTH,
        commands=[
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
        ],
    )
    car_2 = Car(
        name="Car2",
        position=Position(7, 7),
        direction=Direction.SOUTH,
        commands=[Command.FORWARD, Command.LEFT, Command.FORWARD],
    )
    car_3 = Car(
        name="Car3",
        position=Position(0, 2),
        direction=Direction.SOUTH,
        commands=[
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
        ],
    )

    cars = [car_1, car_2, car_3]
    post_simulation_cars = get_post_simulation_cars(cars, field)

    assert post_simulation_cars[0] == Car(
        name="Car1",
        position=Position(0, 1),
        direction=Direction.NORTH,
        commands=[
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
        ],
        collision_statistics=CollisionStatistics(
            other_car_name="Car3", position=Position(x=0, y=1), step=1
        ),
    )
    assert post_simulation_cars[1] == Car(
        name="Car2",
        position=Position(8, 6),
        direction=Direction.EAST,
        commands=[Command.FORWARD, Command.LEFT, Command.FORWARD],
    )
    assert post_simulation_cars[2] == Car(
        name="Car3",
        position=Position(0, 1),
        direction=Direction.SOUTH,
        commands=[
            Command.FORWARD,
            Command.FORWARD,
            Command.FORWARD,
        ],
        collision_statistics=CollisionStatistics(
            other_car_name="Car1", position=Position(x=0, y=1), step=1
        ),
    )
