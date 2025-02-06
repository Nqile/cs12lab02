from typing import Iterable


class GameModel:
    def __init__(self, grid: Iterable[Iterable[int | None]]):
        self.grid:list[list[int | None]] = list([list(e) for e in grid])
        if len(self.grid) == 0:
            raise ValueError("Grid should not be empty")
        rows = len(self.grid) 
        columns = len(list(self.grid[0]))
        if len(self.grid) != len(self.grid[0]):
            raise ValueError(f"Rows ({rows}) and columns ({columns}) should be of equal size")
        if len(self.grid) < 2 or len(self.grid[0]) < 2:
            raise ValueError(f"Rows ({rows}) and columns ({columns}) size should be more than or equal to 2")
        at_least_one: bool = False
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if type(self.grid[i][j]) == int:
                    at_least_one = True
                    break
        if not at_least_one:
            raise ValueError("There should be at least one int in the initial grid")

    def order(self, dir: str):
        rows = len(self.grid) 
        columns = len(list(self.grid[0]))
        def charge(grid_: list[list[int | None]]):
            rest: bool = False
            if dir in "N":
                for i in range (rows-1):
                    for j in range (columns):
                        if grid_[i][j] == None:
                            grid_[i][j] = grid_[i+1][j]
                            grid_[i+1][j] = None
                        elif grid_[i+1][j] != grid_[i][j]:
                            pass
                        elif grid_[i+1][j] == grid_[i][j] and not rest:
                            grid_[i+1][j] = duel(grid_[i+1][j], grid_[i][j])
                            grid_[i][j] = None
                        elif rest:
                            rest = False
                        else:
                            pass
            if dir in "E":
                for i in range (rows):
                    for j in range (columns-1):
                        if grid_[i][j] == None:
                            grid_[i][j] = grid_[i][j+1]
                            grid_[i][j+1] = None
                        elif grid_[i][j+1] != grid_[i][j]:
                            pass
                        elif grid_[i][j+1] == grid_[i][j] and not rest:
                            grid_[i][j+1] = duel(grid_[i][j+1], grid_[i][j])
                            grid_[i][j] = None
                        elif rest:
                            rest = False
                        else:
                            pass
            if dir in "S":
                for i in range (rows-1, -1, -1):
                    for j in range (columns):
                        if grid_[i][j] == None:
                            grid_[i][j] = grid_[i-1][j]
                            grid_[i-1][j] = None
                        elif grid_[i-1][j] != grid_[i][j]:
                            pass
                        elif grid_[i-1][j] == grid_[i][j] and not rest:
                            grid_[i-1][j] = duel(grid_[i-1][j], grid_[i][j])
                            grid_[i][j] = None
                        elif rest:
                            rest = False
                        else:
                            pass
            if dir in "W":
                for i in range (rows):
                    for j in range (columns-1, -1, -1):
                        if grid_[i][j] == None:
                            grid_[i][j] = grid_[i][j-1]
                            grid_[i][j-1] = None
                        elif grid_[i][j-1] != grid_[i][j]:
                            pass
                        elif grid_[i][j-1] == grid_[i][j] and not rest:
                            grid_[i][j-1] = duel(grid_[i][j-1], grid_[i][j])
                            grid_[i][j] = None
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
            
            for i in range (len(grid_)-1, -1, -1):
                for j in range (len(grid_[0])-1, -1, -1):
                    if grid_[i][j] == None:
                        grid_[i][j] = 1
                        return grid_
                        
                    
            return grid_
        
        charge(self.grid)
        print(self.grid)
        
    def get_content(self, row: int, col: int) -> int | None:
    
        return self.grid[row][col]
    
    def game_over_check(self) -> bool:
        
        dirs: list[str] = ["N", "E", "S", "W"]
        grid_ = self

        for dir in dirs:
            grid_.order(dir)
        
        if grid_.grid == self.grid:
            return True

        return False
    
    def get_resulting_strongest(self) -> int | None:
        if not self.game_over_check():
            return None
        else:
            temp_: list[int] = []
            for row in self.grid:
                for e in row:
                    if type(e) == int:
                        temp_.append(e)
            
            return max(temp_)
            
        
