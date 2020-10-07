# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.addons.web.controllers.main import Home, ensure_db, redirect_with_hash
from odoo.http import request


class KsHome(Home, http.Controller):

    @http.route('/web', type='http', auth="none")
    def web_client(self, s_action=None, **kw):
        ensure_db()
        # print("mirando ando")
        # print(request.env.user.browse(request.session.uid).id)
        if not kw.get('debug') is None:
            if request.env.user.browse(request.session.uid).id != 1:
                return redirect_with_hash('/web')
            # if request.env['ir.config_parameter'].sudo().get_param('ks_hide_debug_assets_permission'):
                    
        return super(KsHome, self).web_client(s_action=s_action, **kw)


