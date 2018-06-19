from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    """
    Creates a grid that will hold all of the tiles
    for the boggle game
    """
    return {(row,col): choice(ascii_uppercase) 
        for row in range(height)
        for col in range(width)}
    
def neighbours_of_position(coords):
    """
    Get neighbours of given postion
    """
    row = coords[0]
    col = coords[1]
    
    #Assigne each of the neighbours
    #Top-left to top-right
    
    top_left = (row -1, col -1)
    top_centre = (row -1, col )
    top_right = (row -1, col +1)
    
    #Left to right
    
    left = (row, col -1)
    
    #The '(row, col') coordinates passed to this
    #Function are situated here 
    
    right = (row, col +1)
    
    #Bottom-left to bottom-right
    
    bottom_left = (row +1, col -1)
    bottom_centre = (row +1, col)
    bottom_right = (row +1, col +1)
    
    return [top_left, top_centre, top_right,
            left, right,
            bottom_left, bottom_centre, bottom_right]

def all_grid_neighbours(grid):
    """
    Get all of the possibile neighbours for each position in
    the grid
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    
    return neighbours
    
def path_to_word(grid, path):
    """
    Add all of the letters on the path to a string
    """
    return ''.join([grid[p] for p in path])
    
    
    