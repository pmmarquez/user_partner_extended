# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class Partner(models.Model):
    _inherit = 'res.partner'

    address_street = fields.Text('Address Street')
    address_floor = fields.Text('Address Floor')
    address_portal = fields.Text('Address Portal')
    address_number = fields.Text('Address Number')
    address_door = fields.Text('Address door')
    address_stairs = fields.Text('Address Stairs')
    address_zip_code = fields.Text('Address ZIP Code')
    address_latitude = fields.Text('Address Geo Latitude')
    address_longitude = fields.Text('Address Geo Longitude')
    vat_cif = fields.Char('CIF number')
    social_security = fields.Char('Social security number')
    iae_code = fields.Char('I.A.E code')
    dni = fields.Char('DNI number')