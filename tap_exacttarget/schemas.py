custom_property_list = {
    'type': 'array',
    'inclusion': 'available',
    'description': ('Specifies key-value pairs of properties associated with '
                    'an object.'),
    'items': {
        'type': 'object',
        'properties': {
            'Name': {'type': 'string'},
            'Value': {'type': 'string'},
        }
    }
}

event = {
    'type': 'object',
    'properties': {
        'SendID': {
            'type': 'integer',
            'description': 'Contains identifier for a specific send.',
        },
        'EventDate': {
            'type': 'string',
            'format': 'datetime',
            'description': 'Date when a tracking event occurred.',
        },
        'EventType': {
            'type': 'string',
            'description': 'The type of tracking event',
        },
        'SubscriberKey': {
            'type': 'string',
            'description': 'Identification of a specific subscriber.',
        }
    }
}

send = {
    'type': 'object',
    'properties': {
        'CreatedDate': {
            'type': 'string',
            'format': 'date-time',
            'description': ('Read-only date and time of the object\'s '
                            'creation.'),
        },
        'EmailName': {
            'type': 'string',
            'description': ('Specifies the name of an email message '
                            'associated with a send.'),
        },
        'FromAddress': {
            'type': 'string',
            'description': ('Indicates From address associated with a '
                            'object. Deprecated for email send definitions '
                            'and triggered send definitions.'),
        },
        'FromName': {
            'type': 'string',
            'description': ('Specifies the default email message From Name. '
                            'Deprecated for email send definitions and '
                            'triggered send definitions.'),
        },
        'ID': {
            'type': 'integer',
            'description': ('Read-only legacy identifier for an object. Not '
                            'supported on all objects. Some objects use the '
                            'ObjectID property as the Marketing Cloud unique '
                            'ID.'),
        },
        'IsAlwaysOn': {
            'type': 'boolean',
            'description': ('Indicates whether the request can be performed '
                            'while the system is is maintenance mode. A value '
                            'of true indicates the system will process the '
                            'request.'),
        },
        'IsMultipart': {
            'type': 'boolean',
            'description': ('Indicates whether the email is sent with '
                            'Multipart/MIME enabled.'),
        },
        'ModifiedDate': {
            'type': 'string',
            'format': 'date-time',
            'description': ('Indicates the last time object information '
                            'was modified.'),
        },
        'PartnerProperties': custom_property_list,
        'SendDate': {
            'type': 'string',
            'format': 'date-time',
            'description': ('Indicates the date on which a send occurred.'
                            'Set this value to have a CST (Central Standard '
                            'Time) value.'),
        },
        'SentDate': {
            'type': 'string',
            'format': 'date-time',
            'description': 'Indicates date on which a send took place.',
        },
        'Status': {
            'type': 'string',
            'description': 'Defines status of object. Status of an address.',
        },
        'Subject': {
            'type': 'string',
            'description': 'Contains subject area information for a message.',
        }
    }
}

subscriber = {
    'type': 'object',
    'properties': {
        'Addresses': {
            'type': 'array',
            'inclusion': 'available',
            'description': ('Indicates addresses belonging to a subscriber, '
                            'used to create, retrieve, update or delete an '
                            'email or SMS Address for a given subscriber.'),
            'items': {
                'type': 'object',
                'properties': {
                    'Address': {'type': 'string'},
                    'AddressType': {'type': 'string'},
                    'AddressStatus': {'type': 'string'}
                }
            }
        },
        'Attributes': custom_property_list,
        'CorrelationID': {
            'type': 'string',
            'inclusion': 'available',
            'description': ('Identifies correlation of objects across '
                            'several requests.'),
        },
        'CreatedDate': {
            'type': 'string',
            'inclusion': 'available',
            'description': 'Read-only date and time of the object\'s creation.'
        },
        'CustomerKey': {
            'type': 'string',
            'inclusion': 'automatic',
            'description': ('User-supplied unique identifier for an object '
                            'within an object type (corresponds to the '
                            'external key assigned to an object in the user '
                            'interface).'),
        },
        'EmailAddress': {
            'type': 'string',
            'inclusion': 'available',
            'description': ('Contains the email address for a subscriber. '
                            'Indicates the data extension field contains '
                            'email address data.'),
        },
        'EmailTypePreference': {
            'type': 'string',
            'inclusion': 'available',
            'description': 'The format in which email should be sent'
        },
        'ID': {
            'type': 'int',
            'inclusion': 'automatic',
            'description': ('Read-only legacy identifier for an object. Not '
                            'supported on all objects. Some objects use the '
                            'ObjectID property as the Marketing Cloud unique '
                            'ID.'),
        },
        'ListIDs': {
            'type': 'array',
            'inclusion': 'available',
            'description': 'Defines list IDs a subscriber resides on.',
            'items': {
                'type': 'string'
            }
        },
        'Locale': {
            'type': 'string',
            'inclusion': 'available',
            'description': ('Contains the locale information for an Account. '
                            'If no location is set, Locale defaults to en-US '
                            '(English in United States).'),
        },
        'ModifiedDate': {
            'type': ['string', 'null'],
            'inclusion': 'automatic',
            'description': ('Indicates the last time object information was '
                            'modified.')
        },
        'ObjectID': {
            'type': 'string',
            'inclusion': 'automatic',
            'description': ('System-controlled, read-only text string '
                            'identifier for object.'),
        },
        'ObjectState': {
            'type': 'string',
            'inclusion': 'available',
            'description': 'Reserved for future use.'
        },
        'PartnerKey': {
            'type': 'string',
            'inclusion': 'available',
            'description': ('Unique identifier provided by partner for an '
                            'object, accessible only via API.'),
        },
        'PartnerProperties': custom_property_list,
        'PartnerType': {
            'type': 'string',
            'inclusion': 'available',
            'description': 'Defines partner associated with a subscriber.'
        },
        'PrimaryEmailAddress': {
            'type': 'string',
            'inclusion': 'available',
            'description': 'Indicates primary email address for a subscriber.'
        },
        'PrimarySMSAddress': {
            'type': 'string',
            'inclusion': 'available',
            'description': ('Indicates primary SMS address for a subscriber. '
                            'Used to create and update SMS Address for a '
                            'given subscriber.'),
        },
        'PrimarySMSPublicationStatus': {
            'type': 'string',
            'inclusion': 'available',
            'description': 'Indicates the subscriber\'s modality status.',
        },
        'Status': {
            'type': 'string',
            'inclusion': 'available',
            'description': 'Defines status of object. Status of an address.',
        },
        'SubscriberKey': {
            'type': 'string',
            'inclusion': 'automatic',
            'description': 'Identification of a specific subscriber.',
        },
        'SubscriberTypeDefinition': {
            'type': 'string',
            'inclusion': 'available',
            'description': ('Specifies if a subscriber resides in an '
                            'integration, such as Salesforce or Microsoft '
                            'Dynamics CRM'),
        },
        'UnsubscribedDate': {
            'type': 'string',
            'inclusion': 'available',
            'description': ('Represents date subscriber unsubscribed '
                            'from a list.'),
        }
    }
}
