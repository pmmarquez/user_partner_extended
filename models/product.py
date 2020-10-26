# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    classification = fields.Selection([
        ('service', 'Service'),
        ('cost', 'Service cost'),
        ], readonly=True)