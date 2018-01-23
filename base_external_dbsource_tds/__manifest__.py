# -*- coding: utf-8 -*-
# Copyright <2018> <Yoandy Rodríguez Martínez>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl)
{
    'name': 'External Database Source - PyTDS',
    'summary':
    'Python only adapter for external Microsoft SQL Server Databases',
    'version': '10.0.0.1.0',
    'category': 'Tools',
    'author': "Yoandy Rodríguez Martínez",
    'website': 'https://github.com/yorodm/odoo-tools',
    'license': 'LGPL-3',
    'depends': [
        'base_external_dbsource',
    ],
    # Uncomment this for v11
    # 'external_dependencies': [
    #     'python': [
    #         'python-tds',
    #     ]
    # ],
    'installable': True,
    'auto_install': True,  # Remove this key for v11
}
