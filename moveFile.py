import os, shutil

if __name__ == '__main__':

    # 源文件夹路径
    source_file_path = 'C:/Users/62526/Desktop/Test'
    # 输出文件夹路径
    target_file_path = 'C:/Users/62526/Desktop/Test1'
    # 关键字
    key_word = "test"

    # 如果输出文件夹路径不存在
    if not os.path.exists(target_file_path):
        # 创建文件夹
        os.mkdir(target_file_path)

    # 遍历输出文件夹路径下的所有文件
    for parent, dir_names, file_names in os.walk(source_file_path, followlinks=True):
        # 遍历输出文件夹路径下的所有文件名字
        for filename in file_names:
            # 每一个文件的名字
            file_path = os.path.join(parent, filename)
            # 如果文件名里有关键字
            if key_word in filename:
                # 复制该文件到输出文件夹
                path = shutil.copy(file_path, target_file_path + "/"+filename)
