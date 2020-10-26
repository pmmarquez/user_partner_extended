# -*- coding: utf-8 -*-
{
    'name': "user_partner_extended",

    'summary': """
        Extend res.users and res.partner method and fields""",

    'description': """
        - ADD res.users new field classification (custumer,vendor,admin)
        - ADD res.partner several info fields
        - ADD product classification (service, cost)
        - ADD partner product.supplierinfo relation to create subscriptions to products from partner creation
    """,

    'author': "pmmarquez@gmx.com",

    'category': 'Administration',
    'version': '0.1',
    
    'depends': ['base','product'],

    # always loaded
    # 'data': [
    #     # 'security/ir.model.access.csv',
    #     'views/views.xml',
    #     'views/templates.xml',
    # ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
