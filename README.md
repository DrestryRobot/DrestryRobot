# DrestryRobot

A robot-development knowledge base, written as a Sphinx book and published on
Read the Docs: <https://drestryrobot.readthedocs.io>

The site has two parts: a documentation body (technical notes and tool manuals)
and an index page that doubles as a project portfolio / CV attachment, where
each project is illustrated with a demo video.

## What is inside

| Section | Source folder | Content |
| --- | --- | --- |
| Techniques (技术) | `docs/source/技术/` | 12 notes on control, hardware, algorithms and communication |
| Tools (工具) | `docs/source/工具/` | 19 notes on CAD, simulation, visualisation and IDE tooling |
| Index / portfolio | `docs/source/index.rst` | Project experience, internship and competition results, each with demo videos |

### Techniques (`docs/source/技术/`)

| Topic group | Notes |
| --- | --- |
| Control (`控制 …`) | PID control, dual-loop PID, admittance control, pneumatic control |
| Hardware (`硬件 …`) | Photoelectric switch, optocoupler relay, electric push rod, step-down module |
| Programming (`程序 …`) | `.h` header files |
| Algorithms (`算法 …`) | Gravity compensation |
| Communication (`通信 …`) | CAN bus, serial port |

### Tools (`docs/source/工具/`)

| Tool | Notes |
| --- | --- |
| DELMIA | Getting started, mechanisms, path simulation, gantry-mounted robot, VBA integration |
| SolidWorks | Getting started, installation guide, sketching, moving the origin, fluid simulation, warning cleanup |
| Unity | Getting started, digital twin, data dashboard |
| VisionMaster | UTF-8 encoding problems, byte-related errors |
| Other | Qt, OpenGL data visualisation, VS Code |

## Writing principles

The rules the notes are written by (originally stated in `README.rst`):

- no images, no links, no external resources;
- content should have depth, and existing wheels should not be reinvented;
- hit the point — every note should read as a summary;
- writing matters more than reading;
- everything revolves around robotics;
- code is generally avoided, but formulas are expected;
- only write about what a general reader does not already know;
- do not write about topics you only half understand.

## Repository layout

| Path | Purpose |
| --- | --- |
| `docs/source/conf.py` | Sphinx configuration (project metadata, extensions, RTD theme) |
| `docs/source/index.rst` | Landing page: portfolio, experience and video showcase |
| `docs/source/技术.rst`, `docs/source/工具.rst` | Section pages; both use a `:glob:` toctree over their folder |
| `docs/source/技术/`, `docs/source/工具/` | The actual notes, one RST file per topic |
| `docs/source/_ext/video_links.py` | Custom `video` directive resolving video objects through the URL manifest |
| `export_urls.csv` | Manifest mapping video object names to remote (Aliyun OSS) URLs |
| `docs/requirements.txt` | Sphinx, RTD theme and copybutton versions |
| `docs/Makefile`, `docs/make.bat` | Standard Sphinx build entry points |
| `.readthedocs.yaml` | Read the Docs build configuration |

## Videos

Video files are not stored in the repository. Each one lives on Aliyun OSS and
is referenced by object name:

```rst
.. video:: 202503 导纳控制.mp4
```

The `video` directive added by `docs/source/_ext/video_links.py` looks the name
up in `export_urls.csv` (a two-column `object,url` manifest, read as
UTF-8-with-BOM), then renders a responsive 16:9 HTML5 player with
`object-fit: contain`, so every clip keeps its aspect ratio and nothing is
cropped.

Two things are worth knowing when adding a video:

- the object name in the RST file must match the `object` column — either the
  full entry or a file name that is unique in the manifest;
- when a name is missing or ambiguous, the build logs a warning and the
  directive source is rendered instead of a player.

## Building the documentation locally

```
python -m venv .venv
.venv\Scripts\activate
pip install -r docs/requirements.txt
sphinx-build -b html docs/source docs/build/html
```

`docs\make.bat html` does the same thing through the provided Makefile. Read the
generated site from `docs/build/html/index.html`.

The documentation is written in Chinese, so every `.rst` file must be saved as
UTF-8; a wrong encoding shows up as garbled text in the built page rather than
as a build error.

## Notes

- The build environment is pinned in `.readthedocs.yaml`: Ubuntu 22.04,
  Python 3.10, `docs/requirements.txt` and `docs/source/conf.py`.
- `pyproject.toml` still carries package metadata from the Read the Docs
  tutorial template; this repository only publishes documentation.
- `README.rst` is kept as the original README of the project.

## License

No license file is present in this repository. Contact the repository owner for
licensing terms.
