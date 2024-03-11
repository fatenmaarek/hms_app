{
    'name': "Hospital Management System",
    'summary': """ """,
    'author': "Faten maarek",
    'category': 'Productivity',
    'version': '17.0.0.1.0',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/hms_base_menus.xml',
        'views/hms_patient.xml',
        'views/hms_department.xml',
        'views/hms_doctor.xml',
    ],
}