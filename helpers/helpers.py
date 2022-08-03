import os


def number_of_files(path="./data/articles/"):
    count = 0
    dir_path = path
    for path in os.scandir(dir_path):
        if path.is_file():
            count += 1 
    print(count)
    return count


if __name__=='__main__':
    number_of_files()