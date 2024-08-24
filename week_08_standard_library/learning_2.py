from pathlib import Path
from zipfile import ZipFile

zip = ZipFile("files.zip","w")

for path in Path("modules").rglob("*.*"):
  zip.write(path)

zip.close()