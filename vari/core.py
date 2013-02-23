#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

Color representation conversions in Python.
"""

import re

from helpers import COLORS_NAMES

COLORS_RGB = dict((v, k) for k, v in COLORS_NAMES.iteritems())
HEX_COLOR = re.compile(r'^#[0-9a-fA-F]{6}')
HEX_COLOR_SHORT = re.compile(r'^#[0-9a-fA-F]{3}')


def rgb2hex(clr):
    return '#' + ''.join(map(chr, clr)).encode('hex')


def hex2rgb(clr):
    return tuple(map(ord, clr[1:].decode('hex')))


class Vari(object):
    """Color representation and representation conversion.
    In Finnish, väri means color."""

    def __init__(self, color=None, **kwargs):

        self._rgb = None  # internal repr
        self.update(color, **kwargs)

        # if we've not set self._rgb, we couldn't init the color
        if not self._rgb:
            raise ValueError('cannot initialize Vari instance')

    def update(self, color, **kwargs):

        # handle kwargs[rgb]
        if 'rgb' in kwargs:
            self._rgb = tuple(map(int, kwargs['rgb']))

        elif color:

            # handle hex
            if color.startswith('#'):
                if HEX_COLOR.match(color):
                    self._rgb = hex2rgb(color)
                elif HEX_COLOR_SHORT.match(color):
                    clr = '#' + ''.join(['%s%s' % (e,e) for e in color[1:]])
                    self._rgb = hex2rgb(clr)

            # handle web
            elif color in COLORS_NAMES:
                self._rgb = COLORS_NAMES[color]


    def __eq__(self, other):
        return self._rgb == other._rgb

    def __repr__(self):
        return '<Vari %s>' % self.hex

    @property
    def rgb(self):
        return self._rgb

    @rgb.setter
    def rgb(self, rgb):
        self._rgb = rgb

    @property
    def hex(self):
        return rgb2hex(self._rgb)

    @property
    def web(self):
        return COLORS_RGB.get(self._rgb, self.hex)

def cli():
    import argparse

    # populate and parse command line options
    desc = 'Color representation conversions in Python.'
    desc += '\nhttp://github.com/philadams/vari'
    parser = argparse.ArgumentParser(description=desc)
    args = parser.parse_args()

    print('commandline tool coming soon...')
