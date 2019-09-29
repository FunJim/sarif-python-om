# This file was generated by jschema_to_python version 1.1.0.

import attr


@attr.s
class SarifLog(object):
    """Static Analysis Results Format (SARIF) Version 2.1.0-rtm.4 JSON Schema: a standard format for the output of static analysis tools."""

    runs = attr.ib()
    version = attr.ib()
    schema_uri = attr.ib(default=None)
    inline_external_properties = attr.ib(default=None)
    properties = attr.ib(default=None)
