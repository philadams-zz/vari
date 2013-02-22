#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

Color representation conversions in Python.
"""

import re

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

        if color:

            # handle hex
            if color.startswith('#'):
                if HEX_COLOR.match(color):
                    self.hex = color
                elif HEX_COLOR_SHORT.match(color):
                    self.hex_short = color

            # TODO handle web

        for k, v in kwargs.iteritems():
            setattr(self, k, v)

        # if we've not set self._rgb, we couldn't init the color
        if not self._rgb:
            raise ValueError('cannot initialize Vari instance')

    def __getattr__(self, label):
        if ('get_' + label) in self.__class__.__dict__:
            return getattr(self, 'get_' + label)()
        else:
            raise AttributeError("'%s' not an attribute" % label)

    def __setattr__(self, label, value):
        if label == '_rgb':
            self.__dict__[label] = value
        else:
            fnc = getattr(self, 'set_' + label)
            fnc(value)

    def __eq__(self, other):
        return self._rgb == other._rgb

    def __repr__(self):
        return '<Vari rgb=%s>' % self.hex

    def get_rgb(self):
        return self._rgb

    def get_hex(self):
        return rgb2hex(self._rgb)

    def set_rgb(self, rgb):
        self._rgb = rgb

    def set_hex(self, clr):
        self._rgb = hex2rgb(clr)

    def set_hex_short(self, clr):
        clr = '#' + ''.join(['%s%s' % (e,e) for e in clr[1:]])
        self._rgb = hex2rgb(clr)


def main(args):
    pass


def cli():
    import argparse

    # populate and parse command line options
    desc = 'Color representation conversions in Python.'
    desc += '\nhttp://github.com/philadams/vari'
    parser = argparse.ArgumentParser(description=desc)
    args = parser.parse_args()

    print('commandline tool coming soon...')
