def post_init_hook(env):
    """Invalidate the cached report style assets so the riyal font is used in PDFs
    right away, instead of waiting for a company font/color field to change."""
    env.transaction.invalidate_ormcache('assets')


def uninstall_hook(env):
    """Restore Odoo's default SAR symbol: the riyal font is removed with the module."""
    sar = env.ref('base.SAR', raise_if_not_found=False)
    if sar:
        sar.write({'symbol': 'SR', 'position': 'after'})
