import logging
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from loguru import logger

from main.models import MainSwitch, DishDateLink, Transaction


def get_main_switch_status():
    """Singleton for main setting."""
    try:
        return MainSwitch.objects.latest("id").is_app_online
    except ObjectDoesNotExist as e:
        logging.debug(e)
        switch = MainSwitch.objects.create(is_app_online=True)
        switch.save()
        return switch.is_app_online


def delete_orders_logic(date):
    formatting = "%Y-%m-%d"
    date_obj = datetime.strptime(date, formatting)
    transactions = Transaction.objects.filter(dish_date_link__date__gte=date_obj)
    for item in transactions:
        # Explicit fire delete() method for every object to deduct balance cash
        item.delete()
    DishDateLink.objects.filter(date__gte=date_obj).delete()
    logger.debug(f"All dish links deleted from {date}")
