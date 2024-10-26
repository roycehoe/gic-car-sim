from copy import deepcopy

from controller import apply_command_to_car, create_car, get_field
from models import AddCarOrRunSimulationSelection, Car, PostSimulationSelection
from view import (
    PROMPT_SET_NAME_OF_CAR_MESSAGE,
    PROMPT_SET_SIMULATION_DIMENSIONS_MESSAGE,
    get_prompt_car_commands,
    get_prompt_car_initial_position,
    get_prompt_post_simulation,
    get_prompt_pre_simulation,
)


def main():
    while True:
        cars: list[Car] = []
        post_simulation_cars: list[Car] = []
        field = None

        simulation_dimensions_input = input(PROMPT_SET_SIMULATION_DIMENSIONS_MESSAGE)
        field = get_field(simulation_dimensions_input)

        while True:
            add_car_or_run_simulation_input = input(
                get_prompt_pre_simulation(field, cars)
            )
            if (
                add_car_or_run_simulation_input
                != AddCarOrRunSimulationSelection.ADD_CAR_TO_FIELD
            ):
                break

            car_name_input = input(PROMPT_SET_NAME_OF_CAR_MESSAGE)
            car_initial_position_input = input(
                get_prompt_car_initial_position(car_name_input)
            )
            car_commands_input = input(get_prompt_car_commands(car_name_input))

            new_car = create_car(
                car_name_input, car_initial_position_input, car_commands_input
            )
            print(car_commands_input)
            cars.append(new_car)

        post_simulation_cars = [deepcopy(car) for car in cars]
        command_count = len(cars[0].commands)
        for post_simulation_car in post_simulation_cars:
            for command_index in range(command_count):
                apply_command_to_car(
                    post_simulation_car.commands[command_index], post_simulation_car
                )

        post_simulation_input = input(
            get_prompt_post_simulation(cars, post_simulation_cars)
        )
        if post_simulation_input == PostSimulationSelection.EXIT:
            exit()


main()
