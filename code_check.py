import subprocess


def run_command(command):
    result = subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    return result.stdout.decode() + result.stderr.decode()


print("Running black...")
black_output = run_command("black --check .")
print(black_output)

print("Running isort...")
isort_output = run_command("isort --check-only .")
print(isort_output)

print("Running flake8...")
flake8_output = run_command("flake8 .")
print(flake8_output)
