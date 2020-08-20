from vactivator.finders.base import BaseFinder


class VenvInCurdirFinder(BaseFinder):
    pattern = "**/bin/python"
    def test(self):
        return len(list(self.path.glob(self.pattern))) > 0

    def get_venv_activator(self):
        paths = list(self.path.glob(self.pattern))

        # for now use the first
        python_path = paths[0]

        return str(python_path.parent / "activate")