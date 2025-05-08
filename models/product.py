from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_outlet_item = fields.Boolean(string="Is Outlet Item", default=False)
