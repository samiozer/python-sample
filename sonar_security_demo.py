"""Non-production Sonar demo; excluded from the Docker build context."""

import hashlib


def demo_weak_hash(value: str) -> str:
    return hashlib.sha512(value.encode("utf-8")).hexdigest()
