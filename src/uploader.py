import os
from google_photos_api import upload_image_to_google_photos, create_media_item

def upload_images(creds, folder_path='images/'):
    """Upload all images from a specified folder."""
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' not found.")
        return

    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(('jpg', 'jpeg', 'png')):
            print(f"Uploading {file_name}...")
            
            # Step 1: Upload image and get the token
            upload_token = upload_image_to_google_photos(file_path, creds)
            
            # Step 2: Create a media item in Google Photos
            if upload_token:
                create_media_item(upload_token, creds)
        else:
            print(f"Skipping non-image file: {file_name}")
