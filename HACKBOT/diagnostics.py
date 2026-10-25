import subprocess
import platform 
import socket


def get_system_info():
    print("=========HACKBOT SYTSEM DIAGNOSTICS===========")
    platform_system = {
        "System: ": platform.system(),
        "Python Version: ": platform.python_version(),
        "Architecture: ": platform.architecture(),
        "Processor: ": platform.processor()
    }
    for key, value in platform_system.items():
        print(f"{key}{value}")
    print("="*70)

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname) 
    print(f"Hostname: {hostname}\nIP: {ip}\n")
    '''
    capture_output=True - this directs python to catch the output (stdout) and errors (stderr) instead of printing them 
    directily to the console
    text=True - this tells python to automatically handle the decoded text string. Without this, result.stdout returns raw bytes
    that you woudl have to manually format using .decode('utf-8) or .decode('oem) 
    List Format ['ipconfig', '/all'] - passing arguments as a list of strings is safer and preferred over a single string 
    becasue it bypasses shell injection vulnerabilities and does requre setting shell=True
    '''
    try:
    # to run the ipconfig
        result = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}")
        print(e.stderr)




print(get_system_info())