def make_grid(width, height):
    """
    Creates a grid that will hold all of the tiles
    for the boggle game
    """
    return {(row,col): ' ' for row in range(height)
        for col in range(width)}
    
    
    