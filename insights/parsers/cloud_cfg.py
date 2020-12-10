"""
CloudCfg - file ``/etc/cloud/cloud.cfg``
========================================

This module provides parsing for cloudinit configuration file.
``CloudCfg`` is a parser for ``/etc/cloud/cloud.cfg`` file.

Typical output from the datasource is::

    network:
      config: disabled
    debug:
      output: /var/log/cloud-init-debug.log
      verbose: true

Examples:
    >>> cloud_cfg.data['config']
    'disabled'
"""
import json
from insights import CommandParser, parser
from insights.specs import Specs


@parser(Specs.cloud_init_network_config)
class CloudCfg(CommandParser):
    """ Class for parsing the content of ``/etc/cloud/cloud.cfg``."""
    def parse_content(self, content):
        if not content:
            raise SkipException('No Content')
        self.data = json.loads(''.join(content))
