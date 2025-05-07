# SwitchLanController-Server
## Read before install or use
- I recommend that you use the git console to run the commands from Windows
- When installing requirements, the sistem will ask you for a driver install, this is also required
- Maybe you will need to allow the incoming data for the 8765 port in your firewall ( or just disable it )
- Don't close the application window to keep it running
- This software are tested on Windows
- Execute all the commands from a shell over the repo's directory
## Installing
- Download and install python3 if you don't have it
- Install venv using pip command line
  - `python -m pip install venv`
- Clone the git repo
  - `git clone https://github.com/devnull-tech/SwitchLanController-Server.git`
- Create a virtual environment
  - `python -m venv .venv`
- Install requirements on the environment
  - `source .venv/Scripts/activate`
  - `python -m pip install -r requirements.txt`
## Using steps
- Go to the repo's directory
- Open a terminal and execute the virtual environment
  - `source .venv/Scripts/activate`
- Run the program
  - `python main.py`
- Keep the window open