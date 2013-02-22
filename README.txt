väri
====

Color representations and representation conversions in Python. _Väri_ means
'color' in Finnish.

install
-------

`pip install vari`. Done.

use
---

Create a `Vari` instance with one of many color representations:

    Vari(rgb=(255, 0, 0))
    Vari('#ff0000')

Ask the instance for other representations:

    c = Vari('#f00')
    c.rgb  # (255, 0, 0)
    c.hex  # '#ff0000'

acknowledgements
----------------

The search from rgb to x256 is a python port of [node-x256][node-x256] (MIT license, James Halliday).

future
------

- python port of substack/node-x256 for terminal colors
- human readable CSS web color list
- hsl repr

[node-x256]: https://github.com/substack/node-x256
