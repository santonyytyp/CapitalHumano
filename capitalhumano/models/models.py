# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Colaboradores(models.Model):
        _name = 'capitalhumano.colaboradores'

        #Info basica
        name = fields.Char(string="Title", required=True)
        correo = fields.Text()
        telefono = fields.Text()
        skype = fields.Text()
        #Info de contacto
        dirTrab = fields.Text()
        celular = fields.Text()
        dirOfic = fields.Text()
        #
        compania = fields.Text()
        usuarioerp = fields.Text()
        correo = fields.Text()


        direccion = fields.Text()

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


