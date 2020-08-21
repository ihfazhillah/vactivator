from pathlib import Path
from xml.etree.ElementTree import ElementTree


from vactivator.finders.base import BaseFinder


class IdeaFinder(BaseFinder):
    def get_python_path(self):
        workspace = self.path / ".idea" / "workspace.xml"
        with workspace.open("r") as workspace_xml:
            # only work on unix like. how about windows ???
            etree = ElementTree()
            root = etree.parse(source=workspace_xml)
            python_path = root.find(".//option[@name='mySdkHome']")
        return python_path

    def test(self):
        idea = self.path / ".idea"
        return idea.exists() and self.get_python_path()

    def get_venv_activator(self):
        home = Path.home()
        python_path = self.get_python_path().attrib["value"]
        abs_python_path = python_path.replace("$USER_HOME$", str(home))

        return str(Path(abs_python_path).parent / "activate")
