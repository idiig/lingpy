from functools import partial

class _strings(list):

    def __init__(self, type_, iterable):
        
        list.__init__(self, [type_(x) for x in (iterable if not isinstance(iterable, str) else
                iterable.split())])

    def __str__(self):

        return ' '.join([str(x) for x in self])

strings = partial(_strings, str)
ints = partial(_strings, int)
floats = partial(_strings, float)


class lists(_strings):

    def __init__(self, iterable, sep=" + "):

        _strings.__init__(self, str, iterable)
        self.n = [strings(x) for x in iterable.split(sep)]
        self.sep = sep
        
        
