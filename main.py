from setup import setup

setup()
import os
import sys
import subprocess as sp

import questionary as qr
import requests
from rich import print


class MainApp:
    def __init__(self) -> None:
        self.termSize = termSize = os.get_terminal_size()
        print(sys.version)
        print(sys.executable)
        print("-" * termSize.columns)
        print("Music Downloader".center(termSize.columns))
        print("-" * termSize.columns)

    def chooseAction(self):
        print("[b red] Choose An Action[/]")
        actions = [
            "Download a Single Song",
            "Download a PlayList",
        ]

        choice = qr.select(
            "Choose an action:",
            choices=actions,
            default=actions[0],
        ).ask()

        if choice == actions[1]:
            self.playListMode()
        elif choice == actions[0]:
            self.singleMode()

    def playListMode(self):
        """
        Method for downloading songs from PlayList.
        Uses youtube-dl under the hood.
        """
        print("[b blue]PlayList mode[/]")
        while True:
            url = qr.text(
                "Enter the URL for the PlayList:", qmark="*", multiline=True
            ).ask()

            try:
                requests.get(url)
                # resp.status_code
            except requests.ConnectionError as e:
                print(e)
                return
            else:
                print("URL validated successfully!")
                break

        pathForSong = qr.path(
            "Select the Folder to which you want to download the songs:",
            only_directories=True,
        ).ask()

    def singleMode(self):
        """
        Method for downloading a single song.
        uses youtube-dl under the hood
        """
        print("[b blue] Single Song Mode [/]")

        pathForSong = qr.path(
            "Select path for downloading songs:",
            only_directories=True,
            qmark=">>>",
        ).ask()

        # os.chdir(pathForSong)
        sp.run(
            [
                "cd",
                f"{pathForSong}",
            ],
            shell=True,
        )


if __name__ == "__main__":
    app = MainApp()
    app.chooseAction()
