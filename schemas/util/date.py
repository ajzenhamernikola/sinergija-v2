from datetime import datetime


def json_date(required=True):
    return {
        "type": "date",
        "required": required,
        "coerce": lambda d: datetime.strptime(d, "%Y-%m-%dT%H:%M:%S.%fZ")
    }
