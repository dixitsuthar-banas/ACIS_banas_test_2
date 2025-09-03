from odoo import models, fields


class AcisBaseEncoding(models.Model):
    _name = 'acis.base.encoding'
    _description = 'Character Encoding'

    name = fields.Char(string='Encoding Name', required=True, help="E.g. cp850, iso-8859-1")
    description = fields.Char(string='Description')
    active = fields.Boolean(default=True)
    no_active = fields.Boolean(default=False)