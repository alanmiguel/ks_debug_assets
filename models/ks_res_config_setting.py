# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ks_hide_debug_assets_permission = fields.Boolean(string='Hide Debug Assets', config_parameter='ks_hide_debug_assets_permission')

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('ks_hide_debug_assets_permission',
                                                         self.ks_hide_debug_assets_permission)

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            ks_hide_debug_assets_permission=self.env['ir.config_parameter'].sudo().get_param(
                'ks_hide_debug_assets_permission'))
        return res
