#This is the base code from Kaggle about audio extraction and analysis.

# def extract_and_analyze_video_frames(
#     video_path: str, 
#     max_frames: int = 20, # It will try to use all of these
# ) -> Dict[str, Any]:
#     """
#     Extracts up to 20 frames and UPLOADS ALL OF THEM to Gemini for a detailed storyboard analysis.
#     """
#     print(f"Tool 'extract_video_frames_with_validation' called for video: {video_path}")
    
#     # 1. Validation
#     if not os.path.exists(video_path):
#         return {"status": "error", "message": f"Validation Failed: File not found."}

#     # 2. Setup
#     output_dir = "/kaggle/working/frames/"
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
    
#     # Clean old frames
#     old_files = glob.glob(os.path.join(output_dir, "*.jpg"))
#     for f in old_files: os.remove(f)
   
#     vidcap = None
#     saved_paths = [] 

#     try:
#         vidcap = cv2.VideoCapture(video_path)
#         if not vidcap.isOpened():
#              return {"status": "error", "message": "Could not open video file."}

#         frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
#         frame_interval = max(1, frame_count // max_frames)
        
#         count = 0
#         for i in range(0, frame_count, int(frame_interval)):
#             if len(saved_paths) >= max_frames: break
#             vidcap.set(cv2.CAP_PROP_POS_FRAMES, i)
#             success, image = vidcap.read()
#             if success:
#                 path = os.path.join(output_dir, f"frame_{count}.jpg")
#                 cv2.imwrite(path, image)
#                 saved_paths.append(path)
#                 count += 1
#         vidcap.release()

#         # --- 3. VISION ANALYSIS (ALL FRAMES) ---
#         print(f"Uploading {len(saved_paths)} frames to Gemini (this may take a minute)...")
        
#         # USE ALL FRAMES
#         analysis_paths = saved_paths 

#         uploaded_files = []
#         for index, path in enumerate(analysis_paths):
#             print(f"Uploading frame {index+1}/{len(analysis_paths)}...")
#             myfile = genai.upload_file(path)
            
#             # Wait for processing
#             while myfile.state.name == "PROCESSING":
#                 time.sleep(1)
#                 myfile = genai.get_file(myfile.name)
            
#             uploaded_files.append(myfile)
#             # Sleep briefly to avoid hitting 'Requests Per Minute' limit on free tier
#             time.sleep(1) 
        
#         print("Analyzing storyboard...")
#         vision_model = genai.GenerativeModel("gemini-2.5-flash-lite")
        
#         # Updated Prompt for Full Storyboard
#         prompt = """
#         Analyze this sequence of 20 video frames (Storyboard).
#         1. **Visual Flow:** How does the video change visually from start to finish?
#         2. **Graphics:** Are there text overlays or graphics? Are they consistent?
#         3. **Production:** Is it a single shot or are there multiple cuts/scenes?
#         """
        
#         response = vision_model.generate_content(uploaded_files + [prompt])
#         visual_description = response.text
#         print(f"✅ Vision Analysis Generated: {visual_description[:50]}...")

#         return {
#             "status": "success",
#             "frame_paths": saved_paths,
#             "visual_description": visual_description, 
#             "message": f"Extracted and analyzed {len(saved_paths)} frames."
#         }

#     except Exception as e:
#         return {
#             "status": "success", 
#             "frame_paths": saved_paths,
#             "visual_description": "Visual analysis unavailable (Error).",
#             "message": f"Extraction worked but vision analysis failed: {str(e)}"
#         }

# print('✅ Tool 1: Video extractor and analyzer tool created')