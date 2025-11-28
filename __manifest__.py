{
    'name': 'Tag Sequence Manager',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Analytic',
    'summary': 'Gestor de colecciones y secuencias de etiquetas analíticas',
    'author': 'Assistant',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/sequence_manager_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}