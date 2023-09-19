from itertools import permutations
from menace import Board
from latex import preamb, postamb

positions = [[Board()], [], [], []]

for o1, x1 in permutations(range(9), 2):
    board = Board()
    board[o1] = 1
    board[x1] = 2
    if board.is_max() and not board.in_set(positions[1]):
        positions[1].append(board)

for o1, x1, o2, x2 in permutations(range(9), 4):
    board = Board()
    board[o1] = 1
    board[x1] = 2
    board[o2] = 1
    board[x2] = 2
    if board.is_max() and not board.in_set(positions[2]):
        positions[2].append(board)

for o1, x1, o2, x2, o3, x3 in permutations(range(9), 6):
    board = Board()
    board[o1] = 1
    board[x1] = 2
    board[o2] = 1
    board[x2] = 2
    board[o3] = 1
    board[x3] = 2
    if board.has_winner():
        continue
    if board.is_max() and not board.in_set(positions[3]):
        positions[3].append(board)


assert len(positions[0]) == 1
assert len(positions[1]) == 12
assert sum([len(p) for p in positions]) == 304

for i, boards in enumerate(positions):
    latex = preamb
    for j, board in enumerate(boards):
        # HACK FIX: hard-code the numbers to avoid rewriting the scritps
        if i == 0:
            iter_num = j + 1
        elif i == 1:
            iter_num = 1 + (j + 1)
        elif i == 2:
            iter_num = 13 + (j + 1)
        elif i == 3:
            iter_num = 121 + (j + 1)
        else:
            raise ValueError("The number of possible sets is between 0, 1, 2, and 3")

        latex += board.as_latex(iter_num=None)
        latex += "\n"
        if (j + 1) % 5 == 0:
            latex += "\n\\noindent"
    latex += postamb
    print(latex)
    with open(f"output/boxes{i}.tex", "w") as f:
        f.write(latex)

    # NOTE: we don't use the code from below as pdflatex initialization wasn't working
    # hence we convert tex files to pdf ourselves
    # assert os.system(
    #     f"pdflatex -output-directory output output/boxes{i}.tex") == 0
