import json
import subprocess
import sys


def test_cli_returns_json_and_success():
    proc = subprocess.run(
        [sys.executable, "-m", "ml_service", "--amount", "2500", "--past-due", "2"],
        text=True,
        capture_output=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert json.loads(proc.stdout) == {"score": 50, "category": "medium"}


def test_cli_failure_returns_nonzero():
    proc = subprocess.run(
        [sys.executable, "-m", "ml_service", "--amount", "-1", "--past-due", "0"],
        text=True,
        capture_output=True,
        check=False,
    )
    assert proc.returncode == 2
    assert "Input error" in proc.stderr
    assert proc.stdout == ""
