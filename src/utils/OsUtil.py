import os


class OsUtil(object):

    @staticmethod
    def get_desktop():
        return os.path.join(os.path.expanduser('~'), "Desktop")