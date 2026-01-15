from odoo import models, fields, api

class InventoryItems(models.Model):
    _name = "inventory.items"
    _description = "Todos los items de inventario"

    name = fields.Char(string="Nombre", required=True)
    code = fields.Char(string="Codigo", default=0)
    quantity = fields.Integer(string="Cantidad")
    price = fields.Float(string="Precio")
    category = fields.Selection([
        ('electronica', 'Electronicos'),
        ('ropa', 'Ropa'),
        ('hogar', 'Hogar'),
        ('furniture', 'Muebles'),
    ], string="Categoria")
    description = fields.Text(string="Descripcion")
    active = fields.Boolean(string="Activo", default=True)