import doctest
from insights.parsers import cloud_cfg
from insights.tests import context_wrap


CONFIG = """
{"config": "disabled"}
"""


def test_cloud_cfg():
    result = cloud_cfg.CloudCfg(context_wrap(CONFIG))
    assert result.data['config'] == 'disabled'


def test_doc_examples():
    env = {
        'cloud_cfg': cloud_cfg.CloudCfg(context_wrap(CONFIG)),
    }
    failed, total = doctest.testmod(cloud_cfg, globs=env)
    assert failed == 0
