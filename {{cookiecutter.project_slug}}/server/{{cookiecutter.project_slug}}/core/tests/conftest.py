import pytest  # noqa

# Make fixtures available to all tests in this directory
from .fixtures import *  # noqa
from {{ cookiecutter.project_name }}.common.tests.fixtures import *  # noqa
