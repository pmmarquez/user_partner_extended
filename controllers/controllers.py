# -*- coding: utf-8 -*-
import logging
import werkzeug

from odoo import http
from odoo.http import request


class StripeLinkController(http.Controller):

    @http.route('/payment/stripe/reauth', type='http', auth='none')
    def stripe_refresh_account_link(self,**kwargs):
        data = kwargs.copy()
        old_link = request.env['res.partner'].sudo().search([('id', '=', data['partner_id'])]).stripe_connect_account_link
        link = request.env['res.partner'].sudo().search([('id', '=', data['partner_id'])]).generate_stripe_connect_account_link(data['account_id'], data['reauth_url'], data['return_url'])
        if (link):
            return werkzeug.utils.redirect(link.get('url'))
        else:
            return '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"><title>Link gneration error...</title><p>Try manual: <a href="%s">%s</a>. click the link.' %(old_link, old_link)
        
    @http.route('/payment/stripe/return', type='http', auth='none')
    def stripe_refresh_account_link(self,**kwargs):
        data = kwargs.copy()
        old_link = request.env['res.partner'].sudo().search([('id', '=', data['partner_id'])]).stripe_connect_account_link
        account_verified = request.env['res.partner'].sudo().search([('id', '=', data['partner_id'])]).verify_stripe_connect_account()

        display_location = werkzeug.utils.escape(old_link)
        if isinstance(old_link, str):
            location = werkzeug.urls.iri_to_uri(old_link, safe_conversion=True)
        error_response = werkzeug.wrappers.Response(
            '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n'
            '<title>Redirecting...</title>\n'
            '<body><script>alert("Account data incomplete, redirect to account form");</script>\n'
            '<h1>Redirecting...</h1>\n'
            '<p>You should be redirected automatically to new link: '
            '<a href="%s">%s</a>.  If not click the link.</p></body>' %
            (werkzeug.utils.escape(location), display_location), 302, mimetype='text/html')
        error_response.headers['Location'] = location

        if (account_verified):
            return '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"><title>Success...</title><h1>Correctly account verification</h1>'
        else:
            return error_response
     
