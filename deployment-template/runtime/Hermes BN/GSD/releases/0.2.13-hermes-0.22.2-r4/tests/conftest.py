import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from pathlib import Path


def pytest_addoption(parser):
    parser.addoption("--gsd-settings", default=str(Path(__file__).resolve().parents[3] / "operator/settings.json"),
                     help="Existing operator settings; tests create independent temporary state and keys")
