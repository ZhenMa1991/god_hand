import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from src.tools import Clean


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_window()

    # 初始化窗口
    def init_window(self):
        # 设置窗口的位置和大小
        self.resize(1000, 650)
        self.center()
        self.setWindowTitle('Everything')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('./icon/clean.png'))
        self.init_menu()
        self.show()

    # 将窗口居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_menu(self):
        self._add_menu('桌面清理', Clean.Clean.get_menu_info())

    def _add_menu(self, menu_name, option_infos):
        menu_bar = self.menuBar()
        file = menu_bar.addMenu(menu_name)
        for option_info in option_infos:
            option = QAction(QIcon(option_info[0]), option_info[1], self)
            option.setShortcut(option_info[2])
            option.triggered.connect(option_info[3])
            file.addAction(option)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
