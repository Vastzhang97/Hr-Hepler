import os, shutil

# 复制特定文件夹内所有文件名带关键字的文件到指定文件夹
if __name__ == '__main__':

    # 源文件夹路径
    source_file_path = '/Users/chenjiaqian/Desktop/未命名文件夹/未命名文件夹'
    # 输出文件夹路径
    target_file_path = '/Users/chenjiaqian/Desktop/未命名文件夹'
    target_dir = ['1', '2', '3', '4', '5']

    # 关键字
    key_words = ['1', '2', '3', '4', '5']

    for index, key in enumerate(key_words):

        target_dir_path = target_file_path + '/' + target_dir[index]
        # 如果输出文件夹路径不存在(百度 Python3 判断文件和文件夹是否存在、创建文件夹)
        if not os.path.exists(target_dir_path):
            # 创建文件夹(百度 Python3 创建文件夹)
            os.mkdir(target_dir_path)

        # 遍历输出文件夹路径下的所有文件(百度 Python3:遍历某个目录下的所有文件)
        for parent, dir_names, file_names in os.walk(source_file_path, followlinks=True):
            # 遍历输出文件夹路径下的所有文件名字
            for filename in file_names:
                # 每一个文件的名字
                file_path = os.path.join(parent, filename)
                # 如果文件名里有关键字
                if key_words[index] in filename:
                # if filename.startswith(key_words[index]):
                    # 复制该文件到输出文件夹
                    path = target_file_path + '/' + target_dir[index] + '/' + filename
                    shutil.copy(file_path, path)
