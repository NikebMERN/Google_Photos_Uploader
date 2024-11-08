import requests

UPLOAD_URL = "https://photoslibrary.googleapis.com/v1/uploads"
MEDIA_ITEMS_URL = "https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate"

def upload_image_to_google_photos(image_path, creds):
    """Upload a single image to Google Photos."""
    with open(image_path, 'rb') as img:
        headers = {
            'Authorization': f'Bearer {creds.token}',
            'Content-Type': 'application/octet-stream',
            'X-Goog-Upload-Protocol': 'raw',
            'X-Goog-Upload-File-Name': image_path.split('/')[-1]
        }
        response = requests.post(UPLOAD_URL, headers=headers, data=img)
        
    # Return the upload token if successful
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to upload {image_path}: {response.status_code}")
        return None

def create_media_item(upload_token, creds):
    """Create a media item in Google Photos using the upload token."""
    headers = {
        'Authorization': f'Bearer {creds.token}',
        'Content-Type': 'application/json'
    }
    body = {
        "newMediaItems": [
            {
                "description": "Uploaded via Python script",
                "simpleMediaItem": {
                    "uploadToken": upload_token
                }
            }
        ]
    }
    response = requests.post(MEDIA_ITEMS_URL, headers=headers, json=body)
    
    if response.status_code == 200:
        print("Image successfully uploaded to Google Photos.")
    else:
        print("Failed to create media item:", response.status_code, response.text)
