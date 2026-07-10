# Unzip_Tool

A small Python utility for extracting a `.zip` (or tar) archive and recursively
unpacking any nested archives it contains. Given a folder and an archive name, it
extracts into a sibling `Unzipped/<archive_name>/` directory, then walks the result
and unzips any further `.zip` files it finds. Handy for downloads that arrive as
archives-within-archives.

One-off personal utility, not maintained or packaged.

## Contents

- `Unzip_Tool.py` — a single module with:
  - `unzip_file(file_path, output_path)` — extracts one `.zip` (via `zipfile`) or tar
    archive (via `tarfile`) to `output_path`.
  - `Unzip_class(path, file)` — extracts `path/file` into `path/Unzipped/<name>/`,
    creating the folder if needed, then recursively unpacks nested zips.
  - `down_folder(path)` — recursion helper that walks a directory and unzips any zips.

## Requirements

Python 3, standard library only (`zipfile`, `tarfile`, `os`).

## Usage

    from Unzip_Tool import Unzip_class

    path = r"C:\Users\bmanderson\Downloads"
    file = "coi_disclosure.zip"
    Unzip_class(path=path, file=file)

Output is written to `path/Unzipped/coi_disclosure/`.
