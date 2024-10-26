from models import Car, Command, Direction, Field, Position
from view import (
    PROMPT_SET_NAME_OF_CAR_MESSAGE,
    PROMPT_SET_SIMULATION_DIMENSIONS_MESSAGE,
    get_prompt_car_commands,
    get_prompt_car_initial_position,
    get_prompt_post_simulation_selection,
)

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


def get_field(simulation_dimensions_input: str) -> Field:
    parsed_user_input = simulation_dimensions_input.split("")
    return Field(width=int(parsed_user_input[0]), height=int(parsed_user_input[1]))


def create_car(car_name_input: str, car_initial_position_input: str) -> Car:
    x, y, direction = car_initial_position_input.split(" ")

    car_position = Position(x=int(x), y=int(y))
    car_direction = Direction(direction)
    return Car(
        name=car_name_input, position=car_position, direction=car_direction, commands=[]
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


def apply_command_to_car(direction: Direction, command: Command, car: Car):
    if is_orientating_car(command):
        next_orientation_map = COMMAND_TO_ORIENTATION_TO_NEXT_ORIENTATION_MAP.get(
            command
        )
        if next_orientation_map is None:
            raise Exception
        next_direction = next_orientation_map.get(direction)
        if next_direction is None:
            raise Exception
        car.direction = next_direction

    car.position = get_new_car_position(direction, car.position)
