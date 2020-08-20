from pathlib import Path

import click

from vactivator import activator
from vactivator.finders import idea, venv_in_curdir


@click.group()
def vactivator():
    pass

@vactivator.command()
def activate():
    curdir = Path.cwd()
    finders = [
        idea.IdeaFinder,
        venv_in_curdir.VenvInCurdirFinder
    ]
    for finder_class in finders:
        finder = finder_class(str(curdir))
        if finder.test():
            activator_path = finder.get_venv_activator()
            activator.activate(activator_path)
            return


if __name__ == "__main__":
    vactivator()