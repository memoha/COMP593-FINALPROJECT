""" 
COMP 593 - Final Project

Description: 
  Downloads NASA's Astronomy Picture of the Day (APOD) from a specified date
  and sets it as the desktop background image.

Usage:
  python apod_desktop.py [apod_date]

Parameters:
  apod_date = APOD date (format: YYYY-MM-DD)
"""
from sys import argv 
from datetime import date
import os
import image_lib
import requests
import inspect
import sqlite3


# Global variables
image_cache_dir = None  # Full path of image cache directory
image_cache_db = None   # Full path of image cache database

def main():
    ## DO NOT CHANGE THIS FUNCTION ##
    # Get the APOD date from the command line
    apod_date = get_apod_date()    

    # Get the path of the directory in which this script resides
    script_dir = get_script_dir()

    # Initialize the image cache
    init_apod_cache(script_dir)

    # Add the APOD for the specified date to the cache
    apod_id = add_apod_to_cache(apod_date)

    # Get the information for the APOD from the DB
    apod_info = get_apod_info(apod_id)

    # Set the APOD as the desktop background image
    if apod_id != 0:
        image_lib.set_desktop_background_image(apod_info['file_path'])

def get_apod_date():
    """Gets the APOD date
     
    The APOD date is taken from the first command line parameter.
    Validates that the command line parameter specifies a valid APOD date.
    Prints an error message and exits script if the date is invalid.
    Uses today's date if no date is provided on the command line.

    Returns:
        date: APOD date
    """
    # TODO: Complete function body


    if len(argv) > 1:
           apod_date = date.fromisoformat('2022-12-25')
    else:
        apod_date = date.today()


    try:
        validdate = date.fromisoformat(apod_date)
        if validdate < date(1995, 06, 16):
             print ('Error: Invalid date, Should be after 1995-06-16.')
        elif validdate > date.today():
            print ('Error: Invalid date, Should not be a future date.') 

    except:
            exit('script execution is cancelled')
    return apod_date

api_key = 'UL19gOmIY49bDSfvVx2kbe8b4gWhbo4RMJoLptB0'
apod_date = '2022-12-25'
apod_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&apod_date={apod_date}&hd=True'

get_params = {'api_key' :'UL19gOmIY49bDSfvVx2kbe8b4gWhbo4RMJoLptB0',
            'apod_date'
              : '2022-12-25'}


response_msg = requests.get(url)
if response_msg.status_code == 200:
    print('Getting 2022-12-25 APOD information from NASA.....Success')

else:
    print('Getting 2022-12-25 APOD information from NASA.....Failed')

data = response_msg.json()





def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    ## DO NOT CHANGE THIS FUNCTION ##
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

def init_apod_cache(parent_dir):
    """Initializes the image cache by:
    - Determining the paths of the image cache directory and database,
    - Creating the image cache directory if it does not already exist,
    - Creating the image cache database if it does not already exist.
    
    The image cache directory is a subdirectory of the specified parent directory.
    The image cache database is a sqlite database located in the image cache directory.

    Args:
        parent_dir (str): Full path of parent directory    
    """
    global image_cache_dir
    global image_cache_db
    # TODO: Determine the path of the image cache directory

    image_cache_dir = os.path.join(os.path.expanduser, 'image_cache')
    print('img cache dir:', image_cache_dir)
    # TODO: Create the image cache directory if it does not already exist
    os.makedirs(image_cache_dir)
    # TODO: Determine the path of image cache DB
    image_cache_db = os.path.join(image_cache_dir, image_cache_db)
    # TODO: Create the DB if it does not already exist
    con = sqlite3.connect(image_cache_db)
    con.close


    print('img cache dir:', image_cache_dir)
    print('img cache db:', image_cache_db)


