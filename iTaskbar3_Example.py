import sys
from pathlib import Path

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
)

from iTaskbar3 import ITaskbarList3


# =========================================================
# Paths
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

RESOURCE_DIR = BASE_DIR / "resources"

DOWNLOADING_ICON = RESOURCE_DIR / "downloading.ico"
PAUSED_ICON = RESOURCE_DIR / "paused.ico"
ERROR_ICON = RESOURCE_DIR / "error.ico"
COMPLETED_ICON = RESOURCE_DIR / "completed.ico"


# =========================================================
# Main Window
# =========================================================

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("YawStar iTaskbar3 Demo")

        self.resize(600,400)

        # -------------------------------------------------
        # UI
        # -------------------------------------------------

        layout = QVBoxLayout()

        self.status_label = QLabel(
            "Ready"
        )

        self.btn_loading = QPushButton(
            "Loading / Indeterminate"
        )

        self.btn_download = QPushButton(
            "Downloading"
        )

        self.btn_pause = QPushButton(
            "Paused"
        )

        self.btn_error = QPushButton(
            "Error"
        )

        self.btn_complete = QPushButton(
            "Completed"
        )

        self.btn_clear = QPushButton(
            "Clear Taskbar"
        )

        layout.addWidget(
            self.status_label
        )

        layout.addWidget(
            self.btn_loading
        )

        layout.addWidget(
            self.btn_download
        )

        layout.addWidget(
            self.btn_pause
        )

        layout.addWidget(
            self.btn_error
        )

        layout.addWidget(
            self.btn_complete
        )

        layout.addWidget(
            self.btn_clear
        )

        container = QWidget()

        container.setLayout(
            layout
        )

        self.setCentralWidget(
            container
        )

        # -------------------------------------------------
        # Native HWND
        # -------------------------------------------------

        hwnd = int(
            self.winId()
        )

        # -------------------------------------------------
        # Windows Taskbar
        # -------------------------------------------------

        self.taskbar = ITaskbarList3(
            hwnd
        )

        # -------------------------------------------------
        # Demo Progress
        # -------------------------------------------------

        self.progress = 0

        self.timer = QTimer(
            self
        )

        self.timer.timeout.connect(
            self.update_download_progress
        )

        # -------------------------------------------------
        # Buttons
        # -------------------------------------------------

        self.btn_loading.clicked.connect(
            self.show_loading
        )

        self.btn_download.clicked.connect(
            self.start_download
        )

        self.btn_pause.clicked.connect(
            self.pause_download
        )

        self.btn_error.clicked.connect(
            self.show_error
        )

        self.btn_complete.clicked.connect(
            self.complete_download
        )

        self.btn_clear.clicked.connect(
            self.clear_taskbar
        )


    # =====================================================
    # Loading
    # =====================================================

    def show_loading(self):

        self.timer.stop()

        self.taskbar.indeterminate(
            DOWNLOADING_ICON
        )

        self.status_label.setText(
            "Loading..."
        )


    # =====================================================
    # Start Download
    # =====================================================

    def start_download(self):

        self.progress = 0

        self.taskbar.downloading(
            0,
            100,
            DOWNLOADING_ICON,
        )

        self.status_label.setText(
            "Downloading 0%"
        )

        self.timer.start(
            100
        )


    # =====================================================
    # Update Download
    # =====================================================

    def update_download_progress(self):

        self.progress += 1

        if self.progress >= 100:

            self.timer.stop()

            self.complete_download()

            return

        self.taskbar.downloading(
            self.progress,
            100,
            DOWNLOADING_ICON,
        )

        self.status_label.setText(
            f"Downloading {self.progress}%"
        )


    # =====================================================
    # Pause
    # =====================================================

    def pause_download(self):

        self.timer.stop()

        self.taskbar.paused(
            self.progress,
            100,
            PAUSED_ICON,
        )

        self.status_label.setText(
            f"Paused {self.progress}%"
        )


    # =====================================================
    # Error
    # =====================================================

    def show_error(self):

        self.timer.stop()

        self.taskbar.error(
            self.progress,
            100,
            ERROR_ICON,
        )

        self.status_label.setText(
            "Download Error"
        )


    # =====================================================
    # Completed
    # =====================================================

    def complete_download(self):

        self.timer.stop()

        self.taskbar.completed(
            COMPLETED_ICON
        )

        self.status_label.setText(
            "Download Completed"
        )


    # =====================================================
    # Clear
    # =====================================================

    def clear_taskbar(self):

        self.timer.stop()

        self.taskbar.reset()

        self.status_label.setText(
            "Ready"
        )


    # =====================================================
    # Close Event
    # =====================================================

    def closeEvent(self, event):

        self.timer.stop()

        self.taskbar.close()

        super().closeEvent(
            event
        )


# =========================================================
# Application
# =========================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()
    
    sys.exit(app.exec())