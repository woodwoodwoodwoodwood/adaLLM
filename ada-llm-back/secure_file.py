import os
import re
import unicodedata

# 修改正则表达式以支持更多字符，包括中文字符
_filename_strip_re = re.compile(r'[^A-Za-z0-9\u4e00-\u9fa5_.-]')  # 仅移除不安全的字符
_windows_device_files = {
    'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',
    'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'
}

def secure_filename_wood(filename: str) -> str:
    """Pass it a filename and it will return a secure version of it. This
    filename can then safely be stored on a regular file system and passed
    to :func:`os.path.join`. The filename returned is a Unicode string for
    maximum portability.
    """
    # 正常化文件名以处理 Unicode 字符
    filename = unicodedata.normalize("NFKC", filename)
    for sep in os.sep, os.path.altsep:
        if sep:
            filename = filename.replace(sep, " ")
    # 移除不安全的字符
    filename = str(_filename_strip_re.sub("", "_".join(filename.split()))).strip("._")

    # 在 Windows 系统中，确保文件名不是特殊设备文件名
    if os.name == "nt" and filename and filename.split(".")[0].upper() in _windows_device_files:
        filename = f"_{filename}"

    return filename
