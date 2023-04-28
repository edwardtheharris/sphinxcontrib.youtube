---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: .venv
  language: python
  name: python3
---

# Semver

This notebook allows versioning of the code in this repository.

```{code-cell} ipython3
from pathlib import Path
import semver

with Path('version').open('r', encoding='utf-8') as v_fh:
    current_version=semver.Version.parse(v_fh.read())

current_version
```

```{code-cell} ipython3
current_version=current_version.bump_patch()
current_version
```

```{code-cell} ipython3
# with Path('version').open('w', encoding='utf-8') as v_fh:
#     v_fh.write(str(current_version))
```

```{code-cell} ipython3

```
