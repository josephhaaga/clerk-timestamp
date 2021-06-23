"""Append a timestamp to your clerk journals"""

import datetime
from typing import Mapping
from typing import Sequence


def get_timestamp(stamp_format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Returns a timestamp str in the specified format."""
    return datetime.datetime.now().strftime(stamp_format)


def append_timestamp(
    file_contents: Sequence[str], extension_config: Mapping = {}
) -> Sequence[str]:
    """Append a timestamp to the specified file_contents."""
    stamp_format = (
        "%Y-%m-%d %H:%M:%S"
        if "format" not in extension_config
        else extension_config["format"]
    )
    prefix = "\n[" if "prefix" not in extension_config else extension_config["prefix"]
    suffix = "] " if "suffix" not in extension_config else extension_config["suffix"]
    now = get_timestamp(stamp_format)
    return file_contents + [f"{prefix}{now}{suffix}"]
