# -*- coding: utf-8 -*-
from odoo import http

# class Capitalhumano(http.Controller):
#     @http.route('/capitalhumano/capitalhumano/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/capitalhumano/capitalhumano/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('capitalhumano.listing', {
#             'root': '/capitalhumano/capitalhumano',
#             'objects': http.request.env['capitalhumano.capitalhumano'].search([]),
#         })

#     @http.route('/capitalhumano/capitalhumano/objects/<model("capitalhumano.capitalhumano"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('capitalhumano.object', {
#             'object': obj
#         })