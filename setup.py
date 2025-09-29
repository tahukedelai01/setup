import pyautogui as pag
import time, requests, os

import pygetwindow as gw

actions = [
    (516, 405, 4),
    (50, 100, 1),
    (249, 203, 4),
    (249, 203, 4),
    (249, 203, 4),
    (249, 203, 4),
    (447, 286, 4),
]

time.sleep(15)

img_filename = 'AvicaRemoteIDFixed.png'

def upload_image_to_gofile(img_filename):
    url = 'https://store5.gofile.io/uploadFile'
    with open(img_filename, 'rb') as img_file:
        files = {'file': img_file}
        r = requests.post(url, files=files)
        r.raise_for_status()
        j = r.json()
        if j.get('status') == 'ok':
            return j['data']['downloadPage']
    return None

def minimize_non_avica():
    for w in gw.getAllWindows():
        try:
            title = w.title.lower()
            if "avica" not in title and not w.isMinimized:
                w.minimize()
        except:
            pass

for x, y, duration in actions:
    pag.click(x, y, duration=duration)
    if (x, y) == (249, 203):
        time.sleep(3)
        pag.click(x, y, duration=duration)
    if (x, y) == (447, 286):
        os.system('"C:\\Program Files (x86)\\Avica\\Avica.exe"')
        time.sleep(15)
        pag.click(249, 203, duration=4)
        time.sleep(3)
        minimize_non_avica()
        time.sleep(10)
        pag.screenshot().save(img_filename)
        link = upload_image_to_gofile(img_filename)
        print("Uploaded:", link if link else "failed")
    time.sleep(10)

print("Done!")