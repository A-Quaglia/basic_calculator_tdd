from functools import reduce
from typing import List, Union

num_array = List[Union[float, int]]
ops_result = Union[float, int]


def apply_ops(func, *args: num_array) -> ops_result:
    return reduce(func, *args)


def add(*args: num_array) -> ops_result:
    return apply_ops(lambda a, b: a + b, *args)


def sub(*args: num_array) -> ops_result:
    return apply_ops(lambda a, b: a - b, *args)


def mul(*args: num_array) -> ops_result:
    return apply_ops(lambda a, b: a * b, *args)


def div(*args: num_array) -> ops_result:
    return apply_ops(lambda a, b: a / b, *args)


def read_commands_input(coomands_input: str) -> ops_result:
    operations = \
        {
            '+': add,
            '*': mul,
            '-': sub,
            '/': div,
        }

    result = 0
    new_digit = 0
    new_operation = ''

    for command in coomands_input.split():
        if command in operations:
            new_operation = command
        else:
            try:
                if str.isnumeric(command) and str.isdecimal(command):
                    new_digit = int(command)
                else:
                    new_digit = float(command)
            except ValueError as err:
                raise(f"{command} is not a viable input. \n\t err:{err}")

            if new_operation:
                result = operations[new_operation]([result, new_digit])
            else:
                result = new_digit

    return result