from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    """Upgrade from 1.x: regenerate the company report styles with the riyal font."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['res.company'].search([], limit=1)._update_asset_style()
