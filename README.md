# D-COM

**D-COM v4.77 — An Interactive Alternate Reality Game**

D-COM began as a small Python project intended to prank a friend into believing they had accessed the communications network of an interdimensional spacecraft.

This branch takes that concept further, developing it into a browser-based ARG centred around the Crystal Ship 065, its crew, and a series of events spanning multiple universes.

The experience combines a simulated spacecraft interface, command-based interactions, hidden information, and a branching narrative that unfolds as the player investigates the ship.

## The Experience

The browser interface simulates the control terminal of the Crystal Ship 065. Players begin with limited system access and gradually uncover additional information through commands, diagnostics and hidden authorization sequences.

The interface includes:

- **Ship Systems** — Access to spacecraft subsystems, initially restricted by authorization levels.
- **SPC Reactor** — Reactor temperature and power output monitoring and adjustment.
- **Drone Controls** — Reconnaissance, data collection, drone overrides and targeting.
- **Navisys** — Navigation and inter-universe route plotting.
- **TempoMod** — Time dilation controls and chronal field management.
- **Universe Logs** — Historical records containing coordinates, timestamps and information about alternate realities.
- **Telemetry** — Live spacecraft status and system readings.
- **Intercepted Traffic** — Incoming transmissions and communications.

## ARG

The interface serves as the foundation for a larger narrative. Hidden commands, authorization keys, diagnostic messages and recovered records gradually reveal the events surrounding the Crystal Ship.

The story develops through multiple chapters, involving:

- The Mirakilin Council
- VURG-0
- The Rupture
- The five universe records
- The sixth seat

Progression is tied to player actions and discoveries rather than simply reading through a predefined sequence.

The final chapter introduces the conclusion of the narrative and the resolution of the Rupture.

## Versions

| File | Description |
|---|---|
| `D-COM_v4_77_ARG.html` | Main interactive ARG experience, including the Council and Tribunal sequences. |
| `D-COM_v4_77_ARG_FINAL_CH6.html` | Extended build containing the final Chapter Six sequence and ending. |
| `D_Com_rep.py` | Python-based terminal interface and diagnostic entry point. |

## Installation & Usage

### Browser Experience

No installation or build process is required.

1. Clone the repository.
2. Open `D-COM_v4_77_ARG.html` in a modern web browser.
3. Interact with the terminal using the available commands.
4. Explore the interface and investigate the information you uncover.

The final Chapter Six build can be opened separately using `D-COM_v4_77_ARG_FINAL_CH6.html`.

### Python Terminal

The original terminal interface is also included.

Install the dependencies:

```bash
pip install colorama termcolor
```

Run the application:

```bash
python D_Com_rep.py
```

Alternatively, execute `main.bat` on Windows.

## Technical Details

| Component | Technology |
|---|---|
| Original terminal | Python |
| Web interface | HTML, CSS, JavaScript |
| Terminal styling | Colorama, Termcolor |
| Persistent progress | Browser Local Storage |
| Typography | IBM Plex Mono, Chakra Petch |
| Interface | Custom CSS and JavaScript |

The browser experience is self-contained and does not require a backend server. Player progression is stored locally in the browser.

## Project Structure

```text
D-COM/
│
├── D-COM_v4_77_ARG.html
├── D-COM_v4_77_ARG_FINAL_CH6.html
│
├── D_Com_rep.py
├── main.bat
│
├── Files/
│   ├── icon.ico
│   └── icon.jpg
│
├── dead_drop.txt
└── README.md
```

## Notes

D-COM is a fictional interactive experience. Spacecraft operations, network connections, universe navigation and system diagnostics are simulated. The application does not establish actual TOR connections or interact with external spacecraft or networks.

Browser progress is stored locally. Clearing browser storage may erase saved ARG progression.

---

**Venexs**  
D-COM v4.77
