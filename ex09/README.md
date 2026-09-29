# ft_package

A sample Python package created for the 42 Python Data Science Piscine.

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

if u want to revalidate the ex09

From the project root:

```bash
cd ex09
python3 -m pip install build
python3 -m build
```

This must create:

```text
dist/ft_package-0.0.1.tar.gz
dist/ft_package-0.0.1-py3-none-any.whl
```

Install the wheel:

```bash
python3 -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Verify the package:

```bash
pip show -v ft_package
```

Then run:

```bash
python3 -c "from ft_package import count_in_list; print(count_in_list(['toto', 'tata', 'toto'], 'toto')); print(count_in_list(['toto', 'tata', 'toto'], 'tutu'))"
```

Expected output:

```text
2
0
```
