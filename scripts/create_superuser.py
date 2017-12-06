from __future__ import absolute_import, print_function

import os
import sys
import django

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')

sys.path.append(PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sensor.settings")
django.setup()

from django.contrib.auth import get_user_model  # noqa

try:
    with open('/opt/scos/.db_superuser', 'r') as superuser_file:
        password = superuser_file.readline().rstrip()
except IOError:
    print("Not on a managed sensor, so not auto-generating admin account.")
    print("You can add an admin later with `./manage.py createsuperuser")
    sys.exit(0)

UserModel = get_user_model()

try:
    admin_user = UserModel._default_manager.get(username='admin')
except UserModel.DoesNotExist:
    UserModel._default_manager.create_superuser(
        'admin', 'sms@ntia.doc.gov', password)