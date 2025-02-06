import pytest

from model import GameModel

def test_errors():
    model_empty = GameModel([])
    model_inequal = GameModel([[1, 2, 3], [1, 2]])
    model_toosmall = GameModel([[1], [1]])
    model_noints = GameModel([[None, None], [None, None]])

    assert model_empty == ValueError
    assert model_inequal == ValueError
    assert model_toosmall == ValueError
    assert model_noints == ValueError
    
def test_other_east():
    model_no_move = GameModel([[None, None],[1, 2]])
    model_no_move_1 = GameModel([[None, 1],[1, 2]])
    model_no_move.order("E")

    assert model_no_move == model_no_move_1

def test_other_south():
    model_no_move = GameModel([[None, 1],[None, 2]])
    model_no_move_1 = GameModel([[None, 1],[1, 2]])
    model_no_move.order("S")

    assert model_no_move == model_no_move_1

def test_other_west():
    model_no_move = GameModel([[None, None],[1, 2]])
    model_no_move_1 = GameModel([[None, 1],[1, 2]])
    model_no_move.order("W")

    assert model_no_move == model_no_move_1

def test_other_north():
    model_no_move = GameModel([[None, 1],[None, 2]])
    model_no_move_1 = GameModel([[None, 1],[1, 2]])
    model_no_move.order("N")

    assert model_no_move == model_no_move_1
