from models import Car, Position

PROMPT_SET_SIMULATION_DIMENSIONS_MESSAGE = """Welcome to Auto Driving Car Simulation!

Please enter the width and height of the simulation field in x y format:"""

PROMPT_ADD_CAR_OR_RUN_SIMULATION_MESSAGE = """Please choose from the following options:
[1] Add a car to field
[2] Run simulation
"""

PROMPT_SET_NAME_OF_CAR_MESSAGE = """Please enter the name of the car:"""
PROMPT_START_OVER_OR_EXIT_MESSAGE = """Please choose from the following options:
[1] Start over
[2] Exit
"""


def _get_pre_simulation_car_view(car: Car) -> str:
    return f"- {car.name}, ({car.position.x}, {car.position.y}) {car.direction}, {''.join([command for command in car.commands])}"


def _get_post_simulation_car_view(car: Car) -> str:
    if car.collision_statistics:
        return f"- {car.name}, collides with {car.collision_statistics.other_car_name} at ({car.collision_statistics.position.x},{car.collision_statistics.position.x}) at step {car.collision_statistics.step}"
    return f"- {car.name}, ({car.position.x}, {car.position.y}) {car.direction}"


def _get_current_cars_view(cars: list[Car]) -> str:
    new_line = "\n"
    return f"""Your current list of cars are:
{new_line.join([_get_pre_simulation_car_view(car) for car in cars])}"""


def _get_post_simulation_cars_view(post_simulation_cars: list[Car]) -> str:
    new_line = "\n"
    return f"""After simulation, the result is:
{new_line.join([_get_post_simulation_car_view(post_simulation_car) for post_simulation_car in post_simulation_cars])}
    """


def _get_prompt_pre_simulation_header(field: Position, cars: list[Car]) -> str:
    if not cars:
        return f"You have created a field of {field.width} x {field.height}"
    return f"{_get_current_cars_view(cars)}"


def get_prompt_pre_simulation(field: Position, cars: list[Car]) -> str:
    return f"""{_get_prompt_pre_simulation_header(field, cars)}

{PROMPT_ADD_CAR_OR_RUN_SIMULATION_MESSAGE}"""


def get_prompt_car_initial_position(car_name: str) -> str:
    return (
        f"""Please enter initial position of car {car_name} in x y Direction format:"""
    )


def get_prompt_car_commands(car_name: str) -> str:
    return f"""Please enter the commands for car {car_name}:"""


def get_prompt_post_simulation(cars: list[Car], post_simulation_cars: list[Car]) -> str:
    return f"""{_get_current_cars_view(cars)}

{_get_post_simulation_cars_view(post_simulation_cars)}

{PROMPT_START_OVER_OR_EXIT_MESSAGE}"""
