# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.osv import fields, osv
from datetime import time, datetime

class openacademy_student(osv.osv):
	_name = 'openacademy.student'
	_description = 'Formulario de Estudiantes'
	# _rec_name = 'campo'
	_columns = {
	   'name' : fields.char('Nombre del estudiante', size=256, required=True, help='Aqui pones el nombre'),
	   'fecha' : fields.date('Fecha de nacimiento', help='Fecha de Nacimiento'),
	   'edad' : fields.integer('Edad', size=10, required=True),
	   'active' : fields.boolean('Activo'),
	   'state' : fields.selection([('draft','Borrador'),('confirmed','Confirmado'),('cancel','Cancelado')], 'Estado', readonly=True),
	   'escuela_id' : fields.many2one('res.partner', 'Escuela' , required=True),
	   'horario_ids' : fields.one2many('openacademy.lines','student_id','Holario de Clases')
	   }

	_defaults = {
        'fecha' : fields.datetime.now,
        'state' : 'draft',
        'active' : 'true'
    }

	def confirm(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'state':'confirmed'}, context=None)
		return True

	def cancel(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'state':'cancel'}, context=None)
		return True

	def draft(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'state':'draft'}, context=None)
		return True	


     # self -> Que hace referencia a la clase que se esta definiendo
     # cr -> Cursor de la base que se esta utilizando
     # uid -> El usuario que esta modificando un registro
     # ids -> Listado de los registros que estamos consultando
     # context -> Contine el lenguaje, el idioma y otros atributos


class res_partner(osv.osv):
	_name = 'res.partner'
	_inherit = 'res.partner'
	_columns = {
        'school' : fields.boolean('Escuela'),
	}


class openacademy_lines(osv.osv):
	_name = 'openacademy.lines'
	_description = 'Materias'
	_columns = {
	    'student_id' : fields.many2one('openacademy.student' , 'ID Referencia'),
        'name' : fields.char('Nombre de la Materia', size=64, required=True),
        'horario' : fields.text('Horario de Clases' , required=True),
	}





