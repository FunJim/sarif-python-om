# This file was generated by jschema_to_python version 1.1.0.

import attr


@attr.s
class ExternalProperties(object):
    """The top-level element of an external property file."""

    addresses = attr.ib(default=None)
    artifacts = attr.ib(default=None)
    conversion = attr.ib(default=None)
    driver = attr.ib(default=None)
    extensions = attr.ib(default=None)
    externalized_properties = attr.ib(default=None)
    graphs = attr.ib(default=None)
    guid = attr.ib(default=None)
    invocations = attr.ib(default=None)
    logical_locations = attr.ib(default=None)
    policies = attr.ib(default=None)
    properties = attr.ib(default=None)
    results = attr.ib(default=None)
    run_guid = attr.ib(default=None)
    schema = attr.ib(default=None)
    taxonomies = attr.ib(default=None)
    thread_flow_locations = attr.ib(default=None)
    translations = attr.ib(default=None)
    version = attr.ib(default=None)
    web_requests = attr.ib(default=None)
    web_responses = attr.ib(default=None)
