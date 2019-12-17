import os
from unittest import TestCase

from workshop.Golem import Golem
from workshop.GolemBuilder import GolemBuilder 


class TestGolem(TestCase):
    
    def test_golem_init(self):
        test_golem = Golem(10, 'Golem', {'test_param': 'test_val'})
        assert test_golem.id == 10
        assert test_golem.type == 'Golem'
        assert test_golem.config['test_param'] == 'test_val'


class TestGolemBuilder(TestCase):

    def test_golem_init_run(self):
        test_golem = GolemBuilder(1, 'GolemBuilder', {'golem_name': 'test'})
        assert test_golem.id == 1
        assert test_golem.type == 'GolemBuilder'
        assert test_golem.config['golem_name'] == 'test'
        assert os.path.exists(f'{os.getcwd()}/workshop/test.py')
        os.remove(f'{os.getcwd()}/workshop/test.py')
        # TODO: add the lines to test file creation and removal after the test
