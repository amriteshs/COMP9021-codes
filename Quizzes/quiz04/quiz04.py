# Randomly fills an array of size 10x10 with True and False, and outputs the number of blocks
# in the largest block construction, determined by rows of True's that can be stacked
# on top of each other.
#
# Written by Amritesh Singh and Eric Martin for COMP9021


from random import seed, randrange
import sys

dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end='')
        print(' '.join(f'{int(e)}' for e in grid[i]))
    print()


def size_of_largest_construction():
    maxblocks = 0

    for i in range(dim):
        j = 0
        j1 = -1

        while j < dim:
            if grid[i][j]:
                if j1 < 0:
                    j1 = j

                if j + 1 is dim or (j + 1 is not dim and not grid[i][j + 1]):
                    j2 = j
                    blocks_between_j1_j2 = construction_size(i, j1, j2)
                    j1 = -1
                    maxblocks = max(maxblocks, blocks_between_j1_j2)
            elif j1 < 0:
                j1 = -1

            j += 1

    return maxblocks


# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
def construction_size(i, j1, j2):
    block_ctr = 0

    for j in range(j1, j2 + 1):
        x = i

        while True:
            if grid[x][j]:
                block_ctr += 1

                if x > 0:
                    x -= 1
                else:
                    break
            else:
                break

    return block_ctr


try:
    for_seed, n = input('Enter two integers, the second one being strictly positive: ').split()
    for_seed = int(for_seed)
    n = int(n)
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[bool(randrange(n)) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_construction()
if not size:
    print(f'The largest block construction has no block.')
elif size == 1:
    print(f'The largest block construction has 1 block.')
else:
    print(f'The largest block construction has {size_of_largest_construction()} blocks.')