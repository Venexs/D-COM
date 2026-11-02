# D-COM

A fictional communications network simulator built in Python.

D-COM was created as a prank, designed to make it appear as though the user has intercepted a communications channel belonging to a spacecraft travelling between universes.

The application runs through a command-line interface, simulating system initialization, network connections, restricted access, ship controls and intercepted communications.

## Features

- **System Initialization** — Simulated connection establishment, authentication and startup sequences.
- **Ship Control Interface** — Access to different spacecraft subsystems.
- **Drone Controls** — Simulated drone discovery, reconnaissance and data collection.
- **SPC Reactor Systems** — Reactor diagnostics and adjustable temperature and power output.
- **Universe Logs** — Records of spacecraft activity across different universes, including timestamps, coordinates and intercepted entries.
- **Intercepted Communications** — Simulated communications with unidentified vessels and fleets.
- **Terminal Effects** — Coloured output, typing animations and timed sequences for a more convincing interface.

## Technology

- Python
- Colorama
- Termcolor

## Installation

Requires Python and pip.

Clone the repository:

```bash
git clone https://github.com/Venexs/D-COM.git
cd D-COM
```

Install the dependencies:

```bash
pip install colorama termcolor
```

## Usage

Run the included batch file:

```bat
main.bat
```

Alternatively:

```bash
python D_Com_rep.py
```

### Connection Modes

The `on` variable in `D_Com_rep.py` controls the startup sequence.

| Value | Behaviour |
|---|---|
| `1` | Establishes a connection and opens the ship control interface. |
| `2` | Simulates repeated failed connection attempts. |
| `3` | Simulates an incoming connection from an unidentified fleet. |
| Other | Displays a connection failure. |

## Project Structure

```text
D-COM/
│
├── D_Com_rep.py    # Main application
├── main.bat        # Windows launcher
├── README.md
│
└── New folder/
    ├── icon.ico
    └── icon.jpg
```

## Notes

D-COM is an entirely fictional simulation. It does not establish actual TOR connections, communicate with spacecraft, control drones or interact with external networks. All displayed system information and operations are simulated locally.

The project was originally created as a prank, with the possibility of developing it further into an analog horror experience.

