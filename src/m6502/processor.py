from typing import Literal

from m6502.memory import Memory


class Processor:
    def __init__(self, memory: Memory) -> None:
        """Initialize the processor."""
        self.memory = memory

        # Accumulator A
        self.reg_a = 0

        # Incex Register Y
        self.reg_y = 0

        # Incex Register X
        self.reg_x = 0

        # Program counter PC
        self.program_counter = 0

        # Stack Pointer S
        self.stack_pointer = 0

        # Cycles used
        self.cycles = 0

        # Status flags
        self.flag_c = True
        self.flag_z = True
        self.flag_i = True
        self.flag_d = True
        self.flag_b = True
        self.flag_v = True
        self.flag_n = True

    def reset(self) -> None:
        """Reset processor to initial state."""

        # Hardcoded start vector post-reset
        self.program_counter = 0xFCE2

        # Hardcoded stack pointer post-reset
        self.stack_pointer = 0x01FD

        self.cycles: Literal[0] = 0
        self.flag_i = True
        self.flag_d = False
        self.flag_b = True
