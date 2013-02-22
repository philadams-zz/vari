# -*- coding: utf-8 -*-

from .context import vari

import unittest


class VariTestSuite(unittest.TestCase):

    def setUp(self):
        self.red = vari.Vari(rgb=(255, 0, 0))

    def test_color_instance_comparison(self):
        red = vari.Vari(rgb=(255, 0, 0))
        self.assertEqual(self.red, red)

    def test_load_hex(self):
        red = vari.Vari('#ff0000')
        self.assertEqual(self.red, red)

    def test_load_hex_short(self):
        red = vari.Vari('#f00')
        self.assertEqual(self.red, red)

    def test_load_name(self):
        red = vari.Vari('red')
        self.assertEqual(self.red, red)

    def test_2rgb(self):
        self.assertEqual((255, 0, 0), self.red.rgb)

    def test_2hex(self):
        self.assertEqual('#ff0000', self.red.hex)

    def test_2web(self):
        self.assertEqual('red', self.red.web)


if __name__ == '__main__':
    unittest.main()
