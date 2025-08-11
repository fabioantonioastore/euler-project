from typing import NamedTuple


class Power(NamedTuple):
    line: int
    base: int
    exponent: int


FILE_NAME = "problem_99.txt"


def get_lines():
    count = 1
    with open(FILE_NAME, "r") as file:
        for line in file.readlines():
            line = line.split(",")
            yield Power(line=count, base=int(line[0]), exponent=int(line[1]))
            count += 1


max_power = Power(0, 0, 0)
max_value = 0
for power in get_lines():
    if power.base < max_power.base and power.exponent < max_power.exponent:
        continue
    power_value = pow(power.base, power.exponent)
    if power.base >= max_power.base and power.exponent >= max_power.exponent:
        max_power = power
        max_value = power_value
        continue
    if power_value >= max_value:
        max_power = power
        max_value = power_value

print(max_power.line)
