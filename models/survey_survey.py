# -*- coding: utf-8 -*-
from odoo import models


class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    def action_open_start_survey_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': "Start Survey",
            'res_model': 'survey.start.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_survey_id': self.id},
        }
