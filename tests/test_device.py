import subprocess

def test_single_addition():
    #path to build
    executable_path = "build/device_sim.exe"

    input_to_device = "5\n0\n"

    result = subprocess.run(
        [executable_path],
        input=input_to_device,
        capture_output=True,
        text=True
    )

    print(result.stdout)
    assert "End sum: 5" in result.stdout
