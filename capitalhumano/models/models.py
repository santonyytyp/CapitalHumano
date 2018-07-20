# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
from datetime import timedelta

class Colaboradores(models.Model):
	_name = 'capitalhumano.colaboradores'
	#Info basica
	name = fields.Char(string="Nombre",required=True)
	correo = fields.Char()
	telefono = fields.Char()
	skype = fields.Char()
	imagen = fields.Binary()

	##Informacion publica##
        #Info de contacto
	dirTrab = fields.Text()
	celTrab = fields.Char()
	dirOfi = fields.Text()
	compania = fields.Char()
	usuarioerp = fields.Many2one('res.users', string="Usuario ERP", index=True, ondelete='set null')
	#Cargo
	departamento = fields.Many2one('capitalhumano.departamentos', index=True, ondelete='set null')
	tituloTrab = fields.Char()
	jefeInmediato = fields.Many2one('capitalhumano.colaboradores', ondelete='set null')
	director = fields.Many2one('capitalhumano.colaboradores', ondelete='set null')
	esDirector = fields.Boolean(default=False)

	##Informacion personal##
	#Ciudadania e info adicional
	nacionalidad = fields.Many2one('res.country', ondelete="set null")
	nIdentificacion = fields.Integer()
	nPasaporte = fields.Integer()
	nCuentabancaria = fields.Integer()
	otroID = fields.Char()
	#Info de contacto 2
	direccion = fields.Text()
	#Estado
	sexo = fields.Char()
	estadoCivil = fields.Char()
	nHijos = fields.Integer()
	#Nacimiento
	fechaNac = fields.Date()
	lugarNac = fields.Date()
	edad = fields.Integer()

	##Expediente##
	#Expediente
	curp = fields.Char()
	nEmpleado = fields.Integer()
	nss = fields.Integer()
	gradoEstudios = fields.Char()
	tipoSangre = fields.Char()
	infonavit = fields.Char()
	#Baja
	fechaIngreso = fields.Date()
	fechaBaja = fields.Date()
	motivoBaja = fields.Text()
	#Beneficiarios
	#
	beneficiarios_ids = fields.Many2many('capitalhumano.beneficiarios', string="Beneficiarios")
	#Referencias familiares
	#
	#Auxiliar
	#
	#Documentos
	dcv = fields.Boolean(default=False)
	dine = fields.Boolean(default=False)
	dan = fields.Boolean(default=False)
	dnss = fields.Boolean(default=False)
	dcurp = fields.Boolean(default=False)
	ddomi = fields.Boolean(default=False)
	dar = fields.Boolean(default=False)
	drfc = fields.Boolean(default=False)
	dcl = fields.Boolean(default=False)
	drp = fields.Boolean(default=False)
	dcnap = fields.Boolean(default=False)
	dlc = fields.Boolean(default=False)
	d2fti = fields.Boolean(default=False)
	dcuge = fields.Boolean(default=False)
	dstyp = fields.Boolean(default=False)
	dpsi = fields.Boolean(default=False)
	drl = fields.Boolean(default=False)
	dcp = fields.Boolean(default=False)
	dci = fields.Boolean(default=False)
	dcc = fields.Boolean(default=False)
	dap = fields.Boolean(default=False)
	dimss = fields.Boolean(default=False)
	dsv = fields.Boolean(default=False)
	drit = fields.Boolean(default=False)
	dem = fields.Boolean(default=False)

	##Informacion publica##
	#Ausencias
	auResPer = fields.Integer()
	#Contrato
	examenMedico = fields.Date()
	vehiculoCompania = fields.Char()
	disTarea = fields.Integer()
	#Hojas de trabajo
	producto = fields.Char()
	diario = fields.Char()
	#Activo
	activo = fields.Boolean(defalut=True)


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class beneficiarios(models.Model):
	_name = 'capitalhumano.beneficiarios'
	name = fields.Char(string="Nombre", required=True)
	bDireccion = fields.Char()
	brfc = fields.Char()
	bporcentaje = fields.Integer()


class departamento(models.Model):
	_name = 'capitalhumano.departamentos'
#
	name = fields.Char(required=True)
	encargado = fields.Many2one('capitalhumano.colaboradores', ondelete='set null')
	descripcion = fields.Text()
	departamentoPadre = fields.Many2one('capitalhumano.departamentos', ondelete='set null')
