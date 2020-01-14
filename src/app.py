import os
import importlib
import click

GROUP = 5
STEPS = 1
WIDTH, HEIGHT = click.get_terminal_size()
PATH = os.path.abspath(os.path.dirname(__file__)) + "/solutions"


def list_ranges(files):
    global STEPS
    for group in range(0, len(files), GROUP):
        click.echo(f"{STEPS}. Problem {group + 1} to {group + GROUP}")
        STEPS += 1
    
    click.echo(f"{STEPS}. Exit")
    divisor()

    return STEPS


def list_solutions(solutions):
    global STEPS
    STEPS = 1

    for solution in solutions:
        solution = solution.replace('_', ' ').strip()
        click.echo(f"{STEPS}. {solution}")
        STEPS += 1

    click.echo(f"{STEPS}. Exit")
    divisor()

    return STEPS


def divisor():
    click.echo("*" * WIDTH)


def print_title():
    click.clear()
    click.echo(click.style("PROJECT EULER".center(WIDTH), bold=True))
    divisor()


def ranges(files):
    print_title()
    steps = list_ranges(files)
    return select_options(steps)


def solutions(files, range_selected):
    print_title()

    list_to = range_selected * GROUP
    problems = files[list_to - GROUP:list_to]
    steps = list_solutions(problems)
    return select_options(steps), problems


def select_options(steps):
    selected = None
    while not selected:
        try:
            selected = click.prompt(
                "Please select a valid option to display",
                value_proc=option_validator
            )
        except:
            pass
    
    return selected


def option_validator(value):
    try:
        value = int(value)
        if value <= STEPS:
            return value
    except:
        pass

    return False


def execute_problem(filename):
    print_title()

    problem = importlib.import_module("solutions." + filename.replace(".py", ""))
    click.echo(problem.__doc__)

    divisor()
    click.echo()
    
    problem.main()


if __name__ == "__main__":
    files = os.listdir(PATH)
    list_files = [f.replace(".py", "") for f in files if f.endswith(".py")]
    list_files.sort()
    
    selected = ranges(list_files)
    if selected == STEPS: exit()
        
    selected, problems = solutions(list_files, selected)
    if selected == STEPS: exit()

    selected_problem = problems[selected - 1]
    execute_problem(selected_problem)
    divisor()
