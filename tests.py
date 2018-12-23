"""Unittests for habr proxy"""

import unittest

from utils import HabrParser


class TestStringMethods(unittest.TestCase):
    """Test parser work"""

    def test_baselink(self):
        """Test inner link replacing"""

        input = 'https://habr.com/custom/link'.encode('utf-8')
        output = '/custom/link'.encode('utf-8')
        self.assertEqual(HabrParser.do_related(input), output)


    def test_mobilelink(self):
        """Test mobile link replacing"""

        input = 'https://m.habr.com/custom/link'.encode('utf-8')
        output = '/mobile/custom/link'.encode('utf-8')
        self.assertEqual(HabrParser.do_related(input), output)

    def test_storagelink(self):
        """Test storage link replacing"""

        input = 'https://habrastorage.org/custom/link'.encode('utf-8')
        output = '/storage/custom/link'.encode('utf-8')
        self.assertEqual(HabrParser.do_related(input), output)

    def test_cdnlink(self):
        """Test CDN link replacing"""

        input = 'https://dr.habracdn.net/custom/link'.encode('utf-8')
        output = '/cdn/custom/link'.encode('utf-8')
        self.assertEqual(HabrParser.do_related(input), output)

    def test_endtrade(self):
        """Test adding custom chars"""

        input = '<body>Hello, Marlin</body>'.encode('utf-8')
        marked = str(HabrParser.mark_special_words(input))
        self.assertNotEqual(marked.find('Marlin&trade;'), -1)

    def test_begintrade(self):
        """Test adding custom chars"""

        input = '<body>Marlin is winner</body>'.encode('utf-8')
        marked = str(HabrParser.mark_special_words(input))
        self.assertNotEqual(marked.find('Marlin&trade;'), -1)

    def test_centertrade(self):
        """Test adding custom chars"""

        input = '<body>My name is Marlin and i am a boy</body>'.encode('utf-8')
        marked = str(HabrParser.mark_special_words(input))
        self.assertNotEqual(marked.find('Marlin&trade;'), -1)


if __name__ == '__main__':
    unittest.main()
