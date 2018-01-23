# -*- coding: utf-8 -*-

import logging
from urlparse import urlparse
from odoo import models, api
_logger = logging.getLogger(__name__)

try:
    from odoo.addons.base_external_dbsource.models import (
        base_external_dbsource)
    CONNECTORS = base_external_dbsource.BaseExternalDbsource.CONNECTORS
    try:
        import pytds
        CONNECTORS.append(('tds', 'Microsoft SQL Server native'))
    except ImportError:
        _logger.info('Python TDS library not found please '
                     'install "python-tds" library')
except ImportError:
    _logger.info('base_external_dbsource Odoo module not found')


class BaseExternalDbsource(models.Model):
    """
    It provides logic for connection to a MSSQL data source
    """
    _inherit = 'base.external.dbsource'

    @api.multi
    def connection_close_tds(self, connection):
        return connection.close()

    @api.multi
    def connection_open_tds(self):
        url = urlparse(self.conn_string_full)
        return pytds.connect(url.hostname, url.path[1:], url.username,
                             url.password)

    @api.multi
    def execute_tds(self, sqlquery, sqlparams, metadata):
        return self._execute_generic(sqlquery, sqlparams, metadata)
