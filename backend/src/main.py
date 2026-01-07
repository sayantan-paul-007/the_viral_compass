import asyncio
from pathlib import Path

from config import CACHE_DB_PATH
from utils.cache_setup import initialize_cache_database
from helpers import get_final_report
from agents.root_agent import build_runner


async def main():
    # 1️⃣ Initialize cache DB once
    initialize_cache_database(CACHE_DB_PATH)

    # 2️⃣ Build runner
    runner = build_runner()

    # 3️⃣ Local video path
    video_path = Path("backend/data/input_videos/Video-940.mp4")

    # 4️⃣ Run analysis
    await get_final_report(runner, str(video_path))


if __name__ == "__main__":
    asyncio.run(main())
