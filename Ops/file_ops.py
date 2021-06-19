import shutil as sh
import os
import subprocess


def env(name):
    return os.environ(name)


def create_dirs(dest='.', name='New Folder'):
    path = os.path.join(dest, name)
    os.makedirs(path)


def read_file(name, path='.'):
    full_path = os.path.join(path, name)
    # STEP:1 Open file in read mode
    file = os.open(full_path, 'r')

    # STEP 2: Read file
    file_content = file.read()

    # STEP 3: Close file, MANDATORY
    file.close()

    return file_content


def write_file(content, name, path='.'):
    with open(os.path.join(path, name), "w") as f:
        f.write(content)


def rename_file(old, new):
    os.rename(old, new)


def delete_file(name, path='.'):
    full_path = os.path.join(path, name)
    os.remove(full_path)


def delete_dir(name, path='.'):
    full_path = os.path.join(path, name)
    os.rmdir(full_path)


def delete_dir_recursively(path):
    os.removedirs(path)


def list_dir(path):
    return os.listdir(path)


def copy(source_path, dest_path='.'):
    return sh.copy(source_path, dest_path)


def move(source_path, dest_path='.'):
    return sh.move(source_path, dest_path)


def run_cmd(command):
    # command should be list of strings Ex: ["ls -la"] or ["ls", "-la"]
    return subprocess.run(command)
