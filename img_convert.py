from PIL import Image
from pathlib import Path
import argparse

def check_dir(from_dir, to_dir):
    from_path = Path(from_dir)
    to_path = Path(to_dir)
    if not from_path.exists():
        print(f"From Dir {from_path} not exists")
        raise SystemExit(1)
    if not to_path.exists():
        print("Target Dir not exists")
        to_path.mkdir(parents=True, exist_ok=True)
        print("Created Target Dir:", to_path.resolve())
    
    return from_path, to_path

def convert(from_dir, to_dir, from_ext, to_ext):
    input_ext = '.'+from_ext
    output_ext = '.'+to_ext

    from_path, to_path = check_dir(from_dir, to_dir)

    for file_path in from_path.iterdir():
        if file_path.suffix == input_ext:
            output_file_path = to_path / file_path.name.replace(input_ext, output_ext)
            with Image.open(file_path) as img:
                img.save(output_file_path, to_ext.upper())
                print(f"Converted: {file_path.name} -> {output_file_path.name}")
    


parser = argparse.ArgumentParser(description="Convert image to image but different!")
parser.add_argument("from_ext", type=str, help="Extension of original images (E.g. tif)")
parser.add_argument("to_ext", type=str, help="Extension of target images (E.g png)")
parser.add_argument("from_dir", type=str, help="Directory of original images")
parser.add_argument("to_dir", type=str, help="Directory for target images")
args = parser.parse_args()
    
convert(args.from_dir, args.to_dir, args.from_ext, args.to_ext)