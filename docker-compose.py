import sys
import subprocess
import logging
from pathlib import Path


def get_yaml():
    return [
        p.name
        for p in Path.cwd().iterdir()
        if p.is_file() and p.suffix.lower() in {".yml", ".yaml"}
    ]

def docker_compose_up(yaml_list):
    for file in yaml_list:
        try:
            subprocess.run(
                ["docker", "compose", "-f", file, "up", "-d"],
                check=True
            )
            print(f"Started {file}")
        except subprocess.CalledProcessError:
            print(f"Failed to start {file}")

def docker_compose_down(yaml_list):
    for file in yaml_list:
        try:
            subprocess.run(
                ["docker", "compose", "-f", file, "down"],
                check=True
            )
            print(f"Started {file}")
        except subprocess.CalledProcessError:
            print(f"Failed to stop {file}")

def main():
    yaml_list = get_yaml()
    if not yaml_list:
        print("No YAML files found.")
        return
    docker_compose_up(yaml_list)
    
if __name__ == "__main__":
    main()


