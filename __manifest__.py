
{
    'name': "hfb_evoke_general_quality_module",
    'summary': """test""",
    'description': """test""",
    'author': "MakerONE",
    'website': "http://www.test.com",
    'category': 'Tools',
    'version': '0.5',
    'depends': ['base','mail','portal'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/quality.xml',

    ],

    'installable': True,
    'application': True,
}
