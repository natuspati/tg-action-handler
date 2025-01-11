from actions.send_periodic_message import send_periodic_message


async def run_actions() -> None:
    await send_periodic_message()
