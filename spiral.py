def prnt_mtx(matrix, width):
    height = len(matrix) // width
    for row in range(height):
        for col in range(width):
            print(f"\t{matrix[col + width*row]}", end = "")
        print()

def spiral(width, height):
    size = width * height
    tab = [None] * size

    is_horizontal = True
    drow, dcol = 1, 1
    row, col = 0, 0

    for i in range(size):
        tab[col + width*row] = i

        if is_horizontal:
            ncol = col + dcol
            if ncol < 0 or ncol >= width or tab[ncol + width*row] is not None:
                is_horizontal = False
                dcol *= -1
                row += drow
            else:
                col = ncol
        else:
            nrow = row + drow
            if nrow < 0 or nrow >= height or tab[col + width*nrow] is not None:
                is_horizontal = True
                drow *= -1
                col += dcol
            else:
                row = nrow

    return tab

w = 2
h = 2
prnt_mtx(spiral(w, h), w)