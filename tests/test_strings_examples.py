import unittest
from sample.strings_example import StringsExamples
from mock import patch, Mock

class TestStringsExamples(unittest.TestCase):
    def test_concat_strings(self):
        string1 = "hola"
        string2 = "adios"
        result = StringsExamples.concat_strings(string1, string2)
        assert result == "holaadios"

    def test_concat_numbers(self):
        string1 = 123
        string2 = 456
        self.assertRaises(TypeError, StringsExamples.concat_strings, string1, string2)

    def test_concat_numbers_string(self):
        string1 = 123
        string2 = "asd"
        self.assertRaises(TypeError, StringsExamples.concat_strings, string1, string2)

    def test_concat_string_numbers(self):
        string1 = "asd"
        string2 = 123
        self.assertRaises(TypeError, StringsExamples.concat_strings, string1, string2)

    @patch('sample.strings_example.urllib2.urlopen')
    def test_get_first_string_from_internet(self, mock_urlopen):
        a = Mock()
        a.read.side_effect = ["hello good bye"]
        mock_urlopen.return_value = a
        assert StringsExamples.get_first_string() == "hello"



if __name__ == '__main__':
    unittest.main()
