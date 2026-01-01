#This is the helper function to run the root agent and get the final report.

# async def get_final_report(runner_instance, video_path: str):
#     """
#     Orchestrates the analysis using the robust `run_debug` method.
#     The agent instructions have been updated to extract the path directly from the input.
#     """
#     print(f"\n🎬 Starting analysis for video: {video_path}")
#     start_time = time.monotonic()

#     video_hash = calculate_video_hash(video_path)
#     cached_report = check_cache(video_hash)

#     if cached_report:
#         final_report = cached_report
#         duration = time.monotonic() - start_time
#         print(f"\n✅ Report retrieved from cache in {duration:.2f} seconds.")
#     else:
#         print("\n⏳ Cache miss. Invoking the root agent runner...")
        
#         # We simply pass the video path as the user message.
#         # The agents are now smart enough to extract it themselves.
#         events = await runner_instance.run_debug(video_path)
        
#         # The final report is the content of the very last event in the list.
#         final_report_content = ""
#         if events and events[-1].content and events[-1].content.parts:
#             final_report_content = events[-1].content.parts[0].text
        
#         final_report = final_report_content
#         save_to_cache(video_hash, final_report)

#         duration = time.monotonic() - start_time
#         print(f"🚀 New report generated and saved in {duration:.2f} seconds.")

#     # --- FINAL DISPLAY ---
#     print("\n" + "="*20 + " FINAL REPORT " + "="*20)
#     if final_report:
#         display(Markdown(final_report))
#         print(f"🚀 New report generated and saved in {duration:.2f} seconds.")
#     else:
#         print("❌ Agent did not produce a final report.")

# print("✅ `get_final_report` helper function is defined correctly.")