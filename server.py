#!/usr/bin/env python3

import subprocess
import os
import signal


def run_gunicorn():
    """Start Gunicorn server."""
    subprocess.Popen(
        ["gunicorn", "RentEase.wsgi", "--log-file", "-"],
        preexec_fn=os.setsid,  # To run in a new process group
    )


def run_celery():
    """Start Celery worker."""
    subprocess.Popen(
        ["celery", "-A", "RentEase", "worker", "--loglevel=INFO"],
        preexec_fn=os.setsid,  # To run in a new process group
    )


def stop_processes():
    """Stop all processes."""
    os.killpg(0, signal.SIGKILL)  # Kills all processes in the current process group


if __name__ == "__main__":
    try:
        run_gunicorn()
        run_celery()
    except KeyboardInterrupt:
        print("Keyboard interrupt detected, stopping processes...")
        stop_processes()
