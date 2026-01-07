#This is the helper function to run the root agent and get the final report.
import time
from pathlib import Path
from IPython.display import display, Markdown
from config import CACHE_DB_PATH
from utils.cache_setup import (
    calculate_video_hash,
    check_cache,
    save_to_cache,
)


async def get_final_report(runner_instance, video_path: str):
    """
    Runs the root agent and returns the final report.
    Uses SQLite cache to avoid reprocessing the same video.
    """
    video_path = Path(video_path)

    print(f"\n🎬 Starting analysis for video: {video_path}")
    start_time = time.monotonic()

    # ---- Cache lookup ----
    video_hash = calculate_video_hash(video_path)
    cached_report = check_cache(video_hash, CACHE_DB_PATH)

    if cached_report:
        final_report = cached_report
        duration = time.monotonic() - start_time
        print(f"\n⚡ Cache hit. Report retrieved in {duration:.2f} seconds.")

    else:
        print("\n⏳ Cache miss. Invoking the root agent runner...")

        # Pass the path as a string to the agent runner
        events = await runner_instance.run_debug(str(video_path))

        final_report = ""
        if events and events[-1].content and events[-1].content.parts:
            final_report = events[-1].content.parts[0].text

        if final_report:
            save_to_cache(video_hash, final_report, CACHE_DB_PATH)

        duration = time.monotonic() - start_time
        print(f"🚀 New report generated and cached in {duration:.2f} seconds.")

    # ---- Final display ----
    print("\n" + "=" * 20 + " FINAL REPORT " + "=" * 20)
    if final_report:
        display(Markdown(final_report))
    else:
        print("❌ Agent did not produce a final report.")
