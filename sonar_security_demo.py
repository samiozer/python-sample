"""Non-production Sonar demo; excluded from the Docker build context."""

import hashlib


def demo_weak_hash(value: str) -> str:
    return hashlib.md5(value.encode("utf-8")).hexdigest()
