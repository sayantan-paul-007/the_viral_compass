import sqlite3
from pathlib import Path
import hashlib
from typing import Optional

def initialize_cache_database(db_path: Path) -> bool:
    """
    Initializes the SQLite cache database for video analysis results.
    """
    try:
        # Ensure parent directory exists
        db_path.parent.mkdir(parents=True, exist_ok=True)

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS video_analysis_cache (
            video_hash     TEXT PRIMARY KEY,
            report_content TEXT NOT NULL,
            created_at     DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        conn.commit()
        conn.close()

        print(f"✅ Cache DB initialized at: {db_path.resolve()}")
        return True

    except sqlite3.Error as e:
        print(f"❌ Error initializing cache DB: {e}")
        return False



def calculate_video_hash(video_path: Path) -> str:
    """
    Calculates a SHA-256 hash for a video file.
    """
    sha256_hash = hashlib.sha256()

    with video_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()


def check_cache(video_hash: str, db_path: Path) -> Optional[str]:
    """
    Checks if a video hash exists in the cache.
    Returns report_content if found, else None.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT report_content FROM video_analysis_cache WHERE video_hash = ?",
        (video_hash,)
    )

    row = cursor.fetchone()
    conn.close()

    return row[0] if row else None


def save_to_cache(video_hash: str, report_content: str, db_path: Path) -> None:
    """
    Saves a video analysis report to the cache.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR REPLACE INTO video_analysis_cache (video_hash, report_content) VALUES (?, ?)",
        (video_hash, report_content)
    )

    conn.commit()
    conn.close()

    print("💾 New report saved to cache.")
