# -*- coding: utf-8 -*-

from odoo import fields, api, models


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    product_ref_text = fields.Char('Reference')
