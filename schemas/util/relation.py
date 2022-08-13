from configs.domain_list import DomainList


def relation(resource: DomainList, required: bool, embeddable=True):
    return {
        "type": "objectid",
        "required": required,
        "data_relation": {
            "resource": resource,
            "field": "_id",
            "embeddable": embeddable
        }
    }
