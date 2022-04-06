from collections.abc import Mapping
from functools import wraps

from app.http.response import ResponseFailure, ResponseTypes
from flask import request, jsonify


class invalidRequest:
    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False


class validRequest:
    def __init__(self, filters=None):
        self.filters = filters

    def __bool__(self):
        return True


def build_list_request(filters=None):
    accepted_filters = ["code__eq", "price__eq", "price__lt", "price__gt"]
    invalid_req = invalidRequest()

    if filters is not None:
        if not isinstance(filters, Mapping):
            invalid_req.add_error("filters", "Is not iterable")
            return invalid_req

        for key, _ in filters.items():
            if key not in accepted_filters:
                invalid_req.add_error("filters", "Key {} cannot be used".format(key))

        if invalid_req.has_errors():
            return invalid_req

    return validRequest(filters=filters)


def json_body_required(f):
    """JSON body required"""

    @wraps(f)
    def decorator(*args, **kwargs):
        # Halts the request if the JSON object is empty
        if not len(request.json):
            response = ResponseFailure(
                ResponseTypes.PARAMETERS_ERROR, "JSON body is empty"
            )
            return response.value, 403

        return f(*args, **kwargs)

    return decorator
