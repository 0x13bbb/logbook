# logbook
I'm writing a personal tool to track my mood and some habits. These are just my personal observations/opinions--YMMV. Just going to dump the entire spec here.

## todo
- [ ] backend
    - [x] track moods
        - [x] get/set moods
    - [x] habits
        - [x] get/set habits
        - [x] get/set habit milestones + incentives
    - [x] notifier
    - [ ] protocol
- [ ] frontend
    - [ ] score moods
    - [ ] track habits
    - [ ] mood/habit dashboard
- [ ] someday (stretch)
    - [ ] auto-open on schedule?

## installation (mac)
### backend
Python version: 3.12.3
1. you can check your version `python --version` if you are already on this version the below is optional
2. if you want to use pyenv (python version manager) `brew install pyenv`
3. set your local with `pyenv local 3.12`

Set up your virtual environment
1. cd to `/backend`
2. create a virtual environment called `.venv` with `python -m venv .venv`
3. activate the virtual environment with `source .venv/bin/activate`

Installing prerequisites
1. `pip install -r requirements.txt`

Running the backend
1. `fastapi dev main.py`
