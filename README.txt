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
    Vari('red')

Ask the instance for other representations:

    c = Vari('#f00')
    c.rgb  # (255, 0, 0)
    c.hex  # '#ff0000'
    c.x256  # 196

future
------

- hsl repr
