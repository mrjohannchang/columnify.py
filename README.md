# columnify

[![PyPI - Version](https://img.shields.io/pypi/v/columnify.svg)](https://pypi.org/project/columnify)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/columnify.svg)](https://pypi.org/project/columnify)

-----

`columnify` creates text-based columnified (ls-like) content suitable for console output from list of strings.

Columns are automatically resized to fit the content of the largest cell. Each cell will be padded with spaces to fill the available space and ensure column contents are left-aligned.

**Table of Contents**

- [Quick Start](#quick-start)
- [Installation](#installation)
- [API](#api)
  - [Methods](#methods)
- [License](#license)

## Usage

### Default

```py
import shutil

import columnify


given: list[str] = [
  "Canidae",
  "Felidae",
  "Cat",
  "Cattle",
  "Dog",
  "Donkey",
  "Goat",
  "Guinea pig",
  "Horse",
  "Pig",
  "Rabbit",
  "Fancy rat varieties",
  "laboratory rat strains",
]

output: str = columnify.columnify(given, shutil.get_terminal_size().columns)

print(output)
```

#### Output

```
Canidae  Cat     Dog     Goat        Horse  Rabbit               laboratory rat strains
Felidae  Cattle  Donkey  Guinea pig  Pig    Fancy rat varieties
```

### Horizon first

```py
print(columnify.columnify(given, shutil.get_terminal_size().columns), horizon_first=True)
```

#### Output

```
Canidae     Felidae  Cat  Cattle  Dog                  Donkey                  Goat
Guinea pig  Horse    Pig  Rabbit  Fancy rat varieties  laboratory rat strains
```

## Installation

```console
pip install columnify
```

## API

### Methods

```py
columnify(
    items: list[str],
    line_width: int,
    indent: int = 0,
    delimiter: str = '  ',
    horizon_first: bool = False) -> str
```

## License

`columnify` is distributed under the terms of the [MPL-2.0](https://spdx.org/licenses/MPL-2.0.html) license.
