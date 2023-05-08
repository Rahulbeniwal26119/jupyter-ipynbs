from unittest import TestCase, main
from unittest.mock import Mock, ANY
from tempfile import TemporaryDirectory

import warnings


def absolute_fn(x=None):
    if not x:
        x = 0
        warnings.warn("x is None")
    if x <= 0:
        return -x
    else:
        return x


class TestWarning(TestCase):
    assert absolute_fn(-1) == 1
    assert absolute_fn(1) == 1
    assert absolute_fn() == 0


def setUpModule():
    print('setUpModule')

def tearDownModule():
    print('tearDownModule')


class IntegrationTest(TestCase):
    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test_integration(self):
        print("test_integration")

    def test_another_integration(self):
        print("test_another_integration")


def to_str(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        raise TypeError("Must supply str or bytes, found: %r" % data)


def sum_sqaure(values):
    cumulative = 0
    for value in values:
        cumulative += value ** 2
        yield cumulative


class HelperTestCase(TestCase):
    def verify_complex_case(self, values, expected):
        expect_it = iter(expected)
        found_it = iter(sum_sqaure(values))
        test_it = zip(expect_it, found_it)

        for i, (expected, found) in enumerate(test_it):
            print((expected, found))
            self.assertEqual(expected, found, 'Index %i is wrong.' % i)

        try:
            next(expect_it)
        except StopIteration:
            pass
        else:
            self.fail('Expected longer than found.')

        try:
            next(found_it)
        except StopIteration:
            pass
        else:
            self.fail('Expected longer than found.')

    def test_wrong_length(self):
        values = [1, 2, 3]
        expected = [1, 5, 14, 30]
        self.verify_complex_case(values, expected)

    def test_wrong_result(self):
        values = [1, 2, 3]
        expected = [1, 5, 14]
        self.verify_complex_case(values, expected)

    def test_right(self):
        values = [1, 2, 3]
        expected = [1, 5, 14]
        self.verify_complex_case(values, expected)


class UtilsTestCase(TestCase):
    def test_to_str_bytes(self):
        self.assertEqual('hello', to_str(b'hello'))

    def test_to_str_str(self):
        self.assertEqual('hello', to_str('hello'))

    def test_failing(self):
        self.assertEqual('incorrect', to_str('hello'))

    def test_to_str_bad(self):
        with self.assertRaises(TypeError):
            to_str(object())

    def test_to_str_bad_encoding(self):
        with self.assertRaises(UnicodeDecodeError):
            to_str(b'\xfa\xfa')


class DataDrivenTestCase(TestCase):
    def test_good(self):
        good_case = [
            (b'my bytes', 'my bytes'),
            ('other str', 'other str')
        ]

        for value, expected in good_case:
            with self.subTest(value):
                self.assertEqual(expected, to_str(value))

    def test_bad(self):
        bad_case = [
            (object(), TypeError),
            (b'\xfa\xfa', UnicodeDecodeError)
        ]

        for value, expection in bad_case:
            with self.subTest(value):
                with self.assertRaises(expection):
                    to_str(value)


class EnvironmentTest(TestCase):
    def setUp(self) -> None:
        self.test_dir = TemporaryDirectory()
        # self.test_path = Path(self.test_dir.name)

    def tearDown(self) -> None:
        # self.test_dir.cleanup()
        pass

    def test_modify_file(self):
        print(self.test_dir.name)
        with open(self.test_dir.name + '/test.txt', 'w') as f:
            f.write('hello world')
        print("Inside the test case")
        self.assertTrue(False)

def get_animals():
    return ['dog', 'cat', 'mouse']

mock = Mock(spec=get_animals)
mock.return_value = ['mocked', 'animals']

obj = object()
# result = mock(obj, 'arg1', 'arg2')
# mock.assert_called_with(ANY, 'arg1', 'arg2')
# assert result == ['mocked', 'animals']
main()
