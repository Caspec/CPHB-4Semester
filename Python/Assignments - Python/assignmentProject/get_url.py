import webget

def download_image(arr, folder):    
    for image_path in arr:
        webget.download(image_path, './data/' + folder)
        
    
