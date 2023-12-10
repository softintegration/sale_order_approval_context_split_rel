# -*- coding: utf-8 -*-

{
    'name': 'Sale order approval & Sale/Quotation context split conflict resolver',
    'version': '1.0.1',
    'author':'Soft-integration',
    'category': 'Sale',
    'description': "",
    'depends': [
        'sale_order_quotation_context_split','sale_order_approval'
    ],
    'data': [
        'views/sale_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
