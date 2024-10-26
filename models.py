from dataclasses import dataclass
from enum import Enum, IntEnum, StrEnum, auto


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
