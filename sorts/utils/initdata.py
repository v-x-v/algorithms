#! /usr/bin/env python
import random


def generate(num: int):
    """ Generate random integer list

    Args:
        num (int): size of list

    Returns:
        Array: random integer list(size: num)
    """
    return [random.randint(0, num*100) for i in range(0, num)]


if __name__ == '__main__':
    generate(1)
