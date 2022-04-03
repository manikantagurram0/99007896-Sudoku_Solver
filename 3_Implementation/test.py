import unittest
from pythoncode import *


class CellTests(unittest.TestCase):
    def set_up(self):
        pass

    def test_cell_not_editable_and_value_0(self):
        with self.assertRaises(AttributeError) as cm:
            cell = Cell(0, 0, editable=False, value=0)

        self.assertTrue("Cell not editable and without value" in str(cm.exception))

    def test_cell_value_below_0(self):
        with self.assertRaises(AttributeError) as cm:
            cell = Cell(0, 0, value=-1)

        self.assertTrue("Incorrect value (-1 not in <0,{}>)".format(Cell.MAX_VALUE) in str(cm.exception))

    def test_cell_value_over_MAX(self):
        value = Cell.MAX_VALUE
        with self.assertRaises(AttributeError) as cm:
            cell = Cell(0, 0, value=value+1)

        self.assertTrue("Incorrect value ({} not in <0,{}>)".format(value+1, value) in str(cm.exception))

    def test_cell_not_editable_and_correct_value(self):
        cell = Cell(0, 0, editable=False, value=1)
        self.assertFalse(cell.editable)
        self.assertEqual(cell.value, 1)
        self.assertTrue(cell.possible_values == set())

    def test_cell_editable_and_correct_value(self):
        cell = Cell(0, 0, editable=True, value=1)
        self.assertTrue(cell.editable)
        self.assertEqual(cell.value, 1)
        self.assertTrue(cell.possible_values == set(range(1, Cell.MAX_VALUE + 1)))

    def test_cell_set_value(self):
        cell = Cell(0, 0, editable=True, value=0)
        cell.value = 1
        self.assertEqual(cell.value, 1)

    def test_cell_not_editable_set_value(self):
        cell = Cell(0, 0, editable=False, value=1)
        with self.assertRaises(AttributeError) as cm:
            cell.value = 2
        self.assertTrue("Cell not editable" in str(cm.exception))




if __name__ == '__main__':
    unittest.main()