from configs.domain_list import DomainList
from eve import ID_FIELD


def relation(resource: DomainList, required=True, embeddable=True):
    return {
        "type": "objectid",
        "required": required,
        "data_relation": {
            "resource": resource,
            "field": ID_FIELD,
            "embeddable": embeddable
        }
    }
