import requests
import os

def downlaod_image(url, save_root=".", verbose=False):
    """
    downlaod image from url


    # Parameters 

    - url
    - save_root
    - verbose: print the name of the downloaed image

    """
    response = requests.get(url)
    img_name = os.path.basename(url)
    save_path = os.path.join(save_root, img_name)
    f = open(save_path, 'wb')
    f.write(response.content)
    print("downloaded {}".format(img_name))
    
