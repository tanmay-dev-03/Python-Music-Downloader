from setup import setup

setup()
from rich import print
import os
import sys
import questionary as qr


class MainApp:
    def __init__(self) -> None:
        self.termSize = termSize = os.get_terminal_size()
        print("-" * termSize.columns)
        print("Music Downloader".center(termSize.columns))
        print("-" * termSize.columns)

    def chooseAction(self):
        print("[b red] Choose An Action[/]".center(self.termSize.columns))
        actions = [
            "Download a PlayList",
            "Download a Single Song",
        ]

        choice = qr.select(
            "Choose an action:",
            choices=actions,
            default=actions[1],
        ).ask()

        if choice == actions[0]:
            self.playListMode()
        elif choice == actions[1]:
            self.singleMode()

    def playListMode(self):
        print("[b green]PlayList mode[/]")

    def singleMode(self):
        print("[b green]Single Song Mode[/]")
