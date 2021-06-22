import logging

from django.core.exceptions import ObjectDoesNotExist

from main.models import MainSwitch


def get_main_switch_status():
    try:
        return MainSwitch.objects.latest("id").is_app_online
    except ObjectDoesNotExist as e:
        logging.debug(e)
        switch = MainSwitch.objects.create(is_app_online=True)
        switch.save()
        return switch.is_app_online
