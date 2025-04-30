import re
from typing import List, Tuple


def problem_1(input: List[int]) -> List[int]:
    if all([type(i) == int for i in input]):
        n = int("".join([str(i) for i in input]))
        n = n + 1

        return [int(i) for i in list(str(n))]
    else:
        raise ValueError('All values of "input" argument needs to be of type: int')


def problem_2(input: str) -> bool:
    if re.search(r"[\(\)\{\}\[\]]+", input):
        openers: Tuple[str] = ("(", "{", "[")
        closers: Tuple[str] = (")", "}", "]")

        last_char: str
        for n, c in enumerate(input):
            if n == 0:
                last_char = c
            else:
                if c in openers:
                    if last_char not in closers:
                        return False
                    else:
                        last_char = c
                else:
                    current_closer_index: int = closers.index(c)
                    last_opener_index: int = openers.index(last_char)

                    if current_closer_index != last_opener_index:
                        return False

                    last_char = c

        return True
    else:
        raise ValueError('The "input" argument valid characters are: ()[]{}')
