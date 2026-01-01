#This is the code from Kaggle environment to set up Google API key from secrets
# import os
# from kaggle_secrets import UserSecretsClient

# try:
#     GOOGLE_API_KEY = UserSecretsClient().get_secret("GOOGLE_API_KEY")
#     os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
#     print("✅ Setup and authentication complete.")
# except Exception as e:
#     print(
#         f"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}"
#     )