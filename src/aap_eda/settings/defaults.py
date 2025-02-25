from aap_eda.settings import constants

DEBUG = False
ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS = []

# Session settings
SESSION_COOKIE_AGE = 1800
SESSION_SAVE_EVERY_REQUEST = True

# JWT token lifetime
JWT_ACCESS_TOKEN_LIFETIME_MINUTES = 60
JWT_REFRESH_TOKEN_LIFETIME_DAYS = 365

# Defines feature flags, and their conditions.
# See https://cfpb.github.io/django-flags/
FLAGS = {}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = "static/"
STATIC_ROOT = "/var/lib/eda/static"

MEDIA_ROOT = "/var/lib/eda/files"

RENAMED_USERNAME_PREFIX = "eda_"

# ---------------------------------------------------------
# DEPLOYMENT SETTINGS
# ---------------------------------------------------------
DEPLOYMENT_TYPE = "podman"
WEBSOCKET_BASE_URL = "ws://localhost:8000"
WEBSOCKET_SSL_VERIFY = "yes"
WEBSOCKET_TOKEN_BASE_URL = None
PODMAN_SOCKET_URL = None
PODMAN_SOCKET_TIMEOUT = 0
PODMAN_MEM_LIMIT = "200m"
PODMAN_ENV_VARS = {}
PODMAN_MOUNTS = []
PODMAN_EXTRA_ARGS = {}
DEFAULT_PULL_POLICY = "Always"
CONTAINER_NAME_PREFIX = "eda"

MQ_UNIX_SOCKET_PATH = None
MQ_HOST = "localhost"
MQ_PORT = 6379
MQ_USER = None
MQ_USER_PASSWORD = None
MQ_CLIENT_CACERT_PATH = None
MQ_CLIENT_CERT_PATH = None
MQ_CLIENT_KEY_PATH = None
MQ_TLS = None
MQ_DB = constants.DEFAULT_REDIS_DB
RQ_REDIS_PREFIX = "eda-rq"


# The HA cluster hosts is a string of <host>:<port>[,<host>:port>]+
# and is exhaustive; i.e., not in addition to REDIS_HOST:REDIS_PORT.
# EDA does not validate the content, but relies on DAB to do so.
#
# In establishing an HA Cluster Redis client connection DAB ignores
# the host and port kwargs.
MQ_REDIS_HA_CLUSTER_HOSTS = ""

# A list of queues to be used in multinode mode
# If the list is empty, use the default singlenode queue name
RULEBOOK_WORKER_QUEUES = []

DEFAULT_QUEUE_TIMEOUT = 300
DEFAULT_RULEBOOK_QUEUE_TIMEOUT = 120

RULEBOOK_QUEUE_NAME = "activation"

API_PREFIX = "api/eda"

APP_LOG_LEVEL = "INFO"

SCHEDULER_JOB_INTERVAL = 5

# ---------------------------------------------------------
# CONTROLLER SETTINGS
# ---------------------------------------------------------
CONTROLLER_URL = "default_controller_url"
CONTROLLER_TOKEN = "default_controller_token"
CONTROLLER_SSL_VERIFY = "yes"

# ---------------------------------------------------------
# RULEBOOK LIVENESS SETTINGS
# ---------------------------------------------------------
RULEBOOK_READINESS_TIMEOUT_SECONDS = 30
RULEBOOK_LIVENESS_CHECK_SECONDS = 300
RULEBOOK_LIVENESS_TIMEOUT_SECONDS = 310
ACTIVATION_RESTART_SECONDS_ON_COMPLETE = 0
ACTIVATION_RESTART_SECONDS_ON_FAILURE = 60
ACTIVATION_MAX_RESTARTS_ON_FAILURE = 5

# -1 means no limit
MAX_RUNNING_ACTIVATIONS = 5

# ---------------------------------------------------------
# RULEBOOK ENGINE LOG LEVEL
# ---------------------------------------------------------
ANSIBLE_RULEBOOK_LOG_LEVEL = "error"
ANSIBLE_RULEBOOK_FLUSH_AFTER = 100

# ---------------------------------------------------------
# DJANGO ANSIBLE BASE JWT SETTINGS
# ---------------------------------------------------------
ANSIBLE_BASE_JWT_VALIDATE_CERT = False
ANSIBLE_BASE_JWT_KEY = "https://localhost"

# These settings have defaults in DAB
# ALLOW_LOCAL_RESOURCE_MANAGEMENT = False
# RESOURCE_SERVICE_PATH
# RESOURCE_SERVER_SYNC_ENABLED
# ENABLE_SERVICE_BACKED_SSO

ALLOW_LOCAL_ASSIGNING_JWT_ROLES = False
ALLOW_SHARED_RESOURCE_CUSTOM_ROLES = False

# --------------------------------------------------------
# DJANGO ANSIBLE BASE RESOURCE API CLIENT
# --------------------------------------------------------

RESOURCE_SERVER__URL = "https://localhost"
RESOURCE_SERVER__SECRET_KEY = ""
RESOURCE_SERVER__VALIDATE_HTTPS = False
RESOURCE_JWT_USER_ID = None

ANSIBLE_BASE_MANAGED_ROLE_REGISTRY = {}

ACTIVATION_DB_HOST = "host.containers.internal"
PG_NOTIFY_TEMPLATE_RULEBOOK = None
SAFE_PLUGINS_FOR_PORT_FORWARD = [
    "ansible.eda.webhook",
    "ansible.eda.alertmanager",
]
API_PATH_UI_PATH_MAP = {"/api/controller": "/execution", "/": "/#"}
PG_NOTIFY_DSN_SERVER = None
EVENT_STREAM_BASE_URL = None
EVENT_STREAM_MTLS_BASE_URL = None
MAX_PG_NOTIFY_MESSAGE_SIZE = 6144
