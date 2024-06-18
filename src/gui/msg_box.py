from PyQt6.QtWidgets import QLabel, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontMetrics

class MessageBox(QLabel):
    def __init__(self, text = "", parent=None):
        super().__init__(text, parent)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: rgba(10, 10, 10, 128); color: red;")
        
        self.setGeometry(0, 0, 100, 30)  # 设置初始位置和大小
        self.set_font_size(20)
        self.adjustSizeToContent()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def set_font_size(self, size):
        font = self.font()
        font.setPointSize(size)
        self.setFont(font)

    def set_text(self, text):
        self.setText(text)
        self.adjustSizeToContent()
        

    def show(self):
        super().show()
        # self.move(0, 0)  # 每次显示时都移动到左上角
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        window_geometry = self.frameGeometry()
        x = screen_geometry.width() - window_geometry.width()
        self.move(x, 500)  # 每次显示时都移动到右上角


    def resizeEvent(self, event):
        super().resizeEvent(event)
        # self.move(0, 0)  # 当窗口大小改变时，也移动到左上角
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        window_geometry = self.frameGeometry()
        x = screen_geometry.width() - window_geometry.width()
        self.move(x, 500)  # 当窗口大小改变时，也移动到右上角

    def adjustSizeToContent(self):
        font_metrics = QFontMetrics(self.font())
        lines = self.text().splitlines()
        text_width = 0
        for line in lines:
            text_width = max(text_width,font_metrics.horizontalAdvance(line))
        text_height = font_metrics.height() * len(lines)  # 计算所有文本行的高度
        self.setFixedSize(text_width, text_height)

    def eventFilter(self, obj, event):
        if event.type() in (Qt.EventType.MouseButtonPress, Qt.EventType.MouseButtonRelease, Qt.EventType.MouseButtonDblClick, Qt.EventType.MouseMove):
            # 将鼠标事件传递到下层的窗口
            return False
        return super().eventFilter(obj, event)
    
    def mousePressEvent(self, event):
        # 不要处理鼠标点击事件，使其传递到下层窗口
        event.ignore()