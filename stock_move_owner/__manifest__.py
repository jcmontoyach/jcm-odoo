# -*- encoding: utf-8 -*-
#   Copyright 2017 Juan Carlos Montoya <jcarlosmontoyach@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Stock Move Owner",
    "version": "1.1",
    "author": "Juan Carlos Montoya",
    "website": "http://sdi.es",
    "license": "AGPL-3",
    "category": "Stock",
    'summary': """
        Agregar el propietario en los movimientos
        El propietario se toma del campo propietario en la ubicacion origen
        o destino
    """,
    "depends": [
        'stock',
    ],
    "data": [
        #'views/templates.xml'
    ],
    "installable": True,
    "application": True,
}
