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

from .post_load import post_loading

EDA_SETTINGS_FILE = "/etc/eda/settings.yaml"

DYNACONF = factory(
    __name__,
    "EDA",
    # Options passed directly to dynaconf
    environments=("production", "development", "testing"),
    settings_files=["defaults.py"],
)

load_standard_settings_files(
    DYNACONF
)  # /etc/ansible-automation-platform/*.yaml
DYNACONF.load_file(EDA_SETTINGS_FILE)
load_envvars(DYNACONF)  # load envvars prefixed with EDA_
DYNACONF.load_file("constants.py")  # load internal non-overwritable settings
post_loading(DYNACONF)
export(__name__, DYNACONF)  # export back to django.conf.settings

dab_settings = os.path.join(
    os.path.dirname(dynamic_config.__file__), "dynamic_settings.py"
)
include(dab_settings)
