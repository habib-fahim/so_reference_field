from odoo import api, models, fields
import re

class ManufacturingOrder(models.Model):
    _inherit = 'mrp.production'

    sale_order_id = fields.Many2one('sale.order', string="Sale Order", compute="_compute_sale_order", readonly=False)

    @api.depends("origin")
    def _compute_sale_order(self):
        for order in self:
            if order.origin:
                # Use regular expression to extract the code from origin
                code = re.search(r'\bS(\d+)$', order.origin)
                if code:
                    sale = order.env["sale.order"].search([("name", "=", code.group(0))], limit=1)
                    if sale:
                        order.sale_order_id = sale.id
                    else:
                        order.sale_order_id = False
                else:
                    order.sale_order_id = False
            else:
                order.sale_order_id = False