# # This is the base code from Kaggle about audio extraction and analysis.
# from moviepy import VideoFileClip
# from typing import Any, Dict
# import os
# import time
# import google.generativeai as genai
# def extract_and_analyze_audio(video_path: str) -> Dict[str, Any]:
#     """
#     Extracts audio, uploads it to Gemini, and returns the Transcript + Analysis.
#     """
#     print(f"Tool called for video: {video_path}")
    
#     # 1. Validation & Extraction (Same as your code)
#     if not os.path.exists(video_path):
#         return {"status": "error", "message": "Video file not found."}

#     output_audio_path = "/kaggle/working/temp_audio.wav"
#     try:
#         # Extract Audio
#         video_clip = VideoFileClip(video_path)
#         video_clip.audio.write_audiofile(output_audio_path, logger=None)
#         video_clip.close()
        
#         # 2. Upload to Gemini File API (The Missing Step)
#         print("Uploading audio to Gemini...")
#         audio_file = genai.upload_file(output_audio_path)
        
#         # Wait for processing
#         while audio_file.state.name == "PROCESSING":
#             time.sleep(1)
#             audio_file = genai.get_file(audio_file.name)

#         # 3. Perform Analysis INSIDE the tool
#         # We use a separate model instance here just for the tool's internal work
#         tool_model = genai.GenerativeModel("gemini-2.5-flash-lite") # Use a valid model name
        
#         prompt = """
#         Listen to this audio. Return a valid JSON object with this exact structure:
#         {
#           "transcript": "Verbatim text...",
#           "delivery_analysis": {
#             "pace": "Description...",
#             "energy": "Description...",
#             "tone": "Description..."
#           }
#         }
#         """
#         response = tool_model.generate_content([audio_file, prompt])
        
#         # Clean up the JSON string if the model adds markdown
#         result_text = response.text.strip()
#         if result_text.startswith("```json"):
#             result_text = result_text[7:-3].strip()

#         import json
#         return json.loads(result_text)

#     except Exception as e:
#         return {"status": "error", "message": str(e)}
        
# print('✅ Tool 2: Audio extractor and analyzer tool created ')
# from moviepy import VideoFileClip
# from typing import Any, Dict
# import os
# import time
# import json
# import tempfile

# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load env once
# load_dotenv()

# genai.configure(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )


# def extract_and_analyze_audio(video_path: str) -> Dict[str, Any]:
#     """
#     Extracts audio from a video, uploads it to Gemini, and returns
#     transcript + delivery analysis.
#     """

#     print(f"🎧 Audio analysis tool called for: {video_path}")

#     if not os.path.exists(video_path):
#         return {"status": "error", "message": "Video file not found"}

#     try:
#         # ---- 1. Extract audio to a temp file ----
#         with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
#             audio_path = temp_audio.name

#         video = VideoFileClip(video_path)
#         video.audio.write_audiofile(audio_path, logger=None)
#         video.close()

#         # ---- 2. Upload to Gemini File API ----
#         print("⬆️ Uploading audio to Gemini...")
#         audio_file = genai.upload_file(audio_path)

#         while audio_file.state.name == "PROCESSING":
#             time.sleep(1)
#             audio_file = genai.get_file(audio_file.name)

#         # ---- 3. Run analysis ----
#         model = genai.GenerativeModel("gemini-2.5-flash-lite")

#         prompt = """
#         Listen carefully to this audio.

#         Return a VALID JSON object ONLY in this exact structure:

#         {
#           "transcript": "Verbatim spoken text",
#           "delivery_analysis": {
#             "pace": "Description",
#             "energy": "Description",
#             "tone": "Description"
#           }
#         }
#         """

#         response = model.generate_content([audio_file, prompt])

#         text = response.text.strip()

#         # Remove markdown fences if present
#         if text.startswith("```"):
#             text = text.split("```")[1]

#         return json.loads(text)

#     except Exception as e:
#         return {
#             "status": "error",
#             "message": str(e)
#         }

#     finally:
#         # ---- Cleanup ----
#         if "audio_path" in locals() and os.path.exists(audio_path):
#             os.remove(audio_path)


# print("✅ Audio extractor & analyzer tool ready (local)")
from moviepy import VideoFileClip
from typing import Any, Dict
import os
import time
import json
import google.generativeai as genai


def extract_and_analyze_audio(video_path: str) -> Dict[str, Any]:
    """
    Extracts audio from video, stores it in backend/data/temp_audio,
    uploads to Gemini, and returns transcript + delivery analysis.
    """

    print(f"🔊 Audio tool called for video: {video_path}")

    if not os.path.exists(video_path):
        return {"status": "error", "message": "Video file not found."}

    # --------------------------------------------------
    # Resolve backend/data/temp_audio path safely
    # --------------------------------------------------
    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
    AUDIO_DIR = os.path.join(BASE_DIR, "data", "temp_audio")
    os.makedirs(AUDIO_DIR, exist_ok=True)

    audio_filename = f"{os.path.splitext(os.path.basename(video_path))[0]}.wav"
    audio_path = os.path.join(AUDIO_DIR, audio_filename)

    try:
        # --------------------------------------------------
        # Extract audio
        # --------------------------------------------------
        video_clip = VideoFileClip(video_path)
        video_clip.audio.write_audiofile(audio_path, logger=None)
        video_clip.close()

        print(f"✅ Audio saved at: {audio_path}")

        # --------------------------------------------------
        # Upload audio to Gemini
        # --------------------------------------------------
        print("☁️ Uploading audio to Gemini...")
        audio_file = genai.upload_file(audio_path)

        while audio_file.state.name == "PROCESSING":
            time.sleep(1)
            audio_file = genai.get_file(audio_file.name)

        # --------------------------------------------------
        # Analyze audio
        # --------------------------------------------------
        tool_model = genai.GenerativeModel("gemini-2.5-flash-lite")

        prompt = """
        Listen to this audio and return a VALID JSON object with EXACT structure:
        {
          "transcript": "Verbatim transcript",
          "delivery_analysis": {
            "pace": "Description",
            "energy": "Description",
            "tone": "Description"
          }
        }
        """

        response = tool_model.generate_content([audio_file, prompt])

        result_text = response.text.strip()
        if result_text.startswith("```"):
            result_text = result_text.split("```")[1]

        return json.loads(result_text)

    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        # Cleanup audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)