# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FranchiseeMaster(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address_line_1: DF.SmallText | None
		address_line_2: DF.SmallText | None
		area_code: DF.Data | None
		city: DF.Data | None
		country: DF.Link | None
		date_of_joining: DF.Date | None
		email_id: DF.Data | None
		employment_type: DF.Link | None
		full_name: DF.Data | None
		phone_no: DF.Phone | None
		role: DF.Link | None
		state: DF.Data | None
		status: DF.Literal["Active", "Inactive"]
	# end: auto-generated types

	pass
