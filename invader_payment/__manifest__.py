# -*- coding: utf-8 -*-
# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Shopinvader Payment",
    "summary": "Payment integration for Shopinvader",
    "version": "10.0.2.0.1",
    "category": "e-commerce",
    "website": "https://github.com/shopinvader/None",
    "author": "ACSONE SA/NV",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": ["cerberus", "unidecode"], "bin": []},
    "depends": [
        "payment",
        "account_payment_mode",
        "component",
        "component_event",
    ],
    "data": ["views/account_payment_mode.xml"],
}
