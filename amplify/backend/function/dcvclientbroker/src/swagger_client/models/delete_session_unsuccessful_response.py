# coding: utf-8

"""
    DCV Session Manager

    DCV Session Manager API  # noqa: E501

    OpenAPI spec version: 2020.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DeleteSessionUnsuccessfulResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'session_id': 'str',
        'failure_reason': 'str'
    }

    attribute_map = {
        'session_id': 'SessionId',
        'failure_reason': 'FailureReason'
    }

    def __init__(self, session_id=None, failure_reason=None):  # noqa: E501
        """DeleteSessionUnsuccessfulResponse - a model defined in Swagger"""  # noqa: E501
        self._session_id = None
        self._failure_reason = None
        self.discriminator = None
        if session_id is not None:
            self.session_id = session_id
        if failure_reason is not None:
            self.failure_reason = failure_reason

    @property
    def session_id(self):
        """Gets the session_id of this DeleteSessionUnsuccessfulResponse.  # noqa: E501

        The session id  # noqa: E501

        :return: The session_id of this DeleteSessionUnsuccessfulResponse.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this DeleteSessionUnsuccessfulResponse.

        The session id  # noqa: E501

        :param session_id: The session_id of this DeleteSessionUnsuccessfulResponse.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def failure_reason(self):
        """Gets the failure_reason of this DeleteSessionUnsuccessfulResponse.  # noqa: E501

        The failure reason  # noqa: E501

        :return: The failure_reason of this DeleteSessionUnsuccessfulResponse.  # noqa: E501
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this DeleteSessionUnsuccessfulResponse.

        The failure reason  # noqa: E501

        :param failure_reason: The failure_reason of this DeleteSessionUnsuccessfulResponse.  # noqa: E501
        :type: str
        """

        self._failure_reason = failure_reason

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DeleteSessionUnsuccessfulResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteSessionUnsuccessfulResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
