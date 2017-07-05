# -*- encoding: utf-8 -*-
#   Copyright 2017 Odoo 10 Juan Carlos Montoya  <jcarlosmontoyach@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner(self):
        if self.partner_id:
            domain = [('partner_id', '=', self.partner_id.id)]
            # wdb.set_trace()
            locations = self.env['stock.location'].search(domain)
            if locations:
                return {"domain": {
                    "location_dest_id": [('id', 'in', locations._ids)]}}
        return {"domain": {'location_dest_id': []}}
