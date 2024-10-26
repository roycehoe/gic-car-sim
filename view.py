from dataclasses import dataclass
from enum import Enum, IntEnum, StrEnum, auto

PROMPT_SET_SIMULATION_DIMENSIONS_MESSAGE = """Welcome to Auto Driving Car Simulation!

Please enter the width and height of the simulation field in x y format:"""

PROMPT_ADD_CAR_OR_RUN_SIMULATION_MESSAGE = """Please choose from the following options:
[1] Add a car to field
[2] Run simulation"""

PROMPT_SET_NAME_OF_CAR_MESSAGE = """Please enter the name of the car:"""
PROMPT_SET_INITIAL_POSITION_OF_CAR_MESSAGE = (
    """Please enter initial position of car A in x y Direction format:"""
)


class SimulationInterfaceState(Enum):
    SET_SIMULATION_DIMENSIONS = auto()
    SIMULATION_DIMENSIONS_DISPLAY_AND_ADD_CAR_OR_RUN_SIMULATION_MESSAGE = auto()
    SET_CAR_NAME = auto()
    SET_CAR_INITIAL_POSITION = auto()
    INPUT_CAR_COMMANDS = auto()
    SHOW_ALL_CAR_STATES_AND_ADD_CAR_OR_RUN_SIMULATION_MESSAGE = auto()


class AddCarOrRunSimulationSelection(IntEnum):
    ADD_CAR_TO_FIELD = 1
    RUN_SIMULATION = 2


class Direction(StrEnum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


class Commands(StrEnum):
    FORWARD = "F"
    RIGHT = "R"
    LEFT = "L"


@dataclass
class Field:
    width: int
    height: int


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Car:
    name: str  # Note: Name must be unique
    position: Position
    direction: Direction
    commands: list[Commands]


def get_pre_simulation_car_view(car: Car) -> str:
    return f"- {car.name}, ({car.position.x}, {car.position.y}) {car.direction}, {[command for command in car.commands]}"


def get_post_simulation_car_view(car: Car) -> str:
    return f"- {car.name}, ({car.position.x}, {car.position.y}) {car.direction}"


def get_prompt_post_init_field_selection(field: Field) -> str:
    return f"""You have created a field of {field.width} x {field.height}

     {PROMPT_ADD_CAR_OR_RUN_SIMULATION_MESSAGE}"""


def get_prompt_car_initial_position(car_name: str) -> str:
    return (
        f"""Please enter initial position of car {car_name} in x y Direction format:"""
    )


def get_prompt_car_commands(car_name: str) -> str:
    return f"""Please enter the commands for car {car_name}"""


def get_prompt_post_simulation_selection(
    cars: list[Car], post_simulation_cars: list[Car]
) -> str:
    return f"""Your current list of cars are:
{[car for car in cars]}

After simulation, the result is:
{[post_simulation_car for post_simulation_car in post_simulation_cars]}

Please choose from the following options:
[1] Start over
[2] Exit
"""
