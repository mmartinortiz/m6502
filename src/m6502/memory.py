class Memory:
    """Memory bank for MOT-6502 systems."""

    def __init__(self, size: int = 65536) -> None:
        """Initialize the memory."""
        if 0x0200 < (size - 1) > 0xFFFF:
            raise ValueError("Memory size is not valid")
        self.size = size
        self.memory = [0] * size
        print(len(self.memory))

    def __validate_address(self, address: int) -> bool:
        """Check if the address is correct"""
        if 0x0000 < address > self.size:
            raise ValueError(f"Memory address {address} is not valid")

        return True

    def __getitem__(self, address: int) -> int:
        self.__validate_address(address)

        return self.memory[address]

    def __setitem__(self, address: int, value: int) -> int:
        """Set the value at the specified memory address"""
        self.__validate_address(address)

        if value.bit_length() > 8:
            raise ValueError("Value too large")

        self.memory[address] = value

        return self.memory[address]
