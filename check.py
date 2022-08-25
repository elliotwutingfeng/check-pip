import logging
import subprocess

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
logger.addHandler(console)


def main():
    pip_list = subprocess.run(
        ["pip", "list", "--format=freeze"], capture_output=True)
    stdout_lines: list[str] = pip_list.stdout.decode().split("\n")
    std_err: str = pip_list.stderr.decode()
    if std_err:
        logger.error("%s", std_err)
        return
    if not stdout_lines:
        logger.error("`pip list --format=freeze` output is empty")
        return

    installed_packages: set[str] = set()
    for line in stdout_lines:
        p: list[str] = line.split("==")
        if p and p[0].strip():
            installed_packages.add(p[0].strip())

    with open('malicious_packages.txt', 'r') as f:
        malicious_packages = set(x.strip() for x in f.read().splitlines())
        detected_packages: set[str] = installed_packages.intersection(malicious_packages)
        if detected_packages:
            logger.warning(
                "%d malicious pip packages from `malicious_packages.txt`"
                " detected in `pip list --format=freeze` output"
                "\nThe packages are\n%s", len(detected_packages), sorted(detected_packages))


if __name__ == "__main__":
    main()
