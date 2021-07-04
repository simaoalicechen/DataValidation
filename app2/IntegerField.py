"""
change IntegerField descriptors to inherit from BaseValidator
"""

import numbers

from app2.BaseValidator import BaseValidator


class IntegerField(BaseValidator):
    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be an integer.')
        if self._min is not None and value < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min}.')
        if self._max is not None and value > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max}')