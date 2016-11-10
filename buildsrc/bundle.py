
import sys
import os
import filecmp
import shutil
import zipfile

ARCH = sys.version.lower().find(' 64 bit ') > 0 and 'x64' or 'x86'


def get_zip_contents(zipfile):
    ret = {}
    for info in zipfile.infolist():
        ret[info.filename] = info
    return ret


def cmp_zips(zip_name1, zip_name2):
    zip_file1 = zipfile.ZipFile(zip_name1)
    zip_file2 = zipfile.ZipFile(zip_name2)
    zip_contents1 = get_zip_contents(zip_file1)
    zip_contents2 = get_zip_contents(zip_file2)
    for name, info1 in zip_contents1.items():
        if name not in zip_contents2:
            print("{0} contains {2} which is not in {1}".format(zip_name1, zip_name2, name))
            return False
        if info1.file_size != zip_contents2[name].file_size:
            print("{0} contains {2} with {3} bytes, which is {4} bytes in {1}".format(
                zip_name1, zip_name2, name, info1.file_size, zip_contents2[name].file_size
            ))
            return False
        if info1.CRC != zip_contents2[name].CRC:
            print("{0} contains {2} with CRC {3}, which is {4} in {1}".format(
                zip_name1, zip_name2, name, info1.CRC, zip_contents2[name].CRC
            ))
            return False
        del zip_contents2[name]
    if len(zip_contents2) > 0:
        print("{1} contains files {3}, which are not in {0}".format(
            zip_name1, zip_name2, zip_contents2.keys()
        ))
    return True


def copy_into(base_src_dir, base_out_dir, sub_path):
    src_dir = os.path.join(base_src_dir, sub_path)
    dest_dir = os.path.join(base_out_dir, sub_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for name in os.listdir(src_dir):
        src_file = os.path.join(src_dir, name)
        if os.path.isdir(src_file):
            copy_into(base_src_dir, base_out_dir, os.path.join(sub_path, name))
        elif os.path.isfile(src_file):
            dest_file = os.path.join(dest_dir, name)
            if os.path.exists(dest_file) and os.path.isfile(dest_file):
                if src_file.endswith('.zip'):
                    if not cmp_zips(src_file, dest_file):
                        raise Exception(
                            "source file `{0}` is different than existing destination file `{1}`".format(
                                src_file, dest_file)
                        )
                elif not filecmp.cmp(src_file, dest_file, shallow=False):
                    raise Exception(
                        "source file `{0}` is different than existing destination file `{1}`".format(
                            src_file, dest_file)
                    )
            elif os.path.exists(dest_file):
                raise Exception(
                    "source file `{0}`, but existing destination is not file: {1}".format(src_file, dest_file)
                )
            else:
                shutil.copyfile(src_file, dest_file)


if __name__ == '__main__':
    __dist_dir = sys.argv[1]
    __out_dir = os.path.join(__dist_dir, ARCH)
    os.makedirs(__out_dir)
    for __name in os.listdir(__dist_dir):
        __full_name = os.path.join(__dist_dir, __name)
        if __name.endswith('-' + ARCH) and os.path.isdir(__full_name):
            print("Adding {0}".format(__name))
            copy_into(__full_name, __out_dir, '.')

    # print("Bundling {0} into {1}".format(__out_dir, os.path.join(__dist_dir, '..', 'petronia-' + ARCH + '.zip')))
    print("Bundling zip")
    __zipf = zipfile.ZipFile(os.path.join(__dist_dir, '..', 'petronia-' + ARCH + '.zip'), 'w', zipfile.ZIP_DEFLATED)
    __dirs = [(__out_dir, '')]
    while len(__dirs) > 0:
        __root, __path = __dirs.pop()
        for __file in os.listdir(__root):
            __f = os.path.join(__root, __file)
            __z = __path + __file
            if os.path.isdir(__f):
                __dirs.append((__f, __z + '/'))
            else:
                # print("  {0} -> {1}".format(__f, __z))
                __zipf.write(__f, __z)
    __zipf.close()
