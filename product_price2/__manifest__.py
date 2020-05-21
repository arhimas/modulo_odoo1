# -*- coding: utf-8 -*-
{
    'name': 'Product price 2',
    'summary': "Módulo Cambios para introducir un nuevo campo price 2 en el formulario de productos",
    'description': """Módulo hecho siguiendo paso a paso en IDE Pycharm para introducir un nuevo campo""",
    'version': '1.0',
    'category': 'Sales',
    'author': "TheLastMonkey",
    'website': 'https://www.odoo.com/page/notes',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list


    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
    "views/product_view.xml",
    ],
}
