import subprocess

def test_single_addition():
    #path to build
    executable_path = "parent_child_sim/build/device_sim.exe"

    input_to_device = "5\n1\n0\n"

    result = subprocess.run(
        [executable_path],
        input=input_to_device,
        capture_output=True,
        text=True
    )

    print(result.stdout)
    assert "End sum: 6" in result.stdout
