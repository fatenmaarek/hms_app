from odoo import fields, models

class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'
    _rec_name = 'first_name'

    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float('CR Ratio')
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ])
    pcr = fields.Boolean('PCR')
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer()
    department_id = fields.Many2one('hms.department')
    doctor_id = fields.Many2one('hms.doctor')
    department_capacity = fields.Integer(related='department_id.capacity')
    status = fields.Selection([
        ('undetermined','Undetermined'),
        ('good','Good'),
        ('fair','Fair'),
        ('serious','Serious'),
    ])
    
