"""
Room Acoustics
--------------
Here are contained some functions that are related to room acoustics.

- `reverb_time()`
- `find_modes()`
- `convolve_rir_on_signal()`
- `find_ir_start()`

"""
from .room_acoustics import (reverb_time, find_modes, convolve_rir_on_signal,
                             find_ir_start)

__all__ = [
    'reverb_time',
    'find_modes',
    'convolve_rir_on_signal',
    'find_ir_start',
]
