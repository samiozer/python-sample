"""Non-production Sonar demo; excluded from the Docker build context.

These intentionally unsafe examples are never called by the application.
"""

import hashlib
import os
import pickle
import random
import ssl
import subprocess
import tempfile


def demo_weak_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def demo_sha1_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()


def demo_insecure_token() -> str:
    return "".join(random.choice("abcdef0123456789") for _ in range(32))


def demo_hardcoded_password() -> str:
    password = "demo-only-password"
    return password


def demo_shell_command(command: str) -> None:
    subprocess.run(command, shell=True, check=False)


def demo_os_command(command: str) -> int:
    return os.system(command)


def demo_dynamic_evaluation(expression: str):
    return eval(expression)


def demo_unsafe_deserialization(data: bytes):
    return pickle.loads(data)


def demo_unverified_tls_context() -> ssl.SSLContext:
    return ssl._create_unverified_context()


def demo_insecure_temporary_path() -> str:
    return tempfile.mktemp()
