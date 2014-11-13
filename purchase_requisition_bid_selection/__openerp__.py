# -*- coding: utf-8 -*-
#
#
#    Copyright 2013, 2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{"name": "Purchase Requisition Bid Selection",
 "version": "0.4",
 "author": "Camptocamp",
 "license": "AGPL-3",
 "category": "Purchase Management",
 "complexity": "normal",
 "images": [],
 "depends": ["purchase_requisition",
             "stock",  # For incoterms
             "purchase_rfq_bid_workflow",  # for field incoterms place
             ],
 "demo": [],
 "data": ["wizard/modal.xml",
          "wizard/purchase_requisition_partner_view.xml",
          "view/purchase_requisition.xml",
          "view/purchase_order.xml",
          "workflow/purchase_requisition.xml",
          "data/purchase.cancelreason.yml",
          ],
 "auto_install": False,
 "test": ["test/process/restricted.yml",
          ],
 "installable": True,
 "certificate": "",
 }
