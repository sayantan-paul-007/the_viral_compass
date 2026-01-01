ai-video-consultant/
│
├── 📄 README.md                # Documentation (Architecture diagram, setup steps)
├── 📄 requirements.txt         # Dependencies (google-generativeai, opencv-python, moviepy, etc.)
├── 📄 .env                     # Secrets! (GOOGLE_API_KEY goes here, never commit this)
├── 📄 .gitignore               # Tells git to ignore .env, venv/, and data/ folders
├── 📄 main.py                  # The entry point (Run this to start the app)
│
├── 📂 src/                     # Source Code
│   ├── 📄 config.py            # Gemini Model setup, Retry configs, Logger setup
│   │
│   ├── 📂 agents/              # The "Brains" (Agent Definitions)
│   │   ├── 📄 __init__.py
│   │   ├── 📄 content_analyst.py   # Agent 3 (The Super Agent - ReAct)
│   │   ├── 📄 trend_researcher.py  # Agent 4 (Trend Researcher)
│   │   ├── 📄 creative_strategist.py # Agent 4 (Strategist)
│   │   ├── 📄 final_report.py      # Agent 5 (Formatting)
│   │   └── 📄 orchestrator.py      # Root Agent & Runner Logic (The Pipeline Circuit Breaker)
│   │
│   ├── 📂 tools/               # The "Senses" (Function Code)
│   │   ├── 📄 __init__.py
│   │   ├── 📄 video_vision.py  # extract_video_frames_with_validation (OpenCV + Gemini Vision)
│   │   └── 📄 audio_speech.py  # extract_and_analyze_audio (MoviePy + Regex JSON Fixer)
│   │
│   └── 📂 utils/               # Helpers
│       ├── 📄 __init__.py
│       └── 📄 cache_manager.py # Your SQLite Caching logic
│
├── 📂 data/                    # Temporary storage (Add to .gitignore!)
│   ├── 📂 input_videos/        # Where you drop the .mp4 files
│   ├── 📂 temp_frames/         # Where OpenCV dumps the images
│   └── 📂 temp_audio/          # Where MoviePy dumps the .wav
│
└── 📂 notebooks/               # Keep your original Kaggle work here for reference
    └── 📄 prototype.ipynb





    #2
     📂 backend/                # 🧠 THE BRAIN (FastAPI + AI Logic)
│   ├── 📄 Dockerfile
│   ├── 📄 requirements.txt    # google-generativeai, opencv-python, fastapi, moviepy, etc.
│   ├── 📄 .env                # Secrets: GOOGLE_API_KEY, SERPER_API_KEY (for trends)
│   │
│   └── 📂 app/
│       ├── 📄 main.py         # API Entry Point (Endpoints: /upload, /status, /result)
│       ├── 📄 config.py       # Central config (LLM Model names, Retry settings)
│       │
│       ├── 📂 agents/         # 🤖 THE AGENTS (Your Logic)
│       │   ├── 📄 __init__.py
│       │   ├── 📄 content_analyst.py   # Agent 1 (Super Agent: Audio + Visual)
│       │   ├── 📄 trend_researcher.py  # Agent 2 (UPDATED: Uses Search Tool for real-time trends)
│       │   ├── 📄 creative_strategist.py # Agent 3 (Synthesizes Psychology + Trends)
│       │   ├── 📄 final_report.py      # Agent 4 (Formatter)
│       │   └── 📄 pipeline.py          # Root Agent / Orchestrator Logic
│       │
│       ├── 📂 tools/          # 🛠️ THE CAPABILITIES
│       │   ├── 📄 __init__.py
│       │   ├── 📄 vision.py        # OpenCV logic (20 frames extractor)
│       │   ├── 📄 audio.py         # MoviePy logic (Audio extractor + Regex JSON fix)
│       │   └── 📄 internet.py      # ✨ NEW: Google Search Tool (for Trend/Saturation analysis)
│       │
│       ├── 📂 db/             # 💾 MEMORY
│       │   ├── 📄 cache.py         # SQLite logic (Check hash -> Return cached JSON)
│       │   └── 📄 models.py        # Pydantic models for API responses
│       │
│       └── 📂 utils/
│           └── 📄 video_utils.py   # Helper to hash video files (MD5) for caching
