import pytest
from main import is_valid_password


@pytest.mark.parametrize('string, expected', [('a 1 - 5 abcdj', True),
                                              ('z 2 - 4 asfalseruqwo', False),
                                              ('b 3 - 6 bhhkkbbjjjb', True),
                                              ('1 11 - 5 abcdj', False),
                                              ('z 2 - 4 asfaaaalseruqwozzz', True),
                                              ('z 0 - 4 asfaaaalseruqwozzz', True),
                                              ('z 0 - 0 asfaaaalseruqwozzz', False),
                                              ('d d - 3 asdasdasqdw', False),
                                              ('w v - a asdasdasqdw', False),
                                              ('a 1 - a asdasdasqdw', False),
                                              ('1 1 - 3 12312312', True),
                                              ])
def test_is_valid_function(string: str, expected: bool):
    assert is_valid_password(string) == expected
