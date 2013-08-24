#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mayan.settings")

    sys.path.append(os.path.realpath('mayan/3rd_party_apps'))
    sys.path.append(os.path.realpath('mayan/apps'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
