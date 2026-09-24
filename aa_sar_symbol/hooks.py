def post_init_hook(env):
    """Regenerate the company report styles so the riyal font is used in PDFs."""
    env['res.company'].search([], limit=1)._update_asset_style()


def uninstall_hook(env):
    """Restore Odoo's default SAR symbol: the riyal font is removed with the module."""
    sar = env.ref('base.SAR', raise_if_not_found=False)
    if sar:
        sar.write({'symbol': 'SR', 'position': 'after'})
