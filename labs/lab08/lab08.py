def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
    "*** YOUR CODE HERE ***"
    def new_gen(item):
            g_new = g()
            g_new_item = next(g_new)
            yield g_new_item
            while g_new_item != item:
                g_new_item = next(g_new)
                yield g_new_item
                
    g_loop = g()
    item = next(g_loop, None)
    while item != None:
        yield new_gen(item)
        item = next(g_loop, None)
                
        

