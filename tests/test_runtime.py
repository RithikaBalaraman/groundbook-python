"""Rows checked here: every request and event reaches the log with public ids and no line carries the club,
settings really do come from an env-file, data survives a restart, the image leaves out everything but the app, and
the README walks one booking from the request to the gate. The container runs themselves (rm + run on the same
volume, an edited env-file, docker logs, docker diff) are run by hand with docker."""
import logging
import re
from datetime import timedelta
from pathlib import Path

from fastapi.testclient import TestClient
from sqlalchemy import func, select

from groundbook.app import create_app
from groundbook.clock import get_clock
from groundbook.models import Ground
from groundbook.settings import Settings
from tests.conftest import (
    ROOT,
    T0,
    V,
    booking,
    confirm,
    iso,
    make_settings,
    request,
    requested,
)