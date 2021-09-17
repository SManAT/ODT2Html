# ODT2Html

Converts ODT Files into Html Files, only for WIN Systems

## Needs Unoconv

1. Download from https://github.com/unoconv/unoconv
   File unoconv
2. Rename to unoconv.py
3. On Windows start the process like
   C:\"Program Files"\LibreOffice\program\python.exe <full path>unoconv.py -f pdf <full path>TestFile.odt

# Configuration

You configure the behavor in `config.yaml`

```yaml
# where to find LibreOffice, will be detected automatically
# will search for LO in "C:\Program Files", "C:\Program Files (x86)"
LOPath: C:\"Program Files"\LibreOff.....
```
