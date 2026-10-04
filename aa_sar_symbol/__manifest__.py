{
    "name": "Saudi Riyal (SAR) Currency Symbol | SAR Symbol",
    "version": "17.0.2.0.2",
    "summary": "Show the new Saudi Riyal sign in Odoo: backend, website, "
               "portal, POS and PDF reports",
    "description": """
Saudi Riyal (SAR) New Currency Symbol
=====================================
Replaces the "SR" text of the Saudi Riyal currency with the new official
Saudi Riyal sign (Unicode U+20C1) everywhere amounts are displayed.

* Uses the official Unicode code point U+20C1 (future-proof, works in exports
  and on devices that already support the new sign).
* A tiny web font (under 1 KB) is loaded only for the riyal sign thanks to
  unicode-range: all other text keeps Odoo's fonts untouched.
* Backend, website, customer portal, Point of Sale and PDF reports
  (every company layout font: Lato, Roboto, Open Sans, Tajawal, ...).
* Uninstalling restores the default "SR" symbol.
""",
    "author": "Allam Bushra",
    "maintainer": "Allam Bushra",
    "website": "https://www.linkedin.com/in/lomixyz/",
    "license": "LGPL-3",
    "category": "Tools",
    "depends": ["base", "web"],
    "data": [
        "data/res_currency_data.xml",
        "views/report_templates.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "aa_sar_symbol/static/src/scss/sar_symbol.scss",
        ],
        "web.assets_frontend": [
            "aa_sar_symbol/static/src/scss/sar_symbol.scss",
        ],
        "web.report_assets_common": [
            "aa_sar_symbol/static/src/scss/sar_symbol.scss",
            "aa_sar_symbol/static/src/scss/sar_symbol_report.scss",
        ],
        "point_of_sale._assets_pos": [
            "aa_sar_symbol/static/src/scss/sar_symbol.scss",
        ],
    },
    "images": ["static/description/banner.png"],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    "installable": True,
    "application": True,
}
