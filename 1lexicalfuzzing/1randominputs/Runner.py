from typing import Any, List, Tuple, Union
import subprocess


Outcome = str

class Runner:
    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRELOVED"

    def __init__(self) -> None:

        pass

    def run(self, inp: str) -> Any:
        """run the runner with the given input"""
        return (inp, Runner.UNRESOLVED)


class PrintRunner(Runner):
        def run(self, inp) -> Any:
        # """Print the given input"""
            print(inp)
            return (inp, Runner.UNRESOLVED)

class ProgramRunner(Runner):
    def __init__(self, program:Union[str, List[str]]) -> None:
        self.program = program
    def run_process(self, inp: str="") -> subprocess.CompletedProcess:
        return subprocess.run(self.program,
                input=inp,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True)

    def run(self, inp:str="") -> Tuple[subprocess.CompletedProcess, Outcome]:
        """Run the program with `inp` as input.  
           Return test outcome based on result of `subprocess.run()`."""
        result = self.run_process(inp)

        if result.returncode == 0:
            outcome = self.PASS
        elif result.returncode < 0:
            outcome = self.FAIL
        else:
            outcome = self.UNRESOLVED

        return (result, outcome)

if __name__ == "__main__":
    cat = ProgramRunner(program="cat")
    cat.run("hello")


class Fuzzer:
    """Base class for fuzzers."""

    def __init__(self) -> None:
        """Constructor"""
        pass

    def fuzz(self) -> str:
        """Return fuzz input"""
        return ""

    def run(self, runner: Runner = Runner()) \
            -> Tuple[subprocess.CompletedProcess, Outcome]:
        """Run `runner` with fuzz input"""
        return runner.run(self.fuzz())

    def runs(self, runner: Runner = PrintRunner(), trials: int = 10) \
            -> List[Tuple[subprocess.CompletedProcess, Outcome]]:
        """Run `runner` with fuzz input, `trials` times"""
        return [self.run(runner) for i in range(trials)]

import random

class RandomFuzzer(Fuzzer):
    """Produce random inputs."""

    def __init__(self, min_length: int = 10, max_length: int = 100,
                 char_start: int = 32, char_range: int = 32) -> None:
        """Produce strings of `min_length` to `max_length` characters
           in the range [`char_start`, `char_start` + `char_range`)"""
        self.min_length = min_length
        self.max_length = max_length
        self.char_start = char_start
        self.char_range = char_range

    def fuzz(self) -> str:
        string_length = random.randrange(self.min_length, self.max_length + 1)
        out = ""
        for i in range(0, string_length):
            out += chr(random.randrange(self.char_start,
                                        self.char_start + self.char_range))
        return out
'''
random_fuzzer = RandomFuzzer(min_length=20, max_length=20)
for i in range(10):
    inp = random_fuzzer.fuzz()
    result, outcome = cat.run(inp)
    print(result, outcome)
    assert result.stdout == inp
    assert outcome == Runner.PASS
'''

random_fuzzer = RandomFuzzer(min_length=20, max_length=20)
cat = ProgramRunner(program="cat")

print(random_fuzzer.runs(cat, 10))