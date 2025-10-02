import subprocess
import datetime
import glob
import socket
import time
import os

# Generate the filename with the current date
current_date = datetime.datetime.now().strftime("%Y%m%d")
directory = "/opt/splunk/var/"
hostname = socket.gethostname()
filename1 = f"{directory}{hostname}-configs-backup-apps-{current_date}.tgz"

# Define the tar command with the necessary options
tar_command1 = [
    "tar", "-cvzf", filename1,
    "--exclude", "splunk_gdi",
    "--exclude", "*/locale",
    "--exclude", "*/*.manifest",
    "--exclude", "license*",
    "--exclude", "python_upgrade_readiness_app",
    "--exclude", "*/appserver",
    "--exclude", "*/bin",
    "--exclude", "*/configs",
    "--exclude", "*/forExport",
    "--exclude", "splunk-rolling-upgrade",
    "--exclude", "*/icons*",
    "--exclude", "*/jars*",
    "--exclude", "*/java*",
    "--exclude", "*/keystore",
    "--exclude", "*/lib",
    "--exclude", "*/licenses",
    "--exclude", "*/LICENSES",
    "--exclude", "*/linu*",
    "--exclude", "*/local.old.*",
    "--exclude", "*/log*",
    "--exclude", "*/models",
    "--exclude", "*/outputs",
    "--exclude", "*/profiles",
    "--exclude", "*/README",
    "--exclude", "*/samples",
    "--exclude", "*/SampleTasks",
    "--exclude", "*/scripts",
    "--exclude", "*/Splunk_SA_Scientific_Python_linux_x86_64",
    "--exclude", "*/src",
    "--exclude", "*/static",
    "--exclude", "*/templates",
    "--exclude", "*/windows*",
    "--exclude", "*/default.old*",
    "-C", "/opt/splunk/etc/apps", ".",
]

# Run the tar command
try:
    subprocess.run(tar_command1, check=True)
    print(f"Backup created successfully: {filename1}")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while creating the backup: {e}")

filename2 = f"{directory}{hostname}-configs-backup-users-{current_date}.tgz"
# Define the tar command with the necessary options
tar_command2 = [
    "tar", "-cvzf", filename2,
    "-C", "/opt/splunk/etc/users", "."
]

try:
    subprocess.run(tar_command2, check=True)
    print(f"Backup created successfully: {filename2}")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while creating the backup: {e}")

filename3 = f"{directory}{hostname}-configs-backup-auth-{current_date}.tgz"
# Define the tar command with the necessary options
tar_command3 = [
    "tar", "-cvzf", filename3,
    "-C", "/opt/splunk/etc/auth", "."
]

try:
    subprocess.run(tar_command3, check=True)
    print(f"Backup created successfully: {filename3}")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while creating the backup: {e}")

filename4 = f"{directory}{hostname}-configs-backup-system-{current_date}.tgz"
# Define the tar command with the necessary options
tar_command4 = [
    "tar", "-cvzf", filename4,
    "-C", "/opt/splunk/etc/system/local", "."
]

try:
    subprocess.run(tar_command4, check=True)
    print(f"Backup created successfully: {filename4}")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while creating the backup: {e}")

# Define the directory and pattern
pattern = f"{directory}{hostname}-configs-backup-*.tgz"

# Get the current time
now = time.time()

# Define the age threshold (7 days in seconds)
age_threshold = 7 * 24 * 60 * 60

# Find all files matching the pattern
files = glob.glob(pattern)

# Check each file's age and remove if older than 7 days
for file_path in files:
    if os.stat(file_path).st_mtime < now - age_threshold:
        os.remove(file_path)
        print(f"Removed file: {file_path}")

