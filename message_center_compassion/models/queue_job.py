# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2017 Compassion CH (http://www.compassion.ch)
#    Releasing children from poverty in Jesus' name
#    @author: Emanuel Cino <ecino@compassion.ch>
#
#    The licence is in the file __manifest__.py
#
##############################################################################

from odoo import api, models, _


class QueueJob(models.Model):
    _inherit = 'queue.job'

    @api.multi
    def related_action_messages(self):
        action = {
            'name': _("Messages"),
            'type': 'ir.actions.act_window',
            'res_model': 'gmc.message.pool',
            'domain': [('id', 'in', self.record_ids)],
            'view_type': 'form',
            'view_mode': 'tree,form',
        }
        return action
