class Figure:
    _name: str
    coordinates: tuple[int, int]

    def __init__(self, x: int, y: int):
        self.coordinates = x, y

    @property
    def x(self) -> int:
        return self.coordinates[0]

    @property
    def y(self) -> int:
        return self.coordinates[1]

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def short_name(self) -> str:
        return self._name[0]

    def __repr__(self):
        return self.short_name


class Queen(Figure):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self._name = "Queen"


class Board:
    figures: list[Figure]
    board = list[list[Figure | None]]

    def __init__(self):
        self.figures = []
        self.board = [[None for _ in range(8)] for _ in range(8)]
        # print(self.board)

    def __len__(self):
        return len(self.figures)

    def add_figure(self, figure: Figure):
        self.figures.append(figure)
        self.board[figure.x][figure.y] = figure

    def pop_figure(self) -> Figure:
        f = self.figures.pop()
        self.board[f.x][f.y] = None
        return f

    def check_cell(self, x: int, y: int) -> bool:
        for _x in range(8):
            if _x == x:
                continue
            if self.board[_x][y] is not None:
                return False
        for _y in range(8):
            if _y == y:
                continue
            if self.board[x][_y] is not None:
                return False
        lux, luy = (x - y, 0) if x > y else (0, y - x)
        rux, ruy = (x + y, 0) if x + y <= 7 else (7, y - (7 - x))
        while lux <= 7 and luy <= 7:
            if lux == x and luy == y:
                lux += 1
                luy += 1
                continue
            if self.board[lux][luy] is not None:
                return False
            lux += 1
            luy += 1
        while rux >= 0 and ruy <= 7:
            if rux == x and ruy == y:
                rux -= 1
                ruy += 1
                continue
            if self.board[rux][ruy] is not None:
                return False
            rux -= 1
            ruy += 1
        return True

    def check_board(self):
        return all([self.check_cell(f.x, f.y) for f in self.figures])

    def __repr__(self):
        result = []  # ["___" for _ in range(8)]

        for line in self.board:
            result.append("\n|")
            for cell in line:
                result.append(f'{" " if cell is None else cell.short_name}|')

        result.append("\n")
        # result.extend(["___" for _ in range(8)])
        return ''.join(result)


if __name__ == "__main__":
    b = Board()
    x, y = 0, 0
    while len(b) < 8:
        if b.check_cell(x, y):
            b.add_figure(Queen(x, y))
            y += 1
            x = 0
            continue
        x += 1
        if x > 7:
            f = b.pop_figure()
            while f.x == 7:
                f = b.pop_figure()
            x, y = f.x + 1, f.y
    print(b.check_board())
    print(b)
