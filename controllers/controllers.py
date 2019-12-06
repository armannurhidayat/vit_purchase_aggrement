# -*- coding: utf-8 -*-
from odoo import http

# class VitPurchesAggrement(http.Controller):
#     @http.route('/vit_purches_aggrement/vit_purches_aggrement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_purches_aggrement/vit_purches_aggrement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_purches_aggrement.listing', {
#             'root': '/vit_purches_aggrement/vit_purches_aggrement',
#             'objects': http.request.env['vit_purches_aggrement.vit_purches_aggrement'].search([]),
#         })

#     @http.route('/vit_purches_aggrement/vit_purches_aggrement/objects/<model("vit_purches_aggrement.vit_purches_aggrement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_purches_aggrement.object', {
#             'object': obj
#         })