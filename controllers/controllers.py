# -*- coding: utf-8 -*-
import logging
import werkzeug

from odoo import http
from odoo.http import request


class StripeLinkController(http.Controller):

    @http.route('/payment/stripe/reauth', type='http', auth='none')
    def stripe_refresh_account_link(self,**kwargs):
        data = kwargs.copy()
        link = request.env['res.partner'].sudo().search([('id', '=', data['partner_id'])]).stripe_connect_account_link(data['account_id'], data['reauth_url'], data['return_url'])
        if (link):
            return werkzeug.utils.redirect(link.get('url'))
        else:
            return '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"><title>Redirecting...</title><h1>Link Generation Error</h1>'
        

