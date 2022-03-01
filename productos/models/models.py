# -*- coding: utf-8 -*-

from odoo import models, fields

class productos_productos(models.Model):
     _name = 'productos.productos'
     _description = 'productos.productos'
     name = fields.Integer(string="Número producto")
     tipo = fields.Many2one("productos.tipo",string="Tipo",required=True,ondelete="cascade")
     fecha = fields.Date(string="Fecha de lanzamiento")
     descripcion = fields.Char(string="Descripción")
     precio = fields.Float(string="Precio del producto")
     imagen= fields.Binary(string="Imagen producto") 
     anime = fields.Many2one("res.partner", string="Anime",required=True,ondelete="cascade")


class productos_tipo(models.Model):
     _name = 'productos.tipo'
     _description = 'productos.tipo'
     name = fields.Char(string="Categoria")
     subname = fields.Char(string="Subcategoria")
     # imagen = fields.Binary(string="Imagen general") 
     productos = fields.One2many("productos.productos","tipo",string="Productos")
     
     
     
class productos_anime(models.Model):
     _name = 'res.partner'
     _inherit = 'res.partner'
     
     productos = fields.One2many("productos.productos","anime",string="Productos")

# class productos(models.Model):
#     _name = 'productos.productos'
#     _description = 'productos.productos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
