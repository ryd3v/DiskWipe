import os
import platform
import subprocess
import threading
import time

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

start_time = None


class DiskWipeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def wipe_disk(self):
        global start_time
        start_time = time.time()
        threading.Thread(target=self.wipe_disk_thread).start()

    def wipe_disk_windows(self, disk):
        subprocess.run(['cipher', '/w:' + disk], check=True)

    def wipe_disk_linux(self, disk, num_passes):
        for i in range(num_passes):
            subprocess.run(['sudo', 'dc3dd', f'wipe={disk}', 'pat=0x00', f'hash=sha256', f'hlog=pass{i + 1}.log'],
                           check=True)

    def wipe_disk_thread(self):
        disk = self.disk_entry.text()
        os_name = platform.system()
        if os_name == 'Windows':
            if not os.path.exists(disk):
                self.show_error('Error', f'Disk {disk} does not exist.')
                return
            self.wipe_disk_windows(disk)
        elif os_name == 'Linux':
            num_passes = int(self.num_passes_entry.text())  # Convert to integer here
            if not os.path.exists(disk):
                self.show_error('Error', f'Disk {disk} does not exist.')
                return
            try:
                self.wipe_disk_linux(disk, num_passes)
            except subprocess.CalledProcessError:
                self.show_error('Error', f'Failed to wipe disk {disk}.')
        else:
            self.show_error('Error', 'Unsupported operating system.')

    def update_timer(self):
        if start_time is not None:
            elapsed_time = time.time() - start_time
            self.timer_label.setText(f'Elapsed time: {int(elapsed_time)} seconds')

    def init_ui(self):
        self.setWindowTitle('Disk Wipe')
        self.setGeometry(100, 100, 500, 300)
        layout = QVBoxLayout()

        self.disk_label = QLabel('Disk:')
        layout.addWidget(self.disk_label)
        self.disk_entry = QLineEdit()
        layout.addWidget(self.disk_entry)

        self.num_passes_label = QLabel('Number of Passes:')
        layout.addWidget(self.num_passes_label)
        self.num_passes_entry = QLineEdit()
        layout.addWidget(self.num_passes_entry)

        self.timer_label = QLabel('Elapsed time: 0 seconds')
        layout.addWidget(self.timer_label)

        self.wipe_button = QPushButton('Wipe Disk')
        self.wipe_button.clicked.connect(self.wipe_disk)
        layout.addWidget(self.wipe_button)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # update every second

    def show_error(self, title, message):
        QMessageBox.critical(self, title, message)


if __name__ == '__main__':
    app = QApplication([])
    disk_wipe_app = DiskWipeApp()
    disk_wipe_app.show()
    app.exec()
