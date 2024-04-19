# -*- coding: utf-8 -*-
# from odoo import http


# class FmSoReferenceField(http.Controller):
#     @http.route('/fm_so_reference_field/fm_so_reference_field', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fm_so_reference_field/fm_so_reference_field/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fm_so_reference_field.listing', {
#             'root': '/fm_so_reference_field/fm_so_reference_field',
#             'objects': http.request.env['fm_so_reference_field.fm_so_reference_field'].search([]),
#         })

#     @http.route('/fm_so_reference_field/fm_so_reference_field/objects/<model("fm_so_reference_field.fm_so_reference_field"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fm_so_reference_field.object', {
#             'object': obj
#         })
