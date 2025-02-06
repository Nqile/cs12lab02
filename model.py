from typing import Iterable


class GameModel:
    def __init__(self, grid: Iterable[Iterable[int | None]]):
        self.grid:list[list[int | None]] = list([list(e) for e in grid])
        
    def order(self, dir: str):

        rows = len(self.grid) 
        columns = len(list(self.grid[0]))
             
        def charge(grid_: list[list[int | None]]):
            rest: bool = False
            if dir in "N":
                for i in range (rows):
                    for j in range (columns):
                        if grid_[i][j] == None:
                            grid_[i][j] = grid_[i+1][j]
                            grid_[i+1][j] = None
                        elif grid_[i+1][j] != grid_[i][j]:
                            pass
                        elif grid_[i+1][j] == grid_[i][j] and not rest:
                            grid_[i][j] = duel(grid_[i+1][j], grid_[i][j])
                        elif rest:
                            rest = False
                        else:
                            pass
            if dir in "E":
                for i in range (rows):
                    for j in range (columns):
                        if grid_[i][j] == None:
                            grid_[i][j] = grid_[i][j+1]
                            grid_[i][j+1] = None
                        elif grid_[i][j+1] != grid_[i][j]:
                            pass
                        elif grid_[i][j+1] == grid_[i][j] and not rest:
                            grid_[i][j] = duel(grid_[i][j+1], grid_[i][j])
                        elif rest:
                            rest = False
                        else:
                            pass
            if dir in "S":
                for i in range (rows-1, 0, -1):
                    for j in range (columns):
                        if grid_[i][j] == None:
                            grid_[i][j] = grid_[i-1][j]
                            grid_[i-1][j] = None
                        elif grid_[i-1][j] != grid_[i][j]:
                            pass
                        elif grid_[i-1][j] == grid_[i][j] and not rest:
                            grid_[i][j] = duel(grid_[i-1][j], grid_[i][j])
                        elif rest:
                            rest = False
                        else:
                            pass
            if dir in "W":
                for i in range (rows):
                    for j in range (columns-1, 0, -1):
                        if grid_[i][j] == None:
                            grid_[i][j] = grid_[i][j-1]
                            grid_[i][j-1] = None
                        elif grid_[i][j-1] != grid_[i][j]:
                            pass
                        elif grid_[i][j-1] == grid_[i][j] and not rest:
                            grid_[i][j] = duel(grid_[i][j-1], grid_[i][j])
                        elif rest:
                            rest = False
                        else:
                            pass

            grid_ = new_samurai(grid_)
            return grid_
        
        def duel(samurai1: int | None, samurai2: int | None) -> int | None:
            if samurai1 and samurai2:
                return samurai1+1
            else:
                return None
        
        def new_samurai(grid_: list[list[int | None]]) -> list[list[int | None]]:
            
            for i in range (len(grid_)):
                for j in range (len(grid_[0])):
                    if grid_[i][j] == None:
                        grid_[i][j] = 1
                        return grid_
            return grid_
        
        charge(self.grid)
        
    def get_content(self, row: int, col: int) -> int | None:
    
        return 
    