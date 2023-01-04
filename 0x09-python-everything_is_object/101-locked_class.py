#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("You are not allowed to set new attributes on this object")
        else:
            self.__dict__[name] = value

