# Ensure pytest-xdist is installed to enable parallel test execution
# Run tests with: pytest -n <num_processes>
from mypackage.geometry import Point
from mypackage.utils import distance
from time import sleep


def test_something():
    sleep(5)
    assert 1 == 2


def test_distance():
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    sleep(5)
    assert distance(p1, p2) == 5.0


def new_test():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    sleep(5)
    assert distance(p1, p2) == 5.0
