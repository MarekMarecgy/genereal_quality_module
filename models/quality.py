# -*- coding: utf-8 -*-
##############################################################################
#
#	Odoo, Open ERP Source Management Solution
#	Copyright (C) 2022 Hadron for business sp. z o.o. (http://www.hadron.eu.com)
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU Affero General Public License as
#	published by the Free Software Foundation, either version 3 of the
#	License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU Affero General Public License for more details.
#
#	You should have received a copy of the GNU Affero General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
"""
	@version	0.5
	@owner  Hadron for Business
	@author MakerONE
	@date   2022.11.14
"""

from odoo import models, api, fields, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

import logging

_logger = logging.getLogger(__name__)


class GeneralQuality(models.Model):
	_name = 'general.quality'
	_description = "General Quality model for complaints etc."
	_inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

	# MAIN NAME
	name = fields.Char('Name', readonly=True, copy=True, default='New', required=True)

	@api.model
	def create(self, vals):
		res = super(GeneralQuality, self).create(vals)
		for record in res:
			for attachment in record.images_ids:
				attachment.res_model = 'general.quality'
				attachment.res_id = record.id
				# wersja alternatywna
				# attachment.sudo().write({'res_model':'res.partner', 'res_id': record.id})
				# _logger.info("""\n\npartner.id = %s \n%s = %s""" % (record.id, attachment.res_model, attachment.res_id))
		for record in res:
			for attachment in record.reports_ids:
				attachment.res_model = 'general.quality'
				attachment.res_id = record.id
				# wersja alternatywna
				# attachment.sudo().write({'res_model':'res.partner', 'res_id': record.id})
				# _logger.info("""\n\npartner.id = %s \n%s = %s""" % (record.id, attachment.res_model, attachment.res_id))
		return res
		# WORKING CODE
		# if vals.get('images_ids'):
		# 	_logger.info("""\n %s""" % vals)
		# if vals.get('name', 'New') == 'New':
		# 	vals['name'] = self.env['ir.sequence'].next_by_code('general.quality.sequence') or 'New'
		# result = super(GeneralQuality, self).create(vals)
		# # _logger.info("""\n\n RESULT = %s""" % result)
		# for attachment in result.images_ids:
		# 	attachment.sudo().write({'res_model':'general.quality', 'res_id': result.id})
		# 	# _logger.info("""\n\n ATTACHMENT = %s""" % attachment)
		# for attachment in result.reports_ids:
		# 	attachment.sudo().write({'res_model':'general.quality', 'res_id': result.id})
		# 	# _logger.info("""\n\n ATTACHMENT = %s""" % attachment)
		# return result

	def write(self, vals):
		res = super(GeneralQuality, self).write(vals)
		for record in res:
			for attachment in record.images_ids:
				attachment.res_model = 'general.quality'
				attachment.res_id = record.id
				# wersja alternatywna
				# attachment.sudo().write({'res_model':'res.partner', 'res_id': record.id})
				# _logger.info("""\n\npartner.id = %s \n%s = %s""" % (record.id, attachment.res_model, attachment.res_id))
		for record in res:
			for attachment in record.reports_ids:
				attachment.res_model = 'general.quality'
				attachment.res_id = record.id
				# wersja alternatywna
				# attachment.sudo().write({'res_model':'res.partner', 'res_id': record.id})
				# _logger.info("""\n\npartner.id = %s \n%s = %s""" % (record.id, attachment.res_model, attachment.res_id))
		return res
		# WORKING CODE
		# res = super(GeneralQuality, self).write(vals)
		# for attachment in res.images_ids:
		# 	attachment.sudo().write({'res_model':'general.quality', 'res_id': res.id})
		# 	# _logger.info("""\n\npartner.id = %s \n%s = %s""" % (record.id, attachment.res_model, attachment.res_id))
		# for attachment in res.reports_ids:
		# 	attachment.sudo().write({'res_model':'general.quality', 'res_id': res.id})
		# 	# _logger.info("""\n\npartner.id = %s \n%s = %s""" % (record.id, attachment.res_model, attachment.res_id))
		# return res

	active = fields.Boolean(tracking=True, default=True)

	gq_status = fields.Selection([('open', 'Open'), ('closed', 'Closed')], default='open', tracking=True)

	type = fields.Selection(
		[('cr', 'Consumer Reclamations'), ('pbd', 'Product Batch Deviations'), ('pw', 'Product Withdrawals'),
		 ('ai', 'Authority inspections')], required=True)

	# 1st section
	cr_reclamation_date = fields.Date('Date of reclamation', tracking=True)
	cr_product = fields.Many2one('product.product', string="Product no and name", tracking=True)
	cr_bb_date = fields.Date('Best before date', tracking=True)
	cr_batch = fields.Char('Batch(optional)', tracking=True)
	cr_pof = fields.Char('Place of Purchace', tracking=True)
	cr_compensation = fields.Selection([('gc', 'Gift Card'), ('pr', 'Product'), ('oth', 'Other')], tracking=True,
									   default=None, string="Compensation")
	cr_consumer_name = fields.Char('Consumer name', tracking=True)
	cr_consumer_address = fields.Char('Consumer address', tracking=True)
	cr_consumer_email = fields.Char('Consumer email', tracking=True)
	cr_producer_notified = fields.Boolean('Producer notified', tracking=True)
	# 2nd section
	pbr_date = fields.Date('Date(s)', tracking=True)
	pbr_product_safety_isue = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='product safety issue',
											   tracking=True)
	pbr_other_issue = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Other issue (logistical etc.)',
									   tracking=True)
	pbr_supplier = fields.Many2many('res.partner', string="Supplier", tracking=True)
	pbr_product = fields.Many2many('product.product', 'pbr_product_id', string="Product", tracking=True)
	pbr_batch = fields.Char('Batch', tracking=True)
	pbr_problem = fields.Char('Problem', tracking=True)
	pbr_cause_investigation = fields.Char('Cause/Investigation', tracking=True)
	pbr_conclusion = fields.Char('Conclusion', tracking=True)
	pbr_corrective_actions = fields.Char('Corrective actions', tracking=True)
	pbr_signed = fields.Char('Signed', tracking=True)
	# 3rd section
	pw_date = fields.Date('Date', tracking=True)
	pw_product = fields.Many2many('product.product', 'pw_product_id', string="Product", tracking=True)
	pw_batch = fields.Char('Batch', tracking=True)
	pw_reason = fields.Char('Reason', tracking=True)
	pw_nature_of_withdrawal = fields.Selection(
		[('pb', 'Public'), ('su', 'Silent unconditional'), ('ss', 'Silent self-decided')],
		string="Nature of withdrawal", tracking=True)
	pw_chains_stores = fields.Char('Chains/Stores', tracking=True)
	pw_producer_informed = fields.Boolean('Producer informed', tracking=True)
	pw_producer_comments = fields.Char('Producer comments', tracking=True)
	pw_signed = fields.Char('Signed', tracking=True)
	# 4th section
	ai_date = fields.Date('Date', tracking=True)
	ai_product = fields.Many2many('product.product', 'ai_product_id', string="Product", tracking=True)
	ai_issue = fields.Char('Issue', tracking=True)
	ai_authority = fields.Char('Authority', tracking=True)
	ai_nature_of_inspection = fields.Selection(
		[('rm', 'Remark'), ('rj', 'Rejection'), ('er', 'Explantion requirement')], string="Nature of inspection",
		tracking=True)
	ai_notes = fields.Char('Notes', tracking=True)
	ai_corrective_actions = fields.Char('Corrective actions', tracking=True)
	ai_signed = fields.Char('Signed', tracking=True)

	images_ids = fields.Many2many('ir.attachment', 'general_quality_images', string="Images")
	reports_ids = fields.Many2many('ir.attachment', 'general_quality_reports', string="Reports")
# EoF
