"""
CineSense Application Runner.

This script provides a simple command-line interface to launch the
CineSense Streamlit application. It uses the `subprocess` module to
execute the `streamlit run` command, ensuring that the application
starts correctly.

This runner is designed to be the main entry point for the application,
making it easy to start the web server from the command line or from
a Docker container. It is a lightweight and straightforward way to
get the CineSense app up and running.

Usage:
    python run.py
"""

import subprocess
import sys
from pathlib import Path


def main() -> None:
    """
    Main function to launch the Streamlit application.

    This function finds the path to the main `app.py` file and uses
    `subprocess.run` to execute the `streamlit run` command. It also
    includes error handling to gracefully manage cases where the
    `app.py` file is not found.
    """
    app_path = Path(__file__).parent / "app.py"

    if not app_path.exists():
        print(f"Error: Could not find the main application file at: {app_path}")
        sys.exit(1)

    try:
        subprocess.run(
            ["streamlit", "run", str(app_path)],
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        print(
            "Error: `streamlit` command not found. Please make sure "
            "Streamlit is installed and in your PATH."
        )
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the Streamlit app: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)


if __name__ == "__main__":
    main()
