#coding=utf-8
import time,os,json
from tqdm import tqdm
import requests
import base64

""""

使用建议，软件每次生成图片后，都复制图片到一个文件夹中
这个文件夹中的图片会被上传到图床
上传好之后，直接删除掉本地文件夹的下的图片文件
（如果是一次转换多张图片的情况，那就是遍历图片文件后上传，上传后删除掉所有图像文件,以免影响下一次上传）
"""
def tobase64(filename):
        with open(filename, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string

def upload_img(img_data_path):
    APIKey = "b6d9d156294ed66ef91fbbfdb44fd841"
    img2base64 = tobase64(img_data_path)
    data = {
            "source":img2base64,
            "action":"upload",
            "key":APIKey
            }
    url = "http://jellyfin.orangetien.icu:1500/userapi/1/upload"
    result_json = requests.post(url, data = data).content
    try:
        result_dict = json.loads(result_json.decode())
    except Exception as _:
        print('the result of the picture bed is not standard json.' )
    pic_url = result_dict.get('image',{}).get('url','')
    print('pic_url',pic_url)


def get_image_path_list(img_path):
    file_name = []
    for root,path,files in os.walk(img_path):
        files.sort()
        for file in files:
            file_name.append(os.path.join(root,file))
    return file_name

def upload_to_chevereto(img_path):
    file_name_list = get_image_path_list(img_path)
    for img_index in tqdm(range(len(file_name_list))):
        print('\nimage_file:',file_name_list[img_index])
        upload_img(file_name_list[img_index])


if __name__ == "__main__":

    img_path = "C:\\Users\\AlgerTien\\Desktop\\img"
    upload_to_chevereto(img_path)
