# -*- encoding: utf-8 -*-
#   Copyright 2017 Juan Carlos Montoya <jcarlosmontoyach@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.model
    def create(self, values):
        res = super(StockMove, self).create(values)

        for move in res:
            if not move.restrict_partner_id:
                if move.picking_type_id.code == 'incoming':
                    move.restrict_partner_id = move.location_dest_id.partner_id
                elif move.picking_type_id.code == 'outgoing':
                    move.restrict_partner_id = move.location_id.partner_id
        return res
