import logging
import subprocess

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
logger.addHandler(console)


def main():
    try:
        pip_list = subprocess.check_output(
            ["pip", "list", "--format=freeze"])
    except Exception as e:
        logger.error("%s", e)
        return
    stdout_lines = pip_list.decode().split("\n")
    if not stdout_lines:
        logger.error("`pip list --format=freeze` output is empty")
        return

    installed_packages = set()
    for line in stdout_lines:
        p = line.split("==")
        if p and p[0].strip():
            installed_packages.add(p[0].strip())

    with open('malicious_packages.txt', 'r') as f:
        malicious_packages = set(x.strip() for x in f.read().splitlines())
        detected_packages = installed_packages.intersection(malicious_packages)
        if detected_packages:
            logger.warning(
                "%d malicious pip package%s from `malicious_packages.txt`"
                " detected in `pip list --format=freeze` output"
                "\nThe packages are\n%s", len(detected_packages),
                "s" if len(detected_packages) > 1 else "", sorted(detected_packages))


if __name__ == "__main__":
    main()
