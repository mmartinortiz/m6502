import pytest

from m6502.memory import Memory
from m6502.processor import Processor


@pytest.fixture
def memory():
    return Memory()


@pytest.fixture
def cpu(memory):
    return Processor(memory)


@pytest.mark.parametrize(
    "expected",
    [
        # PC, Stack P., Cycles, B, D, I
        (0xFCE2, 0x01FD, 0, True, False, True)
    ],
)
def test_cpu_reset(cpu, expected) -> None:
    cpu.reset()
    assert (
        cpu.program_counter,
        cpu.stack_pointer,
        cpu.cycles,
        cpu.flag_b,
        cpu.flag_d,
        cpu.flag_i,
    ) == expected


@pytest.mark.parametrize(
    "address, value, expected",
    [(0x0001, 0xA5, (0xFCE2, 0x01FD, 2, True, False, True, 0xA5))],
)
def test_cpu_read_write_byte(cpu, address, value, expected):
    cpu.reset()
    cpu.write_byte(address, value)
    read_value = cpu.read_byte(address)

    assert (
        cpu.program_counter,
        cpu.stack_pointer,
        cpu.cycles,
        cpu.flag_b,
        cpu.flag_d,
        cpu.flag_i,
        read_value,
    ) == expected
