# -*- coding: utf-8 -*-
{
    'name': "user_partner_extended",

    'summary': """
        Extend res.users and res.partner method and fields""",

    'description': """
        - ADD res.users new field classification (custumer,vendor,admin)
    """,

    'author': "pmmarquez@gmx.com",

    'category': 'Administration',
    'version': '0.1',
    
    'depends': ['base'],

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
