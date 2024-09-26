from inspect import isgenerator
from typing import Generator


def generate_cube_numbers(end: int) -> Generator[int, None, None]:
    i = 2
    while i**3 <= end:
        yield i**3
        i += 1


gen = generate_cube_numbers(1)
assert isgenerator(gen), 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'