# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import werkzeug.wsgi
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

    product_supply_ids = fields.One2many('product.supplierinfo', 'name')

    docs_check = fields.Boolean(default=True) #true when partner needs docs check

    def set_docs_check(self):
        users = self.env['res.users'].search([('classification', '=', 'vendor')])
        for user in users:
            user.partner_id.docs_check = True
        return True

    def stripe_express_connect_account(self):

        payment_stripe = self.env['payment.acquirer'].search([('provider', '=', 'stripe')])
        # create express account
        s2s_data_account = {
            'type': 'express',
            'ccountry': 'ES',
            'email': self.email,
        }
        account = payment_stripe._stripe_request('accounts', s2s_data_account)

        # create account link
        s2s_data_account_link = {
            'account': account.get('id'),
            'refresh_url':"http:" + werkzeug.wsgi.get_host + "/reauth",
            'return_url': "http:" + werkzeug.wsgi.get_host + "/return",
            'type':'account_onboarding'
        }

        link = payment_stripe._stripe_request('account_links', s2s_data_account_link)
        
        # return link 
        if account.get('id') and link.get('url'):
            return link.get('url')
        else:
            return False