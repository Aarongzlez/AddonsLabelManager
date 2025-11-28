{
    'name': 'Plan Contable Analítico Personalizado',
    'version': '18.0.1.0.2',
    'category': 'Accounting/Analytic',
    'summary': 'Gestión de planes analíticos y etiquetas personalizadas por cliente',
    'author': 'Assistant',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/analytic_structure_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}