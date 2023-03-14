import pytest
from calc import probability_calc

'''
class Balls:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def selected_balls():
    return Balls("")


@pytest.fixture
def hat(selected_balls):
    return [Balls(""), selected_balls]


def test_balls_in_hat(selected_balls, hat):
    assert selected_balls in hat
'''

#There is a hat containing
#5 blue balls, 4 red balls, 2 green balls.
def hat():
    balls = {"blue":5,
            }

def there_are_5_blue_balls_in_hat("blue" : 5, hat)
    assert {"blue" : 5} in hat

