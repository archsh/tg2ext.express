# -*- coding: utf-8 -*-
class NormalError(Exception):
    _code_ = 500

    def __init__(self, message=None, code=None, details=None):
        super(NormalError, self).__init__()
        self._message = message or self.__class__.__name__
        self._code = code or self._code_
        self._details = details
        #self.__dict__ = dict(code=self._code,
        #                     message=self._message,
        #                     details=self._details)

    def __repr__(self):
        return "<%s: %d (%s)>" % (self.__class__.__name__, self._code, self._message)

    def __unicode__(self):
        return u"<%s: %d (%s)>" % (self.__class__.__name__, self._code, self._message)


class ServerFault(NormalError):
    _code_ = 500
    pass


class FatalError(NormalError):
    _code_ = 501
    pass


class BadRequest(NormalError):
    _code_ = 400
    pass


class InvalidExpression(NormalError):
    _code_ = 400
    pass


class NotFound(NormalError):
    _code_ = 404
    pass


class InvalidData(NormalError):
    _code_ = 400
    pass


class Forbidden(NormalError):
    _code_ = 403
    pass


class Unauthorized(NormalError):
    _code_ = 401
    pass


__all__ = ['NormalError', 'BadRequest', 'InvalidExpression', 'InvalidData', 'NotFound',
           'FatalError', 'ServerFault', 'Forbidden', 'Unauthorized']