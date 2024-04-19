from odoo import models, fields, api


class StockValuationLayer(models.Model):
    _inherit = "stock.valuation.layer"

    # Modify related fields
    sale_order_reference = fields.Many2one(
        string="Sales Order Reference",
        related='stock_move_id.group_id.mrp_production_ids.sale_order_id',
        store=True,
        search='_search_sale_order_reference'  # Add search method for searchability
    )

    sale_order_customer_name = fields.Many2one(
        string="Customer",
        related='sale_order_reference.partner_id',  # Simplify dependency
        store=True,
        search='_search_sale_order_customer_name'  # Add search method for searchability
    )

    # Define search method for sale_order_reference
    def _search_sale_order_reference(self, operator, value):
        return [('stock_move_id.group_id.mrp_production_ids.sale_order_id', operator, value)]

    # Define search method for sale_order_customer_name
    def _search_sale_order_customer_name(self, operator, value):
        return [('sale_order_reference.partner_id', operator, value)]