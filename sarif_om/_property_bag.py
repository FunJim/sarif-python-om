# This file was generated by jschema_to_python version 1.1.0.

import attr


@attr.s
class PropertyBag(object):
    """Key/value pairs that provide additional information about the object."""

    tags = attr.ib(default=None)
