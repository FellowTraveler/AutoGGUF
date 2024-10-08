import sys
from typing import TextIO, Union

from PySide6.QtWidgets import (
    QMessageBox,
)

from Localizations import *


def show_about(self) -> None:
    about_text = (
        "AutoGGUF\n\n"
        f"Version: {AUTOGGUF_VERSION}\n\n"
        "A tool for managing and converting GGUF models."
    )
    QMessageBox.about(self, "About AutoGGUF", about_text)


def ensure_directory(path) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def open_file_safe(file_path, mode="r") -> TextIO:
    encodings = ["utf-8", "latin-1", "ascii", "utf-16"]
    for encoding in encodings:
        try:
            return open(file_path, mode, encoding=encoding)
        except UnicodeDecodeError:
            continue
    raise ValueError(
        f"Unable to open file {file_path} with any of the encodings: {encodings}"
    )


def resource_path(relative_path) -> Union[str, str, bytes]:
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller path
        base_path = sys._MEIPASS
    elif "__compiled__" in globals():
        # Nuitka path
        base_path = os.path.dirname(sys.executable)
    else:
        # Regular Python path
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
