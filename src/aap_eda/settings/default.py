import os

from ansible_base.lib import dynamic_config
from ansible_base.lib.dynamic_config import (
    export,
    factory,
    load_envvars,
    load_standard_settings_files,
    validate,
)
from dynaconf import Validator
from split_settings.tools import include

from .post_load import post_loading, toggle_feature_flags

DYNACONF = factory(
    __name__,
    "EDA",
    # Options passed directly to dynaconf
    settings_files=["constants.py", "defaults.py", "development_defaults.py"],
)

load_standard_settings_files(
    DYNACONF
)  # /etc/ansible-automation-platform/*.yaml
load_envvars(DYNACONF)  # load envvars prefixed with EDA_
post_loading(DYNACONF)

# toggle feature flags, considering flags coming from
# /etc/ansible-automation-platform/*.yaml
# and envvars like `EDA_FEATURE_FOO_ENABLED=true
DYNACONF.update(
    toggle_feature_flags(DYNACONF),
    loader_identifier="settings:toggle_feature_flags",
    merge=True,
)
export(__name__, DYNACONF)  # export back to django.conf.settings
