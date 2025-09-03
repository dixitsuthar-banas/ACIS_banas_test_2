import logging
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class AcisBaseUoMMapping(models.Model):
    _name = 'acis.base.uom.mapping'
    _description = 'Unit of Measure Mapping'

    name = fields.Char('Unit of Measure', required=True)
    uom_id = fields.Many2one('uom.uom', string='Einheit')

