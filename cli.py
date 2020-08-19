from pathlib import Path

import click

from vactivator.activator import activate
from vactivator.finders import idea


@click.group()
def vactivator():
    pass

@vactivator.command()
def activate():
    curdir = Path.cwd()
    finders = [
        idea.IdeaFinder
    ]
    for finder_class in finders:
        finder = finder_class(str(curdir))
        if finder.test():
            activator_path = finder.get_venv_activator()
            activate(activator_path)


if __name__ == "__main__":
    vactivator()