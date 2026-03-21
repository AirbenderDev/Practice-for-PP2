# Practice 6 — Python File Handling, Directory Management & Built-in Functions

> **Source:** All examples are based on [W3Schools Python Tutorial](https://www.w3schools.com/python/)

---

## Project Structure

```
Practice6/
├── file_handling/
│   ├── read_files.py          # 5 examples of reading files
│   ├── write_files.py         # 5 examples of writing/creating files
│   └── copy_delete_files.py   # 5 examples of copying and deleting files
├── directory_management/
│   ├── create_list_dirs.py    # 5 examples of creating & listing directories
│   └── move_files.py          # 5 examples of moving & renaming files/dirs
├── builtin_functions/
│   ├── map_filter_reduce.py   # 5 examples each for map, filter, reduce
│   └── enumerate_zip_examples.py  # 5 examples each for enumerate and zip
└── README.md
```

---

## 1. File Handling

### `read_files.py`
| # | Concept | W3Schools Reference |
|---|---------|-------------------|
| 1 | `read()` — entire file content | [Python File Open](https://www.w3schools.com/python/python_file_open.asp) |
| 2 | `read(n)` — first n characters | [File read() Method](https://www.w3schools.com/python/ref_file_read.asp) |
| 3 | `readline()` — one line at a time | [File readline() Method](https://www.w3schools.com/python/ref_file_readline.asp) |
| 4 | `readlines()` — all lines as a list | [Python File Open](https://www.w3schools.com/python/python_file_open.asp) |
| 5 | `with` statement (best practice) | [Python File Open](https://www.w3schools.com/python/python_file_open.asp) |

### `write_files.py`
| # | Concept | W3Schools Reference |
|---|---------|-------------------|
| 1 | `"w"` mode — overwrite | [Python File Write](https://www.w3schools.com/python/python_file_write.asp) |
| 2 | `"a"` mode — append | [Python File Write](https://www.w3schools.com/python/python_file_write.asp) |
| 3 | `"x"` mode — create new file | [Python File Write](https://www.w3schools.com/python/python_file_write.asp) |
| 4 | `writelines()` — write a list | [File writelines() Method](https://www.w3schools.com/python/ref_file_writelines.asp) |
| 5 | Overwrite existing content | [Python File Write](https://www.w3schools.com/python/python_file_write.asp) |

### `copy_delete_files.py`
| # | Concept | W3Schools Reference |
|---|---------|-------------------|
| 1 | `os.remove()` — delete a file | [Python Delete Files](https://www.w3schools.com/python/python_file_remove.asp) |
| 2 | `os.path.exists()` — safe delete | [Python Delete Files](https://www.w3schools.com/python/python_file_remove.asp) |
| 3 | `shutil.copy()` — copy a file | [Python shutil Module](https://www.w3schools.com/python/module_shutil.asp) |
| 4 | Copy and rename simultaneously | [Python shutil Module](https://www.w3schools.com/python/module_shutil.asp) |
| 5 | Copy + delete (manual move) | [Python Delete Files](https://www.w3schools.com/python/python_file_remove.asp) |

---

## 2. Directory Management

### `create_list_dirs.py`
| # | Concept | W3Schools Reference |
|---|---------|-------------------|
| 1 | `os.mkdir()` — create one directory | [Python os Module](https://www.w3schools.com/python/module_os.asp) |
| 2 | `os.makedirs()` — nested directories | [Python os Module](https://www.w3schools.com/python/module_os.asp) |
| 3 | `os.listdir()` — list contents | [Python os Module](https://www.w3schools.com/python/module_os.asp) |
| 4 | `os.getcwd()` — current directory | [Python os Module](https://www.w3schools.com/python/module_os.asp) |
| 5 | Filter only files with `os.path.isfile()` | [Python os Module](https://www.w3schools.com/python/module_os.asp) |

### `move_files.py`
| # | Concept | W3Schools Reference |
|---|---------|-------------------|
| 1 | `os.rename()` — rename a file | [Python os Module](https://www.w3schools.com/python/module_os.asp) |
| 2 | `shutil.move()` — move to folder | [Python shutil Module](https://www.w3schools.com/python/module_shutil.asp) |
| 3 | Move + rename in one step | [Python shutil Module](https://www.w3schools.com/python/module_shutil.asp) |
| 4 | Rename a directory | [Python os Module](https://www.w3schools.com/python/module_os.asp) |
| 5 | Move an entire directory | [Python shutil Module](https://www.w3schools.com/python/module_shutil.asp) |

---

## 3. Built-in Functions

### `map_filter_reduce.py`

**map()** — applies a function to every element in an iterable.
| # | Example |
|---|---------|
| 1 | Square all numbers |
| 2 | Convert strings to uppercase |
| 3 | Celsius → Fahrenheit |
| 4 | Get string lengths |
| 5 | Add elements from two lists |

**filter()** — keeps elements where the function returns `True`.
| # | Example |
|---|---------|
| 1 | Keep even numbers |
| 2 | Keep positive numbers |
| 3 | Strings longer than 4 characters |
| 4 | Remove falsy values (None, 0, '') |
| 5 | Words starting with a vowel |

**reduce()** — accumulates elements into a single result (from `functools`).
| # | Example |
|---|---------|
| 1 | Sum all numbers |
| 2 | Find maximum value |
| 3 | Product of all numbers |
| 4 | Concatenate strings |
| 5 | Total character count |

> References: [map()](https://www.w3schools.com/python/ref_func_map.asp) · [filter()](https://www.w3schools.com/python/ref_func_filter.asp) · [reduce()](https://www.w3schools.com/python/ref_func_reduce.asp)

---

### `enumerate_zip_examples.py`

**enumerate()** — adds an index counter to any iterable.
| # | Example |
|---|---------|
| 1 | Basic index + value loop |
| 2 | Start counter from 1 |
| 3 | Numbered lines (like a file reader) |
| 4 | Find the index of a specific value |
| 5 | Build a numbered dictionary |

**zip()** — pairs elements from multiple iterables into tuples.
| # | Example |
|---|---------|
| 1 | Pair names with scores |
| 2 | Zip three lists together |
| 3 | Build a dictionary from two lists |
| 4 | Element-wise addition |
| 5 | Unzip (transpose) with `zip(*...)` |

> References: [enumerate()](https://www.w3schools.com/python/ref_func_enumerate.asp) · [zip()](https://www.w3schools.com/python/ref_func_zip.asp)

---

## Quick Reference — File Open Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read (default). Error if file doesn't exist. |
| `"w"` | Write. Creates file if absent; overwrites if present. |
| `"a"` | Append. Creates file if absent; adds to end if present. |
| `"x"` | Create. Error if file already exists. |

---

*All content sourced from [W3Schools Python Tutorial](https://www.w3schools.com/python/) — Copyright 1999-2026 Refsnes Data.*
