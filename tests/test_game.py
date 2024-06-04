from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            new_game = Game()
            # exercise
            grid = new_game.grid
            # verify
            assert type(grid) == list
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase
            # teardown
    def test_empty_word_is_invalid(self):
        # setup
        new_game = Game()
        assert new_game.is_valid('') == False

    def positive_grid_test(self):
        new_game = Game()
        grid = "WEIJWHCDX"
        word = "CHEW"
        new_game.grid = list(grid)
        assert new_game.is_valid(word) is True

    def negative_grid_test(self):
        new_game = Game()
        grid = "WEIJWHCDX"
        word = "GOLEM"
        new_game.grid = list(grid)
        assert new_game.is_valid(word) is False
