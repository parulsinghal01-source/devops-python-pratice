import subprocess

service_name = "ssh"

result = subprocess.run(
    ["pgrep", service_name],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(f"{service_name} service is running")
else:
    print(f"{service_name} service is not running")
