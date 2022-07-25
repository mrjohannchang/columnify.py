# columnify

Inspired by [columnify](https://github.com/timoxley/columnify).

`columnify` creates text-based columnized (ls-like) content suitable for console output from list of strings.

Columns are automatically resized to fit the content of the largest cell. Each cell will be padded with spaces to fill the available space and ensure column contents are aligned.

**Table of Contents**

- [Examples](#examples)
- [Installation](#installation)
- [API](#api)
  - [Methods](#methods)
- [License](#license)

## Examples

```py
items: list[str] = [
    "Canidae", "Felidae", "Cat", "Cattle", "Dog",
    "Donkey", "Goat", "Guinea pig", "Horse", "Pig",
    "Rabbit", "Fancy rat varieties", "laboratory rat strains",
]
```

### Default

```text
Canidae  Cat     Dog     Goat        Horse  Rabbit               laboratory rat strains
Felidae  Cattle  Donkey  Guinea pig  Pig    Fancy rat varieties
```

### Horizon first

```text
Canidae     Felidae  Cat  Cattle  Dog                  Donkey                  Goat
Guinea pig  Horse    Pig  Rabbit  Fancy rat varieties  laboratory rat strains
```

### center()

```text
Canidae   Cat     Dog       Goat     Horse         Rabbit        laboratory rat strains
Felidae  Cattle  Donkey  Guinea pig   Pig   Fancy rat varieties
```

### rjust()

```text
Canidae     Cat     Dog        Goat  Horse               Rabbit  laboratory rat strains
Felidae  Cattle  Donkey  Guinea pig    Pig  Fancy rat varieties
```

### Custom delimiter ( | )

```text
Canidae | Cattle | Goat       | Pig                 | laboratory rat strains
Felidae | Dog    | Guinea pig | Rabbit
Cat     | Donkey | Horse      | Fancy rat varieties
```

### Indent (4 spaces):

```text
    Canidae  Cattle  Goat        Pig                  laboratory rat strains
    Felidae  Dog     Guinea pig  Rabbit
    Cat      Donkey  Horse       Fancy rat varieties
```

See `examples/example.py` for more information.

## Installation

```console
pip install columnify
```

## API

### Methods

```py
def columnify(
        items: list[str],
        line_width: int,
        indent: int = 0,
        delimiter: str = '  ',
        align_func_name: str = 'ljust',
        horizon_first: bool = False) -> str:
    ...
```

## License

`columnify` is distributed under the terms of the [MPL-2.0](https://spdx.org/licenses/MPL-2.0.html) license.
