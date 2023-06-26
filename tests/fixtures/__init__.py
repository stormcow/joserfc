import json
from unittest import TestCase
from pathlib import Path

BASE_PATH = Path(__file__).parent


def read_fixture(filename: str):
    with open((BASE_PATH / filename).resolve()) as f:
        return json.load(f)


class TestFixture(TestCase):
    @classmethod
    def load_fixture(cls, filename: str, private_key, public_key):
        data = read_fixture(filename)

        payload = data.get('payload')
        root_id = data.get('id', '')
        for index, case in enumerate(data['cases']):
            if 'id' not in case:
                alg = case.get('alg', '')
                case['id'] = f'{root_id}_{alg}_{index}'

            if payload and 'payload' not in case:
                case['payload'] = payload
            cls.attach_case(case, private_key, public_key)

    @classmethod
    def attach_case(cls, data, private_key, public_key):

        def method(self):
            self.run_test(data, private_key, public_key)

        case_id = data['id']
        name = f'test_{case_id}'
        method.__name__ = name
        method.__doc__ = f'Run fixture {data}'
        setattr(cls, name, method)

    def run_test(self, case, private_key, public_key):
        raise NotImplementedError()
