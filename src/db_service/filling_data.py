import asyncio
from utils.utils import init_db_by_questions, init_db_by_links


async def main():
    await init_db_by_questions()
    await init_db_by_links()


if __name__ == "__main__":
    asyncio.run(main())