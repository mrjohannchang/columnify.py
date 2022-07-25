# SPDX-FileCopyrightText: 2022 Johann Chang <mr.changyuheng@gmail.com>
#
# SPDX-License-Identifier: MPL-2.0

import math
import os


def columnify(
        items: list[str],
        line_width: int,
        indent: int = 0,
        delimiter: str = '  ',
        align_func_name: str = 'ljust',
        horizon_first: bool = False) -> str:
    if align_func_name not in ('ljust', 'center', 'rjust'):
        raise ValueError('alignment must be one of these options: ljust, center, rjust')

    res: str = ''

    if not items:
        return res

    width: int = line_width - len(os.linesep) - indent

    if horizon_first:
        num_column: int = math.ceil(width + len(delimiter) / (min(map(len, items)) + len(delimiter)))
        column_widths: list[int] = [min(map(len, items)) for _ in range(num_column)]
        while num_column > 0:
            r: int
            for r in range(math.ceil(len(items) / num_column)):
                c: int
                for c in range(num_column):
                    if r * num_column + c >= len(items):
                        continue
                    if len(items[r * num_column + c]) <= column_widths[c]:
                        continue
                    column_widths[c] = len(items[r * num_column + c])
                    if sum(column_widths) + len(delimiter) * (num_column - 1) <= width:
                        continue
                    num_column -= 1
                    column_widths = [min(map(len, items)) for _ in range(num_column)]
                    break
                else:
                    continue
                break
            else:
                break

        if num_column > 0:
            i: int
            for i in range(0, len(items), num_column):
                line: str = ' ' * indent
                x: tuple[int, str]
                line += delimiter.join(
                    map(lambda x: getattr(x[1], align_func_name)(column_widths[x[0]]),
                        enumerate(items[i:i + num_column])))
                line += os.linesep
                res += line
            res = res.rstrip(os.linesep)
    else:
        num_column: int = 2
        column_widths: list[int] = [0] * num_column
        rows: list[list[str]] = list()
        while True:
            group_size: int = math.ceil(len(items) / num_column)
            tmp_column_widths: list[int] = [0] * num_column
            c: int
            for c in range(num_column):
                if items[group_size * c:group_size * (c + 1)]:
                    x: str
                    tmp_column_widths[c] = len(max(items[group_size * c:group_size * (c + 1)], key=lambda x: len(x)))
            if sum(tmp_column_widths) + len(delimiter) * (num_column - 1) > width:
                break
            column_widths = tmp_column_widths
            rows = list()
            r: int
            for r in range(group_size):
                row: list[str] = list()
                for c in range(num_column):
                    if r < len(items[group_size * c:group_size * (c + 1)]):
                        row.append(items[group_size * c:group_size * (c + 1)][r])
                rows.append(row)
            num_column += 1
        c: int
        item: str
        res = os.linesep.join(' ' * indent + delimiter.join(
            getattr(item, align_func_name)(column_widths[c]) for c, item in enumerate(row)) for row in rows)

    if not res:
        res = ' ' * indent + f'{os.linesep}{" " * indent}'.join(items)

    return res
