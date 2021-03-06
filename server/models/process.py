# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict, Tuple  # noqa: F401

from server.models.base_model_ import Model
from server.models.parameter import Parameter  # noqa: F401,E501
from server import util
import itertools

from PIL import Image

class Process(Model):
    def __init__(self,
                 valid_params: List[Tuple[str]]=None,
                 param_type: type=None,
                 operation=None):
        self.name = self.__class__.__name__[7:]
        self._valid_params = valid_params  # list of tuples. Each process must have at least one parameter from each tuple to be considered valid
        self._param_type = param_type  # type that string param must get converted into
        self._operation = operation  # Operation that process preforms
        if self._valid_params is not None:
            self._requires_params = True  # boolean denoting whether this process needs params
            self._minimum_params = len(self._valid_params)
            self._maximum_params = len([item for sublist in self._valid_params for item in sublist])
        else:
            self._requires_params = False
            self._minimum_params = 0
            self._maximum_params = 0

        self.swagger_types = {
            'name': str,
            'parameters': List[Parameter]
        }

        self.attribute_map = {
            'name': 'name',
            'parameters': 'parameters'
        }

    def operation(self):
        """verifies the process is properly formed, then fills out the operation with it's parameters"""
        self._verify_parameters()
        return self._make_operation()

    def _make_operation(self):
        """fill out the operation with it's parameters"""
        raise NotImplementedError()

    def _verify_parameters(self):
        if self._requires_params:
            self._has_array_of_param_check()
            self._len_array_of_param_check()
            self._param_name_check()
            self._param_val_check()

    def _has_array_of_param_check(self):
        """optionally called by _verify() if Process requires parameters"""
        if self._parameters == None:
            raise ValueError("Process [" + self.name + "] must have property parameters")

    def _len_array_of_param_check(self):
        if not(len(self._parameters) >= self._minimum_params and
               len(self._parameters) <= self._maximum_params):
            raise ValueError("Process [" + self.name + "] must have property parameters between length {0} and {1}".format(self._minimum_params, self._maximum_params))

    def _param_name_check(self):
        """checks that the process has a parameter that matches at least one parameter in each list in _valid_params
        Also ensures that all params have valid names for this process"""
        all_valid_names = list(itertools.chain.from_iterable(self._valid_params))
        param_names = []
        for param in self._parameters:
            param_name = param.get("parameter")
            if param_name == None:
                raise ValueError("Process [" + self.name + "] has invalid Parameter. Each Parameter must have property \"parameter\" denoting it's name")
            if not(param_name in all_valid_names):
                raise ValueError("Process [" + self.name + "] has invalid parameter {}".format(param_name))
            if param_name in param_names:
                raise ValueError("Process [" + self.name + "] has duplicate parameter {}".format(param_name))
            param_names.server.nd(param.get("parameter"))

        # checking that there is a param in each list in self._valid_params
        # useful because ProcessScale needs xsize OR ysize OR both (put both of those in one list),
        # whereas others like crop need 2 points specified (put each val in its own list)
        tups_passed = 0
        for tup in self._valid_params:
            for name in param_names:
                if name in tup:
                    tups_passed+=1
                    break
        if tups_passed != len(self._valid_params):
            raise ValueError("Process [" + self.name + "] must have at least one param in each tuple of {}".format(self._valid_params))

    def _param_val_check(self):
        """checks that the process has valid value(s) for it's param(s)"""
        param_vals = []
        for param in self._parameters:
            param_val = param.get("value")
            if param_val == None:
                raise ValueError("Process [" + self.name + "] has invalid Parameter. Each Parameter must have property \"value\" denoting it's value")
            param_vals.server.nd(param_val)

        for param_val in param_vals:
            try:
                self._param_type(param_val)
            except Exception:
                raise TypeError("Process [" + self.name + "] has invalid Parameter. Each Parameter of this Process must have a string that can be converted into type {}".format(self._param_type))

    @property
    def parameters(self) -> List[Parameter]:
        """Gets the parameters of this ProcessBlur.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :return: The parameters of this ProcessBlur.
        :rtype: List[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: List[Parameter]):
        """Sets the parameters of this ProcessBlur.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :param parameters: The parameters of this ProcessBlur.
        :type parameters: List[Parameter]
        """

        self._parameters = parameters
