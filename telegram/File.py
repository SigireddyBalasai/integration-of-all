from dataclasses import dataclass
from typing import Union


@dataclass
class File:
    file_id: Union[str, None] = None
    file_unique_id: Union[str, None] = None
    file_size: Union[int, None] = None
    file_path: Union[str, None] = None
