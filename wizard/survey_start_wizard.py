# -*- coding: utf-8 -*-
from odoo import _, fields, models


class SurveyStartWizard(models.TransientModel):
    _name = 'survey.start.wizard'
    _description = "Start Survey for a Partner"

    survey_id = fields.Many2one('survey.survey', string="Survey", required=True)
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    require_login = fields.Boolean(related='survey_id.users_login_required')
    answer_id = fields.Many2one('survey.user_input', readonly=True)
    survey_start_link = fields.Char(string="Survey Link", readonly=True)

    def _answer(self):
        self.ensure_one()
        # create the answer for the partner
        if not self.answer_id:
            is_manager = self.env.user.has_group('survey.group_survey_manager')
            self.answer_id = self.survey_id._create_answer(partner=self.partner_id, check_attempts=not is_manager)
        return self.answer_id

    def action_generate_link(self):
        answer = self._answer()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        self.survey_start_link = base_url + answer.get_start_url()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'survey.start.wizard',
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    def action_start_survey(self):
        answer = self._answer()
        self.survey_id.message_post(body=_("Survey started for %(partner)s from %(user)s: %(answer)s",
            partner=self.partner_id.display_name,
            user=self.env.user.display_name,
            answer=answer._get_html_link(),
        ))
        return self.survey_id.action_start_survey(answer=answer)
