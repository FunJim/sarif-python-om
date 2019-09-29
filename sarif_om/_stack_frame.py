# This file was generated by jschema_to_python version 1.1.0.

import attr


@attr.s
class StackFrame(object):
    """A function call within a stack trace."""

    location = attr.ib(default=None)
    module = attr.ib(default=None)
    parameters = attr.ib(default=None)
    properties = attr.ib(default=None)
    thread_id = attr.ib(default=None)
