# Avian Blasters

Avian Blasters (or Avian Blasters: The Avians Strike Back) is a desktop game application with a GUI inspired by arcade games such as Space Invaders and Galaga, developed in Python for a University Software Engineering project work, built using pygame, pygame_menu and the template provided by the University course.

---

Defend yourself agianst the Avians, with your trusty car, the Jolly Runner, in this arcade inspired shooter.

Your driving and shooting skills will be put to the test as every distraction will become your worst nightmare!

Don't forget to use Power-Ups dropped from defeated enemies to increase the odds of survival against this never-ending enemy horde of the flying variety.

Coming to your home in 2025, on Windows, Linux, and MacOs devices!

Are you brave enough to face the rising odds?

---
For a more detailed user guide, describing all the in-game features and controls, click [`here`](https://unibo-dtm-se-2425-avianblasters.github.io/report/sections/09-userguide/)! 

## To start the software application

Python version 3.9 or above is required for this application and needs to be installed on your device.

1) Clone the repository locally: 

        git clone https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact.git

2) Go into artifact:
        
        cd artifact

3) Install the required dependencies:

        pip install -r requirements.txt
    
    For developmental purpouses use:

        pip install -r requirements-dev.txt

4) Launch the application:

        python -m Avian_Blasters

## Futher resources

[`Bug Reports`](https://github.com/unibo-dtm-se-2425-AvianBlasters/artifact/issues)

[`Project documentation`](https://unibo-dtm-se-2425-avianblasters.github.io/report)

[`TestPyPi page`](https://test.pypi.org/project/Avian-Blasters/3.1.0/)

[`Link to the project template`](https://github.com/unibo-dtm-se/template-python-project)

## Project structure 

Overview:
```bash
<root directory>
├── Avian_Blasters/             # main package
│   ├── __init__.py         # python package marker
│   └── __main__.py         # application entry point
├── test/                   # test package
├── .github/                # configuration of GitHub CI
│   └── workflows/          # configuration of GitHub Workflows
│       ├── check.yml       # runs tests on multiple OS and versions of Python
│       └── deploy.yml      # if check succeeds, and the current branch is master, automatic release on TestPyPi is triggered
├── MANIFEST.in             # file stating what to include/exclude in releases 
├── LICENSE                 # license file (Apache 2.0)
├── pyproject.toml          # declares build dependencies
├── renovate.json           # configuration of Renovate bot, for automatic dependency updates
├── requirements-dev.txt    # declares development dependencies
├── requirements.txt        # declares runtime dependencies
├── setup.py                # configuration of the package to be released on TestPyPi
└── Dockerfile              # configuration of the Docker image to be realsed on Dockerhub
```
