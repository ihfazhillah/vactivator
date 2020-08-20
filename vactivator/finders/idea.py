from pathlib import Path
from xml.etree.ElementTree import ElementTree


from vactivator.finders.base import BaseFinder


class IdeaFinder(BaseFinder):
    def test(self):
        idea = self.path / ".idea"
        return idea.exists()

    def get_venv_activator(self):
        workspace = self.path / ".idea" / "workspace.xml"
        with workspace.open("r") as workspace_xml:
            # root = etree.parse(workspace_xml)

            # only work on unix like. how about windows ???
            home = Path.home()
            etree = ElementTree()
            root = etree.parse(source=workspace_xml)
            python_path = root.find(".//option[@name='mySdkHome']").attrib["value"]

            abs_python_path = python_path.replace("$USER_HOME$", str(home))

            return str(Path(abs_python_path).parent / "activate")
