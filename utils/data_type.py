from typing import Dict, Union


class DataType:
    data = Dict[str, Union[str, bool, Dict[str, Union[str, bool]]]]
