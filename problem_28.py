from array import array


class Spiral:
    def __init__(self, spiral_row_size: int) -> None:
        total_number = spiral_row_size ** 2
        self.spiral_numbers = array("I", [
            i for i in range(1, total_number + 1)
        ])

    def get_diagnoals(self) -> array:
        diagnals = array("I", [1])
        depth = 1
        
        # Dn = n * 2
        # next_index = index + Dn
        # start_index = 0

        index = 0
        n = 1
        try:
            while (True):
                for _ in range(4):
                    index += n * 2
                    diagnals.append(self.spiral_numbers[index])
                n += 1
        except:
            return diagnals

    def get_diagnoals_sum(self) -> int:
        return sum(self.get_diagnoals())


SPIRAL_SIZE = 1001

SPIRAL = Spiral(SPIRAL_SIZE)
print(SPIRAL.get_diagnoals_sum())
