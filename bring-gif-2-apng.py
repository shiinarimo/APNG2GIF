import os

# 动图文件夹
clip = 'C:/Users/Administrator/Desktop/gif'

# collecting
pics_path = clip + '/'
pics_format = ['.gif', '.GIF']
pics_name = [name for name in os.listdir(pics_path) for item in pics_format if
             os.path.splitext(name)[1] == item]
print(pics_name)
print('原图共' + str(len(pics_name)) + '张')

# 打开处理软件
os.chdir(os.getcwd())
for pic in pics_name:
    os.system('gif2apng ' + clip + '/' + pic)
