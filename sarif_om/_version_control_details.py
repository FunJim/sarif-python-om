# This file was generated by jschema_to_python version 1.1.0.

import attr


@attr.s
class VersionControlDetails(object):
    """Specifies the information necessary to retrieve a desired revision from a version control system."""

    repository_uri = attr.ib()
    as_of_time_utc = attr.ib(default=None)
    branch = attr.ib(default=None)
    mapped_to = attr.ib(default=None)
    properties = attr.ib(default=None)
    revision_id = attr.ib(default=None)
    revision_tag = attr.ib(default=None)
