import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class AnalyticCustomTag(models.Model):
    _name = 'analytic.custom.tag'
    _description = 'Etiqueta Analítica'
    _rec_name = 'code' 
    _order = 'code'

    plan_id = fields.Many2one('analytic.custom.plan', string='Plan / Cliente', required=True, ondelete='cascade')

    code = fields.Char(string='Código', required=True, index=True, help="Identificador único dentro del plan")
    name = fields.Char(string='Nombre', required=True)

    # Campo Many2many para etiquetas de la OCA
    analytic_tag_ids = fields.Many2many(
        comodel_name='account.analytic.tag', 
        string='Secuencia de Etiquetado',
        help="Etiquetas analíticas oficiales asociadas a este registro"
    )

    # NUEVO CAMPO: Activo
    # Al llamarlo 'active', Odoo maneja automáticamente el archivado/desarchivado
    active = fields.Boolean(string='Activo', default=True)

    _sql_constraints = [
        ('code_plan_uniq', 'unique (code, plan_id)', 'El código debe ser único dentro del mismo Plan Contable.')
    ]

    @api.depends('code', 'name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.code}] {rec.name}"

class AnalyticCustomPlan(models.Model):
    _name = 'analytic.custom.plan'
    _description = 'Plan Contable Analítico'
    _order = 'name'

    name = fields.Char(string='Nombre del Plan / Cliente', required=True, help="Ej: Renault, Porsche")
    description = fields.Text(string='Descripción')

    tag_ids = fields.One2many('analytic.custom.tag', 'plan_id', string='Etiquetas Analíticas')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'El nombre del plan debe ser único.')
    ]

    def init(self):
        _logger.info(">>> MODELO ANALYTIC CUSTOM PLAN CARGADO EN MEMORIA <<<")