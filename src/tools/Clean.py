import os
import shutil
from src.utils.OsUtil import OsUtil


class Clean(object):
    # cursor = DataBaseUtil.query_by_sql('select match_type,match_content from t_clean_setting')
    target_dir = os.path.join(OsUtil.get_desktop(), '桌面')

    @staticmethod
    def clean_setting():
        print(123)

    @staticmethod
    def clean():
        # 拉取所有的桌面文件
        desktop_path = OsUtil.get_desktop()
        # 过滤掉word等文件的浏览缓存数据
        file_names = filter(lambda file: not file.startswith('~$'), os.listdir(desktop_path))
        for file_name in file_names:
            if os.path.isdir(os.path.join(desktop_path, file_name)) or 'lnk' in file_name:
                continue
            # 解析文件名，如果命中规则，则将文件移动至指定文件夹
            Clean.do_clean(file_name)

    @staticmethod
    def do_clean(file_name):
        if not os.path.exists(Clean.target_dir):
            os.makedirs(Clean.target_dir)
        folders = os.listdir(Clean.target_dir)
        for folder in folders:
            if folder in file_name:
                shutil.move(os.path.join(OsUtil.get_desktop(), file_name), os.path.join(Clean.target_dir, folder))
                break

    @staticmethod
    def get_menu_info():
        return [
            ['./icon/setting.png', '设置', 'ctrl+Q', lambda: Clean.clean_setting()],
            ['./icon/doClean.png', '立即清理', 'ctrl+P', lambda: Clean.clean()]
        ]
