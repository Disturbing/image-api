# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server.models.base_model_ import Model
from server import util

class Parameter(Model):
    def __init__(self, parameter: str=None, value: str=None):  # noqa: E501
        """Parameter - a model defined in Swagger

        :param parameter: The parameter of this Parameter.  # noqa: E501
        :type parameter: str
        :param value: The value of this Parameter.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'parameter': str,
            'value': str
        }

        self.attribute_map = {
            'parameter': 'parameter',
            'value': 'value'
        }

        self._parameter = parameter
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Parameter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Parameter of this Parameter.  # noqa: E501
        :rtype: Parameter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def parameter(self) -> str:
        """Gets the parameter of this Parameter.


        :return: The parameter of this Parameter.
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter: str):
        """Sets the parameter of this Parameter.


        :param parameter: The parameter of this Parameter.
        :type parameter: str
        """
        if parameter is None:
            raise ValueError("Invalid value for `parameter`, must not be `None`")  # noqa: E501

        self._parameter = parameter

    @property
    def value(self) -> str:
        """Gets the value of this Parameter.


        :return: The value of this Parameter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Parameter.


        :param value: The value of this Parameter.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    def verify_parameter(self):
        if self._parameter is None:
            raise ValueError('Parameter improperly formed. Each Parameter must have property "parameter".')
        if self._value is None:
            raise ValueError('Parameter improperly formed. Each Parameter must have property "value".')

    @staticmethod
    def lookup(parameters, key):
        return next(filter(lambda x: x.get("parameter") == key, parameters), None)
