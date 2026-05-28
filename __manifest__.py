# -*- coding: utf-8 -*-
{
    'name': 'Survey - Start for Partner',
    'version': '18.0.1.0.0',
    'category': 'Surveys',
    'summary': "Start a survey for a partner from the kanban view",
    'description': """
Adds a "Start Survey" button on the survey kanban, next to "Share".
It opens a wizard where you pick a partner: on confirm a result
(survey.user_input) is created for that partner and the survey is opened.
    """,
    'author': 'Arcadio',
    'depends': ['survey'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/survey_start_wizard_views.xml',
        'views/survey_survey_views.xml',
    ],
    'license': 'LGPL-3',
}
