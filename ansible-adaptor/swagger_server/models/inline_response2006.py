# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse2006(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name: str=None, type: str=None, properties: object=None):
        """
        InlineResponse2006 - a model defined in Swagger

        :param name: The name of this InlineResponse2006.
        :type name: str
        :param type: The type of this InlineResponse2006.
        :type type: str
        :param properties: The properties of this InlineResponse2006.
        :type properties: object
        """
        self.swagger_types = {
            'name': str,
            'type': str,
            'properties': object
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'properties': 'properties'
        }

        self._name = name
        self._type = type
        self._properties = properties

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2006':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_6 of this InlineResponse2006.
        :rtype: InlineResponse2006
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """
        Gets the name of this InlineResponse2006.

        :return: The name of this InlineResponse2006.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this InlineResponse2006.

        :param name: The name of this InlineResponse2006.
        :type name: str
        """

        self._name = name

    @property
    def type(self) -> str:
        """
        Gets the type of this InlineResponse2006.

        :return: The type of this InlineResponse2006.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """
        Sets the type of this InlineResponse2006.

        :param type: The type of this InlineResponse2006.
        :type type: str
        """

        self._type = type

    @property
    def properties(self) -> object:
        """
        Gets the properties of this InlineResponse2006.

        :return: The properties of this InlineResponse2006.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties: object):
        """
        Sets the properties of this InlineResponse2006.

        :param properties: The properties of this InlineResponse2006.
        :type properties: object
        """

        self._properties = properties

