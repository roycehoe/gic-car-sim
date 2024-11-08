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


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass
class CollisionStatistics:
    other_car_name: str
    position: Position
    step: int


@dataclass
class Car:
    name: str  # Note: Name must be unique
    position: Position
    direction: Direction
    commands: list[Command]
    collision_statistics: Optional[CollisionStatistics] = None
