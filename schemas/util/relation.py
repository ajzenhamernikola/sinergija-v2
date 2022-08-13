from configs.domain_list import DomainList


def relation(resource: DomainList, embeddable=True):
    return {
        "type": "objectid",
        "required": True,
        "data_relation": {
            "resource": resource,
            "field": "_id",
            "embeddable": embeddable
        }
    }
