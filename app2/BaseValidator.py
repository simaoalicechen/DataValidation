"""
Refactor the code and create a BaseValidator class that will handle the common functionality.
"""


class BaseValidator:
    def __init__(self, min_=None, max_=None):
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

    def validate(self, value):
        # this will need to be implemented specifically by each subclass
        # here we just default to not raising any exceptions
        pass

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.prop_name] = value
