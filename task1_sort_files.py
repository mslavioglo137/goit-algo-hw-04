import argparse
import shutil
import sys
from pathlib import Path

stats = {
    "directories": 0,
    "files": 0,
    "duplicates": 0,
    "errors": 0,
}


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Recursively copy and sort files by extension."
    )

    parser.add_argument(
        "source",
        type=Path,
        nargs="?",
        help="Source directory",
    )

    parser.add_argument(
        "destination",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Destination directory (default: dist)",
    )

    return parser.parse_args()


def interactive_mode():
    """Run interactive mode if no arguments were provided."""

    print("=" * 50)
    print("           Recursive File Sorter")
    print("=" * 50)

    while True:

        print("\nSelect the source directory:")
        print("1 - Current directory")
        print("2 - Home directory")
        print("3 - Enter custom path")

        choice = input("\nYour choice: ").strip()

        if choice == "1":
            source = Path.cwd()
            break

        elif choice == "2":
            source = Path.home()
            break

        elif choice == "3":
            source = Path(
                input("Enter source directory: ").strip()
            ).expanduser()

            if source.exists() and source.is_dir():
                break

            print(f"\nDirectory not found:\n{source}")

        else:
            print("Invalid choice. Please try again.")

    destination = input(
        "\nEnter destination directory "
        "(press Enter for 'dist'): "
    ).strip()

    destination = (
        Path("dist")
        if not destination
        else Path(destination).expanduser()
    )

    if destination.exists() and destination.is_file():
        print("\nDestination path points to a file.")
        sys.exit()

    if source.resolve() == destination.resolve():
        print("\nSource and destination directories cannot be the same.")
        sys.exit()

    print("\nSelected directories")
    print(f"Source      : {source}")
    print(f"Destination : {destination}")

    confirm = input("\nContinue? (Y/n): ").strip().lower()

    if confirm in {"n", "no"}:
        print("Operation cancelled.")
        sys.exit()

    return source, destination


def copy_file(file_path: Path, destination_root: Path):
    """Copy a file into a directory based on its extension."""

    extension = file_path.suffix.lower().lstrip(".")

    if not extension:
        extension = "no_extension"

    destination_dir = destination_root / extension
    destination_dir.mkdir(parents=True, exist_ok=True)

    destination_file = destination_dir / file_path.name

    if destination_file.exists():
        stats["duplicates"] += 1
        print(f"Skipped duplicate: {destination_dir.name}/{file_path.name}")
        return

    shutil.copy2(file_path, destination_file)

    stats["files"] += 1

    print(f"Copied: {file_path.name} -> {destination_dir.name}/")


def process_directory(source_dir: Path, destination_root: Path):
    """Recursively process a directory."""

    stats["directories"] += 1

    try:
        for item in source_dir.iterdir():

            if item.is_dir():
                process_directory(item, destination_root)

            elif item.is_file():
                copy_file(item, destination_root)

    except PermissionError:
        stats["errors"] += 1
        print(f"Permission denied: {source_dir}")

    except OSError as error:
        stats["errors"] += 1
        print(f"Error processing {source_dir}: {error}")


def main():

    args = parse_arguments()

    if args.source:
        source_dir = args.source.expanduser()
        destination_dir = args.destination.expanduser()
    else:
        source_dir, destination_dir = interactive_mode()

    if not source_dir.exists():
        print("Source directory does not exist.")
        return

    if not source_dir.is_dir():
        print("The specified source path is not a directory.")
        return

    destination_dir.mkdir(parents=True, exist_ok=True)

    process_directory(source_dir, destination_dir)

    print("\n" + "=" * 50)
    print("Sorting completed successfully.")
    print("=" * 50)
    print(f"Directories scanned : {stats['directories']}")
    print(f"Files copied        : {stats['files']}")
    print(f"Duplicates skipped  : {stats['duplicates']}")
    print(f"Errors              : {stats['errors']}")
    print(f"Destination         : {destination_dir}")
    print("=" * 50)


if __name__ == "__main__":
    main()