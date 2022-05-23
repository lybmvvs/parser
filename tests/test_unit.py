import pytest
import numpy as np
from lib.pre_parser import clear_of_rubbish
from lib.pre_parser import probels_clearing
from lib.pre_parser import to_normal_view
from lib.post_parser import frame_creation

class Test_clear_of_rubbish:
    @pytest.fixture
    def test_first_func(self):

        self.input_file = 'test_input/test_schedule.inc'

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






