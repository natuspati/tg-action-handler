import asyncio
import random
from abc import ABCMeta
from datetime import datetime, timedelta

from settings import settings


class SingletonABCMeta(ABCMeta):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


def get_current_time() -> datetime:
    return datetime.now(tz=settings.time_zone)


def get_random_time_within_range(right_now: bool = False) -> datetime:
    current_time = get_current_time()
    if right_now:
        return current_time

    start_time = current_time.replace(
        hour=settings.periodic_message_start_time,
        minute=0,
        second=0,
        microsecond=0,
    )
    end_time = current_time.replace(
        hour=settings.periodic_message_end_time,
        minute=0,
        second=0,
        microsecond=0,
    )

    random_seconds = random.randint(0, int((end_time - start_time).total_seconds()))
    return start_time + timedelta(seconds=random_seconds)


async def sleep_until(target_time) -> None:
    current_time = get_current_time()
    sleep_duration = (target_time - current_time).total_seconds()
    if sleep_duration > 0:
        await asyncio.sleep(sleep_duration)
