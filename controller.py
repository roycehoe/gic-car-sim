from models import Car, CollisionStatistics, Command, Direction, Position

COMMAND_TO_ORIENTATION_TO_NEXT_ORIENTATION_MAP: dict[
    Command, dict[Direction, Direction]
] = {
    Command.RIGHT: {
        Direction.NORTH: Direction.EAST,
        Direction.EAST: Direction.SOUTH,
        Direction.SOUTH: Direction.WEST,
        Direction.WEST: Direction.NORTH,
    },
    Command.LEFT: {
        Direction.NORTH: Direction.WEST,
        Direction.WEST: Direction.SOUTH,
        Direction.SOUTH: Direction.EAST,
        Direction.EAST: Direction.NORTH,
    },
}

USER_INPUT_TO_COMMAND_MAP: dict[str, Command] = {
    "F": Command.FORWARD,
    "R": Command.RIGHT,
    "L": Command.LEFT,
}


def get_field(simulation_dimensions_input: str) -> Position:
    parsed_user_input = simulation_dimensions_input.split(" ")
    return Position(x=int(parsed_user_input[0]), y=int(parsed_user_input[1]))


def create_car(
    car_name_input: str, car_initial_position_input: str, commands_input: str
) -> Car:
    commands = []

    x, y, direction = car_initial_position_input.split(" ")

    car_position = Position(x=int(x), y=int(y))
    car_direction = Direction(direction)
    for command_input in commands_input:
        if parsed_command := USER_INPUT_TO_COMMAND_MAP.get(command_input):
            commands.append(parsed_command)
            continue
        raise Exception

    return Car(
        name=car_name_input,
        position=car_position,
        direction=car_direction,
        commands=commands,
    )


def is_orientating_car(command: Command):
    return command == Command.RIGHT or command == Command.LEFT


def get_new_car_position(direction: Direction, position: Position):
    if direction == Direction.NORTH:
        return Position(position.x, position.y + 1)
    if direction == Direction.SOUTH:
        return Position(position.x, position.y - 1)
    if direction == Direction.EAST:
        return Position(position.x + 1, position.y)
    if direction == Direction.WEST:
        return Position(position.x - 1, position.y)


def _is_car_out_of_bounds(field: Position, car_position: Position):
    if car_position.x < 0:
        return True
    if car_position.y < 0:
        return True

    # For an [a] x [b] field, the maximum upper right coordinate is
    # [a-1] x [b-1] due to boundary inclusion in a zero based system
    if car_position.x >= field.x - 1:
        return True
    if car_position.y >= field.y - 1:
        return True

    return False


def apply_command_to_car(command: Command, car: Car, field: Position):
    if is_orientating_car(command):
        next_orientation_map = COMMAND_TO_ORIENTATION_TO_NEXT_ORIENTATION_MAP.get(
            command
        )
        if next_orientation_map is None:
            raise Exception
        next_direction = next_orientation_map.get(car.direction)
        if next_direction is None:
            raise Exception
        car.direction = next_direction
    else:
        new_car_position = get_new_car_position(car.direction, car.position)
        if not _is_car_out_of_bounds(field, new_car_position):
            car.position = new_car_position

    car.commands.append(command)


def set_collided_cars(cars: list[Car], step: int) -> None:
    index: dict[Position, list[Car]] = {}
    non_collided_cars = [
        non_collided_car
        for non_collided_car in cars
        if non_collided_car.collision_statistics is None
    ]
    for car in non_collided_cars:
        if car.position not in index:
            index[car.position] = []
        index[car.position].append(car)

    for position, cars_at_position in index.items():
        if len(cars_at_position) == 1:
            continue
        first_car, second_car = cars_at_position
        first_car.collision_statistics = CollisionStatistics(
            other_car_name=second_car.name, position=position, step=step
        )
        second_car.collision_statistics = CollisionStatistics(
            other_car_name=first_car.name, position=position, step=step
        )
