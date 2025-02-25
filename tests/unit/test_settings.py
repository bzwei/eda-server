#  Copyright 2024 Red Hat, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from unittest.mock import patch
from django.test import override_settings

import pytest

from aap_eda.settings.defaults import (
    DEFAULT_QUEUE_TIMEOUT,
    DEFAULT_RULEBOOK_QUEUE_TIMEOUT,
)
from aap_eda.core.enums import RulebookProcessLogLevel
from aap_eda.settings.post_load import get_rulebook_process_log_level
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from aap_eda.settings.post_load import get_rq_queues

@pytest.mark.parametrize(
    "value,expected",
    [
        ("debug", RulebookProcessLogLevel.DEBUG),
        ("info", RulebookProcessLogLevel.INFO),
        ("error", RulebookProcessLogLevel.ERROR),
        ("-v", RulebookProcessLogLevel.INFO),
        ("-vv", RulebookProcessLogLevel.DEBUG),
    ],
)
def test_rulebook_log_level(value, expected):
    settings_override = {'ANSIBLE_RULEBOOK_LOG_LEVEL': value}

    result = get_rulebook_process_log_level(settings_override)

    assert result == expected

def test_rulebook_log_level_invalid():
    settings_override = {'ANSIBLE_RULEBOOK_LOG_LEVEL': "invalid"}
    with pytest.raises(ImproperlyConfigured):
        get_rulebook_process_log_level(settings_override)


def test_rq_queues_with_unix_socket_path():
    settings_override = {
        'REDIS_UNIX_SOCKET_PATH': 'path/to/socket',
        'RULEBOOK_WORKER_QUEUES': ['activation-node1'],
        'REDIS_DB': 'test',
        'REDIS_USER': 'test',
        'REDIS_USER_PASSWORD': 'test',
        'DEFAULT_QUEUE_TIMEOUT': 300,
        'DEFAULT_RULEBOOK_QUEUE_TIMEOUT': 120
    }
    queues = get_rq_queues(settings_override)
    assert "default" in queues
    assert queues["default"]["UNIX_SOCKET_PATH"] == "path/to/socket"
    assert queues["default"]["DEFAULT_TIMEOUT"] == DEFAULT_QUEUE_TIMEOUT
    assert "activation-node1" in queues
    assert queues["activation-node1"]["UNIX_SOCKET_PATH"] == "path/to/socket"
    assert (
        queues["activation-node1"]["DEFAULT_TIMEOUT"]
        == DEFAULT_RULEBOOK_QUEUE_TIMEOUT
    )
    assert "activation" not in queues


# def test_rq_queues_default_configuration(redis_parameters):
#     # Get the host and port from the test redis parameters in case the
#     # test is being run using an external redis.
#     # We explicitly check for None as the parameters may exist with a value of
#     # None.
#     host = redis_parameters.get("host")
#     if host is None:
#         host = "localhost"
#     port = redis_parameters.get("port")
#     if port is None:
#         port = 6379

#     queues = get_rq_queues()
#     assert queues["default"]["HOST"] == host
#     assert queues["default"]["PORT"] == port
#     assert queues["default"]["DEFAULT_TIMEOUT"] == DEFAULT_QUEUE_TIMEOUT
#     assert queues["activation"]["HOST"] == host
#     assert queues["activation"]["PORT"] == port
#     assert (
#         queues["activation"]["DEFAULT_TIMEOUT"]
#         == DEFAULT_RULEBOOK_QUEUE_TIMEOUT
#     )


# @patch("aap_eda.settings.default.REDIS_HOST", "custom-host")
# def test_rq_queues_custom_host():
#     queues = get_rq_queues()
#     assert queues["default"]["HOST"] == "custom-host"
#     assert queues["default"]["PORT"] == 6379
#     assert queues["default"]["DEFAULT_TIMEOUT"] == DEFAULT_QUEUE_TIMEOUT
#     assert queues["activation"]["HOST"] == "custom-host"
#     assert queues["activation"]["PORT"] == 6379
#     assert (
#         queues["activation"]["DEFAULT_TIMEOUT"]
#         == DEFAULT_RULEBOOK_QUEUE_TIMEOUT
#     )


# @patch(
#     "aap_eda.settings.default.RULEBOOK_WORKER_QUEUES",
#     ["activation-node1", "activation-node2"],
# )
# @patch("aap_eda.settings.default.REDIS_HOST", "custom-host")
# @patch("aap_eda.settings.default.REDIS_USER_PASSWORD", "password")
# @patch("aap_eda.settings.default.REDIS_CLIENT_CERT_PATH", "somepath")
# def test_rq_queues_custom_host_multiple_queues():
#     queues = get_rq_queues()
#     assert queues["default"]["HOST"] == "custom-host"
#     assert queues["default"]["PORT"] == 6379
#     assert queues["default"]["DEFAULT_TIMEOUT"] == DEFAULT_QUEUE_TIMEOUT
#     assert queues["activation-node1"]["HOST"] == "custom-host"
#     assert queues["activation-node1"]["PORT"] == 6379
#     assert (
#         queues["activation-node1"]["DEFAULT_TIMEOUT"]
#         == DEFAULT_RULEBOOK_QUEUE_TIMEOUT
#     )
#     assert queues["activation-node2"]["HOST"] == "custom-host"
#     assert queues["activation-node2"]["PORT"] == 6379
#     assert (
#         queues["activation-node2"]["DEFAULT_TIMEOUT"]
#         == DEFAULT_RULEBOOK_QUEUE_TIMEOUT
#     )
#     assert queues["default"]["PASSWORD"] == "password"
#     assert (
#         queues["default"]["REDIS_CLIENT_KWARGS"]["ssl_certfile"] == "somepath"
#     )
#     assert queues["activation-node1"]["PASSWORD"] == "password"
#     assert (
#         queues["activation-node1"]["REDIS_CLIENT_KWARGS"]["ssl_certfile"]
#         == "somepath"
#     )
#     assert "activation" not in queues


# @pytest.mark.parametrize(
#     "value,expected",
#     [
#         ("true", True),
#         ("True", True),
#         ("False", False),
#         ("false", False),
#         ("yes", True),
#         ("no", False),
#         ("1", True),
#         ("0", False),
#         ("", False),
#         ("anything", False),
#     ],
# )
# @patch("aap_eda.settings.default.settings")
# def test_get_boolean(mock_settings, value, expected):
#     mock_settings.get.return_value = value
#     result = _get_boolean("DEBUG")
#     assert result == expected


# @patch("aap_eda.settings.default.settings")
# def test_get_boolean_exception(mock_settings):
#     mock_settings.get.return_value = ["something", "else"]
#     with pytest.raises(ImproperlyConfigured):
#         _get_boolean("DEBUG")
