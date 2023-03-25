#!/usr/bin/env python3

import sys
import os
import django
from django.conf import settings
from django.test.utils import get_runner


APP_NAME = "gamerauntsia"

os.environ["DJANGO_SETTINGS_MODULE"] = "gamerauntsia.settings"

if hasattr(django, "setup"):
    django.setup()

TestRunner = get_runner(settings)
test_runner = TestRunner()
failures = test_runner.run_tests([APP_NAME])
if failures:
    sys.exit(failures)
