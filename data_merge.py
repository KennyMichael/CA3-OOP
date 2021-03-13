data = [{'section': '1', 'summary': '<p>https://github.com/KennyMichael/CA3-OOP/blob/main/wk1/index.html</p><p>https://github.com/KennyMichael/CA3-OOP/blob/main/wk1/wk1.pdf</p>'}, {'section': '2', 'summary': '<p>https://github.com/KennyMichael/CA3-OOP/blob/main/wk2/index.html</p><p>https://github.com/KennyMichael/CA3-OOP/blob/main/wk2/wk2.pdf</p>'},
        {'section': '3', 'summary': '<p>https://github.com/KennyMichael/CA3-OOP/blob/main/wk3/index.html</p><p>https://github.com/KennyMichael/CA3-OOP/blob/main/wk3/wk3.pdf</p>'}, {'section': '4', 'summary': '<p>https://github.com/KennyMichael/CA3-OOP/blob/main/wk4/index.html</p><p>https://github.com/KennyMichael/CA3-OOP/blob/main/wk4/wk4.pdf</p>'}]


video_data = [{'section': 1, 'summary': '<p></p><p>https://drive.google.com/file/d/1vyPoSlUc5hcXajllDyaqMKvlJOiYxbNH/view?usp=sharing</p>'}, {'section': 2, 'summary': '<p></p><p>https://drive.google.com/file/d/1elgdm2482AMcARz_NUVTjg8KBPmoLTxj/view?usp=sharing</p>'}, {'section': 3, 'summary': '<p></p><p>https://drive.google.com/file/d/1_RgK_fcatlpGOSDn6yokgOEZAFxKmTlc/view?usp=sharing</p>'}, {'section': 4, 'summary': '<p></p><p>https://drive.google.com/file/d/1AFfRgg3y_ebWYsmJmANSQYFgOeDnVnwJ/view?usp=sharing</p>'}, {'section': 5, 'summary': '<p></p><p>https://drive.google.com/file/d/1Gx_QXD9kQFJNi9_oOlQN4Sa9Irz0ki2K/view?usp=sharing</p>'}, {'section': 6, 'summary': '<p></p><p>https://drive.google.com/file/d/1nx7eMPpso7oXgU-KViMQZb48qUZahLru/view?usp=sharing</p>'}, {'section': 8, 'summary': '<p></p><p>https://drive.google.com/file/d/1rQM7k4oCRTxnAb8gzIGVCgTv1gVuT3Wq/view?usp=sharing</p>'}, {'section': 9, 'summary': '<p></p><p>https://drive.google.com/file/d/13lW7t_bpHCpRV9LuoXCXInUWnqbQ6ZGj/view?usp=sharing</p>'}, {'section': 10, 'summary': '<p></p><p>https://drive.google.com/file/d/1bndcQ1ZMj9KxxSkXEUYvZBsXo3nDIl4b/view?usp=sharing</p>'},
              {'section': 11, 'summary': '<p></p><p>https://drive.google.com/file/d/1_GYn_eb9WVSA-VU4hH-87XAuCKIXD22x/view?usp=sharing</p>'}, {'section': 16, 'summary': '<p></p><p>https://drive.google.com/file/d/16zl5c8bZOasi7kXcQEZxKQ408iUOMJr_/view?usp=sharing</p>'}, {'section': 17, 'summary': '<p></p><p>https://drive.google.com/file/d/14pVDe0l1SYcpQxqsfW32modTbxhMEIcJ/view?usp=sharing</p>'}, {'section': 18, 'summary': '<p></p><p>https://drive.google.com/file/d/1mdRLlLsT3UWYfNR_df-I2zTqfbhePcn8/view?usp=sharing</p>'}, {'section': 19, 'summary': '<p></p><p>https://drive.google.com/file/d/1l6jDCVocVeD8ap3gpi-dlrkTIGGotLOj/view?usp=sharing</p>'}, {'section': 20, 'summary': '<p></p><p>https://drive.google.com/file/d/1ZEGGqefwz_sw88YP9aXSQRaK-ghcY9VP/view?usp=sharing</p>'}, {'section': 21, 'summary': '<p></p><p>https://drive.google.com/file/d/1wg0gkGZp19JJdTa8Zim3L1_jCH4vawa1/view?usp=sharing</p>'}, {'section': 22, 'summary': '<p></p><p>https://drive.google.com/file/d/14uB6duBXl17ksMX_RFZaUB5NBMoPWZzT/view?usp=sharing</p>'}, {'section': 23, 'summary': '<p></p><p>https://drive.google.com/file/d/14Y0AW9ZqlUgxl4hD-iIicJZRkcmG9Ccc/view?usp=sharing</p>'}]


def data_merge(data, video_data):
    tick = 0
    for i in data:
        video_data[tick]['summary'] = video_data[tick]['summary'] + \
            ((i['summary']))
        tick += 1

    return video_data


print(video_data[2]['summary'])

# print(ls)
# vids = []

# for i in video_data:
#     if i['section'] in ls:
#         vids.append(i['summary'])

# for i in ls:
#     int(i['section']

# for i in ls1:
#     print(ls2[i])
# for i in video_data:
#     print(i['summary'])
