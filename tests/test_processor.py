from m6502.memory import Memory
from m6502.processor import Processor


def test_cpu_reset() -> None:
    memory = Memory()
    cpu = Processor(memory)

    cpu.reset()
    assert (
        cpu.program_counter,
        cpu.stack_pointer,
        cpu.cycles,
        cpu.flag_b,
        cpu.flag_d,
        cpu.flag_i,
    ) == (0xFCE2, 0x01FD, 0, True, False, True)
