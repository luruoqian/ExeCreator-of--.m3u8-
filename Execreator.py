import os
import datetime
def test(path, save_path):
    file_names = os.listdir(path)
    if 'file_list.txt' in file_names:
        os.remove(path+'\\file_list.txt')
        file_names = os.listdir(path)
    file_names.sort(key=lambda x:int(x.split('.')[0]))
    out_file_name = 'output.mp4'
    while out_file_name in os.listdir(save_path):
        out_file_name = '新' + out_file_name
    f = open(path+'\\file_list.txt', 'w+')
    for one in file_names:
        f.write("file '" + one + "'\n")
    f.close()
    print("生成txt文件成功!")
    start = datetime.datetime.now()
    print('开始合成，初始时间为:',datetime.datetime.now())
    ffmpeg_bin_dic = "C:/Users/qian/Desktop/ffmpeg-2024-01-11-git-5e751dabc5-essentials_build/bin"
    os.system('ffmpeg -f concat -safe 0 -i '+path+'\\file_list.txt'+' -c '+ ' copy ' +save_path+'\\'+ out_file_name)
    print('合成后的当前时间为：',datetime.datetime.now())
    print('合成视频完成！用时：'+str(datetime.datetime.now()-start))
    print('合成视频完成')

