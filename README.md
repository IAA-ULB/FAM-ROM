This repository can be used to create an emulator for QRPA linear response. The emulator applies reduced order modelling to approximate from previous FAM amplitudes. 
Related DOI: TBA

---
 The repository is structured as follows:
```text
FAM-ROM/
├── docs/
├── src/
│   ├── __init__.py
│   ├── ROM_basis.py
│   └── Utils.py
├── .gitignore
├── LICENSE.md
├── mkdocs.yml
├── requirements.txt
├── README.md
└── script.py
```
The user is expected to provide the FAM outputs and a parser to extract the following quantities:
- $n_s$ FAM frequencies, parsed into a vector of length $n_s$
- FAM amplitudes, parsed into a matrix of shape $(n_s, 2, m)$, ordered according to the $n_s$ frequencies, where $X$ and $Y$ stacked along the second dimension and $m$ is the number of matrix elements.
- External field matrix elements, parsed into a vector of shape $(2m)$, with the first half corresponding to $F^{20}$ and the second half corresponding to $F^{02}$.

After initialisation of the basis using
```python
from src.ROM_basis import ROM_basis
import parser # user-defined parser
basis = ROM_basis()
omegas, matrices, F = parser.parse(data)
basis.load(omegas=omegas, snapshots=matrices, F=F)
```
the repository can be used for the following tasks:
- Offline: Building the emulator by finding a single new snapshot location
```python
basis.next_snapshot()
```
- Online: Evaluating the emulator to obtain the strength at new frequencies
```python
targets = np.linspace(0, 40, 2000)+1.0j
basis.evaluate(targets)
```

## Installation
```bash
git clone https://github.com/IAA-ULB/FAM-ROM.git
cd ./FAM-ROM/
python3 -m venv .venv
source .venv/bin/activate 
python3 -m pip install -r requirements.txt
```
## Documentation
The documentation can be opened by running the following command in the root directory of the repository:
```bash
mkdocs serve
```
