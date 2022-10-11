import unittest

import numpy as np

from tableturf.model import Card, Grid


class TestCard(unittest.TestCase):
    def setUp(self) -> None:
        self.card = Card(
            -1,
            np.array([
                [Grid.MyInk.value, Grid.MyInk.value, Grid.MyInk.value],
                [Grid.Empty.value, Grid.Empty.value, Grid.MySpecial.value],
            ]),
            5
        )

    def test_card_grid(self):
        self.assertListEqual(self.card.get_grid(rotate=0).tolist(), [
            [Grid.MyInk.value, Grid.MyInk.value, Grid.MyInk.value],
            [Grid.Empty.value, Grid.Empty.value, Grid.MySpecial.value],
        ])
        self.assertListEqual(self.card.get_grid(rotate=1).tolist(), [
            [Grid.MyInk.value, Grid.MySpecial.value],
            [Grid.MyInk.value, Grid.Empty.value],
            [Grid.MyInk.value, Grid.Empty.value],
        ])
        self.assertListEqual(self.card.get_grid(rotate=2).tolist(), [
            [Grid.MySpecial.value, Grid.Empty.value, Grid.Empty.value],
            [Grid.MyInk.value, Grid.MyInk.value, Grid.MyInk.value],
        ])
        self.assertListEqual(self.card.get_grid(rotate=3).tolist(), [
            [Grid.Empty.value, Grid.MyInk.value],
            [Grid.Empty.value, Grid.MyInk.value],
            [Grid.MySpecial.value, Grid.MyInk.value],
        ])

    def test_card_offset(self):
        self.assertListEqual(self.card.get_offsets(0, rotate=0).tolist(), [
            [0, 0],
            [0, 1],
            [0, 2],
            [1, 2],
        ])
        self.assertListEqual(self.card.get_offsets(0, rotate=1).tolist(), [
            [0, 0],
            [-1, 0],
            [-2, 0],
            [-2, 1],
        ])
        self.assertListEqual(self.card.get_offsets(0, rotate=2).tolist(), [
            [0, 0],
            [0, -1],
            [0, -2],
            [-1, -2],
        ])
        self.assertListEqual(self.card.get_offsets(0, rotate=3).tolist(), [
            [0, 0],
            [1, 0],
            [2, 0],
            [2, -1],
        ])
        self.assertListEqual(self.card.get_offsets(1, rotate=0).tolist(), [
            [0, -1],
            [0, 0],
            [0, 1],
            [1, 1],
        ])
        self.assertListEqual(self.card.get_offsets(2, rotate=0).tolist(), [
            [0, -2],
            [0, -1],
            [0, 0],
            [1, 0],
        ])
        self.assertListEqual(self.card.get_offsets(3, rotate=0).tolist(), [
            [-1, -2],
            [-1, -1],
            [-1, 0],
            [0, 0],
        ])
