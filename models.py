from dataclasses import dataclass
from enum import Enum, StrEnum, auto
from typing import Optional


class SimulationInterfaceState(Enum):
    SET_SIMULATION_DIMENSIONS = auto()
    SIMULATION_DIMENSIONS_DISPLAY_AND_ADD_CAR_OR_RUN_SIMULATION_MESSAGE = auto()
    SET_CAR_NAME = auto()
    SET_CAR_INITIAL_POSITION = auto()
    INPUT_CAR_COMMANDS = auto()
    SHOW_ALL_CAR_STATES_AND_ADD_CAR_OR_RUN_SIMULATION_MESSAGE = auto()


class AddCarOrRunSimulationSelection(StrEnum):
    ADD_CAR_TO_FIELD = "1"
    RUN_SIMULATION = "2"


class PostSimulationSelection(StrEnum):
    START_OVER = "1"
    EXIT = "2"


class Direction(StrEnum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


class Command(StrEnum):
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
    commands: list[Command]


@dataclass
class App:
    cars: list[Car]
    field: Optional[Field] = None

    def add_car(self, car: Car):
        self.cars.append(car)

    def set_field(self, field: Field):
        self.field = field
