from auth import authenticate
from uploader import upload_images
from utils import logger

def main():
    logger.info("Starting Google Photos Uploader")

    # Authenticate user and get credentials
    creds = authenticate()

    # Upload images from the 'images/' folder
    upload_images(creds, folder_path='images/')

    logger.info("Upload completed.")

if __name__ == '__main__':
    main()
