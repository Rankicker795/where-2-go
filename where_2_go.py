from itertools import chain
from random import randint

from restconfig import dinner, brunch, coffee


def _combine_lists(*args):
    return set(chain(*args))


def generate_rest_dict(choice: str) -> dict:
    restaurants = {
        "dinner": set(dinner),
        "brunch": set(brunch),
        "coffee": set(coffee),
        "all": _combine_lists(dinner, brunch),
    }
    return {index: value for index, value in enumerate(restaurants.get(
        choice))}


def make_random_choice(dict_) -> str:
    r_int = randint(0, len(dict_.keys()) - 1)
    return dict_.get(r_int)


if __name__ == "__main__":
    d = generate_rest_dict(input("Dinner, Brunch, or All? ").strip().lower())
    print(make_random_choice(d))
