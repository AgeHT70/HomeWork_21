import pytest
from player import Player


class TestPlayer:

    def test_change_name(self):
        player = Player('Vova')
        player.change_name('Vasya')
        assert player.name == 'Vasya', 'Error in change_name'

    def test_add_points(self):
        player = Player('Vova')
        player.add_points(100)
        assert player.points == 100, 'Error in add_points'

    def test_get_points(self):
        player = Player('Vova')
        assert player.points == 0, 'Error in get_points'


