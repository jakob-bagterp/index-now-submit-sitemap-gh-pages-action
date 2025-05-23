import subprocess

from colorist import Color


def test_submit_sitemap_from_terminal(capfd: object) -> None:
    subprocess.call(["python3", "./src/helper/submit_sitemap.py",
                     "jakob-bagterp.github.io",
                     "6d71a14ac15c4c41a0c19e641f659208",
                     "https://jakob-bagterp.github.io/index-now-api-key.txt",
                     "https://jakob-bagterp.github.io/index-now-submit-sitemap-action/sitemap.xml",
                     "yandex"
                     ])
    terminal_output, _ = capfd.readouterr()
    assert f"URL(s) submitted successfully to the IndexNow API:{Color.OFF}" in terminal_output
    assert f"Status code: {Color.GREEN}200{Color.OFF}" or f"Status code: {Color.GREEN}202{Color.OFF}" in terminal_output
