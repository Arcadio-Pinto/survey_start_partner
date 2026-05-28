# -*- coding: utf-8 -*-
from odoo.http import request
from odoo.addons.survey.controllers.main import Survey


class Survey(Survey):

    def _check_validity(self, survey_token, answer_token, ensure_token=True, check_partner=True):
        user = request.env.user
        if check_partner and not user._is_public() and user.has_group('survey.group_survey_user'):
            check_partner = False
        return super()._check_validity(survey_token, answer_token, ensure_token=ensure_token, check_partner=check_partner)
