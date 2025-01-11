import asyncio
import logging

from actions import run_actions

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


async def main() -> None:
    await run_actions()


if __name__ == "__main__":
    asyncio.run(main())
