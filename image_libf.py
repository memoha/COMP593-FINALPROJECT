'''
Library of useful functions for working with images.
'''

from http import HTTPStatus
import os
import sys
import requests
import sqlite3
import ctypes
import hashlib



image_cache_directory = 'image_cache/'
img_cache_db = os.path.join(image_cache_directory, 'img_cache.db')

def main():
    # TODO: Add code to test the functions in this module
    image_url = 'https://apod.nasa.gov/apod/image/2304/AuroraSnow_Casado_3000.jpg'

    image_data = download_image('https://apod.nasa.gov/apod/image/2304/AuroraSnow_Casado_3000.jpg')
    
    apod_date = '2022-12-25'
    print(f'img cache dir: {image_cache_directory}')
    print(f'img cache db: {img_cache_db}')
    
    apod_info = get_apod_info(apod_date)
    if not apod_info:
        print("Failed to get APOD info from NASA.")
        return

    apod_title = apod_info['AuroraSnow']
    apod_url = apod_info['https://apod.nasa.gov/apod/image/2304/AuroraSnow_Casado_3000.jpg']
    print(f"APOD title: {apod_title}")
    print(f"APOD URL: {apod_url}")
    image_path = os.path.join(image_cache_directory, f"{apod_title}.jpg")
    image_sha256 = download_image(apod_url, image_path)
    if not image_sha256:
        print("Failed to download APOD image.")
        return
    print(f"APOD SHA-256: {image_sha256}")
    set_desktop_background_image(image_path)
    print(f"Setting desktop to {image_path}...success")

def download_image(image_url):
    """Downloads an image from a specified URL.

    DOES NOT SAVE THE IMAGE FILE TO DISK.

    Args:
        image_url (str): https://apod.nasa.gov/apod/image/2304/AuroraSnow_Casado_3000.jpg

    Returns:
        bytes: Binary image data, if succcessful. None, if unsuccessful.
    """
    # TODO: Complete function body

    apod_url = 'https://apod.nasa.gov/apod/image/2304/AuroraSnow_Casado_3000.jpg'
    print(f'Downloading image from {apod_url}...', end='')
    resp_msg = requests.get(image_url)

    # Check if the image was retrieved successfully
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        return resp_msg.content
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
    return

def save_image_file(image_data, image_path):
    """Saves image data as a file on disk.
    
    DOES NOT DOWNLOAD THE IMAGE.

    Args:
        image_data (bytes): Binary image data
        image_path (str): Path to save image file

    Returns:
        bytes: True, if succcessful. False, if unsuccessful
    """
    # TODO: Complete function body
    return

def set_desktop_background_image(image_path):
    """Sets the desktop background image to a specific image.

    Args:
        image_path (str): Path of image file

    Returns:
        bytes: True, if succcessful. False, if unsuccessful        
    """
    # TODO: Complete function body

    print(f"Setting desktop to {image_path}...", end='')
    SPI_SETDESKWALLPAPER = 20
    try:
        if ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3):
            print("success")
            return True
        else:
            print("failure")
    except:
        print("failure")
    return False

def scale_image(image_size, max_size=(800, 600)):
    return

def scale_image(image_size, max_size=(800, 600)):
    """Calculates the dimensions of an image scaled to a maximum width
    and/or height while maintaining the aspect ratio  

    Args:
        image_size (tuple[int, int]): Original image size in pixels (width, height) 
        max_size (tuple[int, int], optional): Maximum image size in pixels (width, height). Defaults to (800, 600).

    Returns:
        tuple[int, int]: Scaled image size in pixels (width, height)
    """
    ## DO NOT CHANGE THIS FUNCTION ##
    # NOTE: This function is only needed to support the APOD viewer GUI
    resize_ratio = min(max_size[0] / image_size[0], max_size[1] / image_size[1])
    new_size = (int(image_size[0] * resize_ratio), int(image_size[1] * resize_ratio))
    return new_size

if __name__ == '__main__':
    main()