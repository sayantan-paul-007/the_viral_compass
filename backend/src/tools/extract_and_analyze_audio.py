#This is the base code from Kaggle about audio extraction and analysis.

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