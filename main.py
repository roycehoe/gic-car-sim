from models import AddCarOrRunSimulationSelection, Car, Direction, Field, Position
from view import (
    PROMPT_SET_NAME_OF_CAR_MESSAGE,
    PROMPT_SET_SIMULATION_DIMENSIONS_MESSAGE,
    get_prompt_car_commands,
    get_prompt_car_initial_position,
    get_prompt_post_simulation_selection,
)


def get_field(simulation_dimensions_input: str):
    parsed_user_input = simulation_dimensions_input.split("")
    return Field(width=int(parsed_user_input[0]), height=int(parsed_user_input[1]))


def main():
    mock_car = Car(
        name="placeholder_name",
        position=Position(x=0, y=0),
        direction=Direction.NORTH,
        commands=["L", "L", "R"],
    )
    mock_post_simulation_car = Car(
        name="placeholder_name",
        position=Position(x=0, y=0),
        direction=Direction.NORTH,
        commands=["L", "L", "R"],
    )

    simulation_dimensions_input = input(PROMPT_SET_SIMULATION_DIMENSIONS_MESSAGE)
    field = get_field(simulation_dimensions_input)

    add_car_or_run_simulation_input = input(get_prompt_post_init_field_selection(field))
    if (
        add_car_or_run_simulation_input
        == AddCarOrRunSimulationSelection.ADD_CAR_TO_FIELD
    ):
        car_name_input = input(PROMPT_SET_NAME_OF_CAR_MESSAGE)
        car_initial_position_input = input(
            get_prompt_car_initial_position(car_name_input)
        )
    elif (
        add_car_or_run_simulation_input == AddCarOrRunSimulationSelection.RUN_SIMULATION
    ):
        ...
    else:
        raise Exception

    car_commands = get_prompt_car_commands(mock_car.name)
    get_prompt_post_simulation_selection([mock_car], [mock_post_simulation_car])
