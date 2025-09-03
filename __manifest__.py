{
    'name': 'ACIS Base',
    'version': '18.0.1.0.2',
    'license': 'LGPL-3',
    'author': 'ACIS GmbH',
    'summary': 'Base models and views',
    'description': """
    This module contains base models and views used by 
    other modules.
    """,
    'category': 'Technical',
    'website': 'www.acis.at',
    'depends': [
        'uom'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/uom_mapping_views.xml',
        'views/encoding_views.xml',
    ]
}
