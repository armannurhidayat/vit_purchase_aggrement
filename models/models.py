# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)
from datetime import datetime

class PurchaseAggrement(models.Model):
	_name = 'purchase.aggrement'

	def cek_deadline(self):
		today = datetime.now()

		aggrement = self.env['purchase.requisition'].search([
			('date_end', '<=', today),
			('state', '!=', 'done')
		])
		for x in aggrement:
			x.state = 'done'