def add_apod_to_cache(apod_date):
    """Adds the APOD image from a specified date to the image cache.
     
    The APOD information and image file is downloaded from the NASA API.
    If the APOD is not already in the DB, the image file is saved to the 
    image cache and the APOD information is added to the image cache DB.

    Args:
        apod_date (date): Date of the APOD image

    Returns:
        int: Record ID of the APOD in the image cache DB, if a new APOD is added to the
        cache successfully or if the APOD already exists in the cache. Zero, if unsuccessful.
    """
    print("APOD date:", apod_date.isoformat())
    # TODO: Download the APOD information from the NASA API
    apod_url = f'https://api.nasa.gov/planetary/apod?date={apod_date}&api_key=UL19gOmIY49bDSfvVx2kbe8b4gWhbo4RMJoLptB0'
    response_msg = requests.get(url)


    # TODO: Download the APOD image
    apod_url = get_apod_info(url)
    response_img = requests.get(apod_url)
    # TODO: Check whether the APOD already exists in the image cache
    if os.path.__file__(f'{image_cache_dir}{apod_date}'):
        print('APOD img is already existing in cache.')
    # TODO: Save the APOD file to the image cache directory
    # TODO: Add the APOD information to the DB
    cursor = con.cursor()
    cursor.exeute()


    return 0

def add_apod_to_db(title, explanation, file_path, sha256):
    """Adds specified APOD information to the image cache DB.
     
    Args:
        title (str): Title of the APOD image
        explanation (str): Explanation of the APOD image
        file_path (str): Full path of the APOD image file
        sha256 (str): SHA-256 hash value of APOD image

    Returns:
        int: The ID of the newly inserted APOD record, if successful.  Zero, if unsuccessful       
    """
    # TODO: Complete function body

    con = sqlite3.connect(image_cache_db)
    cur = con.cursor
    cur.execute("INSERT INTO apod_cache(title, explanation, file_path, sha256) VALUES (?, ?, ?, ?)",
                    (title, explanation, file_path, sha256))
    if id == cur.new_id:
        con.commit
        con.close
        return id
    else:
        print('Failed to give APOD record into the database')

    return 0

def get_apod_id_from_db(image_sha256):
    """Gets the record ID of the APOD in the cache having a specified SHA-256 hash value
    
    This function can be used to determine whether a specific image exists in the cache.

    Args:
        image_sha256 (str): SHA-256 hash value of APOD image

    Returns:
        int: Record ID of the APOD in the image cache DB, if it exists. Zero, if it does not.
    """
    # TODO: Complete function body
    con = sqlite3.connect(image_cache_db)
    cur = con.cursor()
    cur.execute('SELECT ID FROM image_cache_db WHERE SHA256 = image_sha256')

    return 0

def determine_apod_file_path(image_title, image_url):
    """Determines the path at which a newly downloaded APOD image must be 
    saved in the image cache. 
    
    The image file name is constructed as follows:
    - The file extension is taken from the image URL
    - The file name is taken from the image title, where:
        - Leading and trailing spaces are removed
        - Inner spaces are replaced with underscores
        - Characters other than letters, numbers, and underscores are removed

    For example, suppose:
    - The image cache directory path is 'C:\\temp\\APOD'
    - The image URL is 'https://apod.nasa.gov/apod/image/2205/NGC3521LRGBHaAPOD-20.jpg'
    - The image title is ' NGC #3521: Galaxy in a Bubble '

    The image path will be 'C:\\temp\\APOD\\NGC_3521_Galaxy_in_a_Bubble.jpg'

    Args:
        image_title (str): APOD title
        image_url (str): APOD image URL
    
    Returns:
        str: Full path at which the APOD image file must be saved in the image cache directory
    """
    # TODO: Complete function body

    image_title = 'NGC 1333: Stellar Nursery in Perseus'
    image_url = 'https://apod.nasa.gov/apod/image/2304/AuroraSnow_Casado_3000.jpg'
    image_cache_dir = '/path/to/image/cache'
    image_path = determine_apod_file_path(image_title, image_url, image_cache_dir)

    print (image_lib)

    return image_path

def get_apod_info(image_id):
    """Gets the title, explanation, and full path of the APOD having a specified
    ID from the DB.

    Args:
        image_id (int): ID of APOD in the DB

    Returns:
        dict: Dictionary of APOD information
    """
    # TODO: Query DB for image info
    con = sqlite3.connect(image_cache_db)
    cur = con.cursor

    cur.execute(image_id)
    cur.close


    # TODO: Put information into a dictionary
    apod_info = {
        #'title': , 
        #'explanation': ,
        'file_path': 'TBD',
    }
    return apod_info

def get_all_apod_titles():
    """Gets a list of the titles of all APODs in the image cache

    Returns:
        list: Titles of all images in the cache
    """
    # TODO: Complete function body
    title = get_all_apod_titles

    # NOTE: This function is only needed to support the APOD viewer GUI
    return title

if __name__ == '__main__':
    main()