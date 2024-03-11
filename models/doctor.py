from odoo import fields, models

class Doctor(models.Model):
    _name = 'hms.doctor'
    _description = 'Doctor'
    _rec_name = 'first_name'

    first_name = fields.Char("First Name")
    last_name = fields.Char('Last Name')
    image = fields.Binary()
