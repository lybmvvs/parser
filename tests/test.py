import pytest
import numpy as np
from lib.parser import to_pars


class TestLineParsersUnit:
    @pytest.fixture
    def test_parser_data(self):

        self.input_file = 'test_input/test_schedule.inc'

        self.parsing_result = [
            [np.nan, 'W1', np.nan, '10', '10', '1', '3', 'OPEN', '1*', '1', '2', '1',
             '3*', '1.0'],
            [np.nan, 'W2', np.nan, '32', '10', '1', '3', 'OPEN', '1*', '1', '2', '1',
             '3*', '2.0'],
            [np.nan, 'W3', np.nan, '5', '36', '2', '2', 'OPEN', '1*', '1', '2', '1',
             '3*', '3.0'],
            [np.nan, 'W4', np.nan, '40', '30', '1', '3', 'OPEN', '1*', '1', '2', '1',
             '3*', '4.0'],
            [np.nan, 'W5', np.nan, '21', '21', '4', '4', 'OPEN', '1*', '1', '2', '1',
             '3*', '5.0'],
            ['01 JUL 2018', 'W3', np.nan, '32', '10', '1', '1', 'OPEN', '1*', '1', '2', '1',
             '3*', '1.0718'],
            ['01 JUL 2018', 'W5', np.nan, '21', '21', '1', '3', 'OPEN', '1*', '1', '2', '1',
             '3*', '5.0'],
            ['01 SEP 2018', 'W1', np.nan, '10', '10', '2', '3', 'OPEN', '1*', '1', '2', '1',
             '3*', '1.0918'],
            ['01 SEP 2018', 'W2', np.nan, '32', '10', '1', '2', 'OPEN', '1*', '1', '2', '1',
             '3*', '2.0'],
            ['01 SEP 2018', 'W3', 'LGR1', '10', '10', '2', '2', 'OPEN', '1*', '1', '2', '1',
             '3*', '1.0918'],
            ['01 JUN 2018', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
             np.nan, np.nan],
            ['01 AUG 2018', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
             np.nan, np.nan],
            ['01 OCT 2018', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
             np.nan, np.nan],
            ['01 NOV 2018', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
             np.nan, np.nan],
            ['01 DEC 2018', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
             np.nan, np.nan]]

    def test_parser_result(self, test_parser_data):

        assert to_pars(self.input_file).values.tolist() == self.parsing_result