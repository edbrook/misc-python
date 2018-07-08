#!/usr/bin/env python

def _qs(value):
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


class TypedList(list):
    def __init__(self, type_):
        print(f"Construct new TypedList({_qs(type_)}) - ", end='')
        if not isinstance(type_, type):
            raise TypeError(f"Must pass a valid type, not {type(type_).__name__}")
        self.type_ = type_
        print("OK")

    def append(self, value):
        print(f"Try to append {_qs(value)} - ", end='')
        if not isinstance(value, self.type_):
            raise ValueError(f"Values must be of type {self.type_.__qualname__}")
        super().append(value)
        print("OK")
    
    def extend(self, values):
        for value in values:
            self.append(value)


if __name__ == "__main__":
    def try_(fn, *args):
        try:
            return fn(*args)
        except Exception as e:
            print(f"ERROR: {e}")

    try_(TypedList, "Python")
    try_(TypedList, 1024)
    l = lambda: 2048
    try_(TypedList, l)

    print()
    tl = try_(TypedList, int)
    try_(tl.append, 42)
    try_(tl.extend, [43, "thirty-six"])
    try_(tl.append, "hello")
    print(tl)
    
    print()
    sl = TypedList(str)
    try_(sl.append, "Hello")
    try_(sl.extend, ["world", 24, "hours"])
    try_(sl.append, 48)
    print(sl)

    print()
    tltl = try_(TypedList, TypedList)
    try_(tltl.append, TypedList(int))
    try_(tltl.extend, [TypedList(str), 346, TypedList(float)])
    try_(tltl.append, 3198)
    try_(tltl[0].append, 1048576)
    try_(tltl[0].extend, (1, 2, 2.5, 3))
    try_(tltl[1].append, "2222")
    try_(tltl[1].extend, ("1", 2, "2.5", "3"))
    print(tltl)