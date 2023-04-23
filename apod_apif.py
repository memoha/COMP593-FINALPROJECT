'''
Library for interacting with NASA's Astronomy Picture of the Day API.
'''
import datetime
import requests



def main():
    # TODO: Add code to test the functions in this module
    apod_date = datetime.date.today()
    apod_info = get_apod_info,apod_date

    return

def get_apod_info(apod_date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (date): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """

    api_key = 'UL19gOmIY49bDSfvVx2kbe8b4gWhbo4RMJoLptB0'
    apod_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&apod_date={apod_date}&hd=True'

    response_msg = requests.get(apod_url)

    if response_msg : requests.get(apod_url)
    else:
    
     return None  

def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    if apod_info_dict == 'image':
       return 'highdefenition_url'
    elif apod_info_dict == 'video':
       return 'thumbnail_url'
    else:
       return None
    

if __name__ == '__main__':
    main()