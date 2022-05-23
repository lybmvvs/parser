import pytest

import numpy as np
from lib.pre_parser import clear_of_rubbish
from lib.pre_parser import probels_clearing
from lib.pre_parser import to_normal_view
from lib.post_parser import frame_creation


class Test_clear_of_rubbish:
    @pytest.fixture
    def test_first_func(self):

        self.input_file = open("test_input/test_schedule.inc")

        self.parsing_result = ['COMPDAT',
                    '',
                    'W1 10 10  1   3  OPEN  1*  1 2  1  3*    1.0',
                    'W2 32 10  1   3  OPEN  1*  1  2  1  3*    2.0',
                    '',
                    '',
                    'COMPDAT',
                    '',
                    'W3 5  36  2   2  OPEN  1*  1  2  1  3*    3.0',
                    'W4 40 30  1   3  OPEN  1*  1  2  1  3*    4.0',
                    '',
                    '',
                    'COMPDAT',
                    '',
                    'W5 21 21  4   4  OPEN  1*  1  2  1 3*    5.0',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    'DATES',
                    '01 JUN 2018',
                    '',
                    '',
                    '',
                    '',
                    '',
                    'WEFAC',
                    'W1 1.0',
                    '',
                    '',
                    'DATES',
                    '01 JUL 2018',
                    '',
                    '',
                    'COMPDAT',
                    'W3 32 10  1   1  OPEN  1*  1  2  1  3*    1.0718',
                    'W5 21 21  1   3  OPEN  1*  1  2  1 3*    5.0',
                    '',
                    '',
                    'DATES',
                    '01 AUG 2018',
                    '01 SEP 2018',
                    '',
                    '',
                    'COMPDAT',
                    'W1 10 10  2   3  OPEN  1*  1 2  1  3*    1.0918',
                    'W2 32 10  1   2  OPEN  1*  1  2  1  3*    2.0',
                    '',
                    '',
                    'COMPDATL',
                    'W3 LGR1 10 10  2   2  OPEN  1*  1 2  1  3*    1.0918',
                    '',
                    '',
                    'DATES',
                    '01 OCT 2018',
                    '',
                    '',
                    'DATES',
                    '01 NOV 2018',
                    '',
                    '',
                    'DATES',
                    '01 DEC 2018',
                    '',
                    '',
                    'END']
    def test_first_func_result(self, test_first_func):

        assert clear_of_rubbish(self.input_file) == self.parsing_result


class Test_probels_clearing:
    @pytest.fixture
    def test_sec_func(self):

        self.input_file = clear_of_rubbish(open("test_input/test_schedule.inc"))

        self.parsing_result = ['COMPDAT',
                    'W1 10 10  1   3  OPEN  1*  1 2  1  3*    1.0',
                    'W2 32 10  1   3  OPEN  1*  1  2  1  3*    2.0',
                    'COMPDAT',
                    'W3 5  36  2   2  OPEN  1*  1  2  1  3*    3.0',
                    'W4 40 30  1   3  OPEN  1*  1  2  1  3*    4.0',
                    'COMPDAT',
                    'W5 21 21  4   4  OPEN  1*  1  2  1 3*    5.0',
                    'DATES',
                    '01 JUN 2018',
                    'WEFAC',
                    'W1 1.0',
                    'DATES',
                    '01 JUL 2018',
                    'COMPDAT',
                    'W3 32 10  1   1  OPEN  1*  1  2  1  3*    1.0718',
                    'W5 21 21  1   3  OPEN  1*  1  2  1 3*    5.0',
                    'DATES',
                    '01 AUG 2018',
                    '01 SEP 2018',
                    'COMPDAT',
                    'W1 10 10  2   3  OPEN  1*  1 2  1  3*    1.0918',
                    'W2 32 10  1   2  OPEN  1*  1  2  1  3*    2.0',
                    'COMPDATL',
                    'W3 LGR1 10 10  2   2  OPEN  1*  1 2  1  3*    1.0918',
                    'DATES',
                    '01 OCT 2018',
                    'DATES',
                    '01 NOV 2018',
                    'DATES',
                    '01 DEC 2018',
                    'END']
    def test_sec_func_result(self, test_sec_func):

        assert probels_clearing(self.input_file) == self.parsing_result


class Test_to_normal_view:
    @pytest.fixture
    def test_third_func(self):

        self.input_file = probels_clearing(clear_of_rubbish(open("test_input/test_schedule.inc")))

        self.parsing_result = [['COMPDAT',
                'W1 10 10  1   3  OPEN  1*  1 2  1  3*    1.0',
                'W2 32 10  1   3  OPEN  1*  1  2  1  3*    2.0',
                'COMPDAT',
                'W3 5  36  2   2  OPEN  1*  1  2  1  3*    3.0',
                'W4 40 30  1   3  OPEN  1*  1  2  1  3*    4.0',
                'COMPDAT',
                'W5 21 21  4   4  OPEN  1*  1  2  1 3*    5.0'],
                ['DATES', '01 JUN 2018'],
                ['DATES',
                '01 JUL 2018',
                'COMPDAT',
                'W3 32 10  1   1  OPEN  1*  1  2  1  3*    1.0718',
                'W5 21 21  1   3  OPEN  1*  1  2  1 3*    5.0'],
                ['DATES', '01 AUG 2018'],
                ['DATES',
                '01 SEP 2018',
                'COMPDAT',
                'W1 10 10  2   3  OPEN  1*  1 2  1  3*    1.0918',
                'W2 32 10  1   2  OPEN  1*  1  2  1  3*    2.0',
                'COMPDATL',
                'W3 LGR1 10 10  2   2  OPEN  1*  1 2  1  3*    1.0918'],
                ['DATES', '01 OCT 2018'],
                ['DATES', '01 NOV 2018'],
                ['DATES', '01 DEC 2018']]
    def test_third_func_result(self, test_third_func):

        assert to_normal_view(self.input_file) == self.parsing_result

class Test_frame_creation:
    @pytest.fixture
    def test_fourth_func(self):

        self.input_file = to_normal_view(probels_clearing(clear_of_rubbish(open("test_input/test_schedule.inc"))))

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


    def test_third_func_result(self, test_fourth_func):

        assert frame_creation(self.input_file).values.tolist() == self.parsing_result

