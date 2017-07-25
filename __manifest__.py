# -*- coding: utf-8 -*-

{
    "name": "付款审批",
    "summary": "会签模块",
    "author": "Latlng",
    "sequence": "0",
    "version": "1.0",
    "depends": ["hr", "report"],
    "data": [
        "security/countersign_security.xml",
        "security/ir.model.access.csv",
        "views/leader_countersign_view.xml",
        "views/menuitem_view.xml",
        "report/countersign_report.xml",
        "report/countersign_report_template.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
