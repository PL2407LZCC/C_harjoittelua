import subprocess
import pytest

#adding a fixture to have the compilation automated for all tests
@pytest.fixture(scope="session")
def compiled_device():
    source_file = "parent_child_sim/main.c"
    exe_path = "parent_child_sim/build/device_sim.exe"

    print("\n compiling... \n")
    compile_process = subprocess.run(["gcc", source_file, "-o", exe_path])
    assert compile_process.returncode == 0, "Compilation fail"

    yield exe_path

def run_device(executable_path, input_bytes):
    result = subprocess.run(
        [executable_path],
        input=input_bytes,
        capture_output=True,
        text=True
    )
    return result.stdout

def test_single_addition(compiled_device):

    input_to_device = "5\n1\n0\n"
    result = run_device(compiled_device, input_to_device)
    print(result)
    assert "End sum: 6" in result


def test_single_addition_with_faulty_input(compiled_device):

    input_to_device = "h\n0\n"
    result = run_device(compiled_device, input_to_device)
    print(result)
    assert "has to be integer, please continue" in result
    assert "End sum: 0" in result


