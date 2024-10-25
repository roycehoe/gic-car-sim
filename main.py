from dataclasses import dataclass
from enum import Enum, IntEnum, auto

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


class Simulation: ...


class Direction(Enum):


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
    name: str # Note: Name must be unique
    stating_position: Position
    direction: Direction



class AddCarOrRunSimulationSelection(IntEnum):
    ADD_CAR_TO_FIELD = 1
    RUN_SIMULATION = 2


def get_field(simulation_dimensions_input: str):
    parsed_user_input = simulation_dimensions_input.split("")
    return Field(width=int(parsed_user_input[0]), height=int(parsed_user_input[1]))


def get_field_message(field: Field):
    return f"You have created a field of {field.width} x {field.height}"


def get_post_init_field_message(field: Field):
    return f"""{get_field_message(field)}

     {PROMPT_ADD_CAR_OR_RUN_SIMULATION_MESSAGE}"""


def get_car_initial_position(car_name: str):
    return (
        f"""Please enter initial position of car {car_name} in x y Direction format:"""
    )


def main():
    simulation_dimensions_input = input(PROMPT_SET_SIMULATION_DIMENSIONS_MESSAGE)
    field = get_field(simulation_dimensions_input)
    add_car_or_run_simulation_input = input(get_post_init_field_message(field))
    if (
        add_car_or_run_simulation_input
        == AddCarOrRunSimulationSelection.ADD_CAR_TO_FIELD
    ):
        car_name_input = input(PROMPT_SET_NAME_OF_CAR_MESSAGE)
        car_initial_position_input = input(get_car_initial_position(car_name_input))
    elif (
        add_car_or_run_simulation_input == AddCarOrRunSimulationSelection.RUN_SIMULATION
    ):
        ...
    else:
        raise Exception
