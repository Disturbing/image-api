# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util


class ProcessCrop(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type: str=None, array_of_parameter: List[Parameter]=None):  # noqa: E501
        """ProcessCrop - a model defined in Swagger

        :param type: The type of this ProcessCrop.  # noqa: E501
        :type type: str
        :param array_of_parameter: The array_of_parameter of this ProcessCrop.  # noqa: E501
        :type array_of_parameter: List[Parameter]
        """
        self.swagger_types = {
            'type': str,
            'array_of_parameter': List[Parameter]
        }

        self.attribute_map = {
            'type': 'type',
            'array_of_parameter': 'array_of_Parameter'
        }

        self._type = type
        self._array_of_parameter = array_of_parameter

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessCrop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Crop of this ProcessCrop.  # noqa: E501
        :rtype: ProcessCrop
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this ProcessCrop.

        The type of image processing you want to preform. See Enum for array of supported processes.  # noqa: E501

        :return: The type of this ProcessCrop.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ProcessCrop.

        The type of image processing you want to preform. See Enum for array of supported processes.  # noqa: E501

        :param type: The type of this ProcessCrop.
        :type type: str
        """
        allowed_values = ["Rotate", "Scale", "Crop", "Mirror", "Color", "Brightness", "Contrast", "Sharpen", "Blur", "maxFilter", "minFilter", "modeFilter", "medianFilter", "Edge", "Reformat"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def array_of_parameter(self) -> List[Parameter]:
        """Gets the array_of_parameter of this ProcessCrop.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :return: The array_of_parameter of this ProcessCrop.
        :rtype: List[Parameter]
        """
        return self._array_of_parameter

    @array_of_parameter.setter
    def array_of_parameter(self, array_of_parameter: List[Parameter]):
        """Sets the array_of_parameter of this ProcessCrop.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :param array_of_parameter: The array_of_parameter of this ProcessCrop.
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
