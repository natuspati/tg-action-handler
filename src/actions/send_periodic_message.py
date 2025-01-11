import logging
from datetime import timedelta

from base_lib.errors import BaseError
from base_lib.utilities import (
    get_current_time,
    get_random_time_within_range,
    sleep_until,
)
from dependencies import get_tg_service
from settings import settings

_logger = logging.getLogger(__name__)


async def send_periodic_message() -> None:
    tg_service = await get_tg_service()
    while True:
        random_time = get_random_time_within_range()
        _logger.info(f"Sleeping until {random_time} to send the message")
        await sleep_until(random_time)

        _logger.info(f"Finished sleeping until {random_time}, sending the message")
        try:
            await tg_service.send_message(
                recipient=settings.periodic_message_recipient,
                message=settings.periodic_message,
            )
        except BaseError as error:
            _logger.info(f"Error occurred: {error}")
        else:
            _logger.info("Successfully sent the message")

        current_time = get_current_time()
        next_day = current_time + timedelta(days=1)
        next_day_start = next_day.replace(hour=8, minute=0, second=0, microsecond=0)
        _logger.info(f"Sleeping until {next_day_start}")
        await sleep_until(next_day_start)
