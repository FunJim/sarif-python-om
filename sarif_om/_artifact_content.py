# This file was generated by jschema_to_python version 1.1.0.

import attr


@attr.s
class ArtifactContent(object):
    """Represents the contents of an artifact."""

    binary = attr.ib(default=None)
    properties = attr.ib(default=None)
    rendered = attr.ib(default=None)
    text = attr.ib(default=None)
