import sys
import pkg_resources
import subprocess as sp


def setup():
    """Function for installing necessary modules i.e.:

    - rich
    - questionary
    - youtube-dl
    - tabulate"""
    installed = {pkg.key for pkg in pkg_resources.working_set}
    required = {"rich", "questionary", "youtube-dl", "tabulate"}
    missing = required - installed
    if missing:
        for module in missing:
            try:
                sp.check_call(
                    [
                        sys.executable,
                        "-m",
                        "pip",
                        "install",
                        "--no-cache-dir",
                        module,
                    ],
                    stdout=sp.DEVNULL,
                )
            except sp.SubprocessError as e:
                print(e)
                exit()
            else:
                print("{} was installed successfully".format(module))
