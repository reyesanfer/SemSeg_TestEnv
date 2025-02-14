import os
import subprocess
from tqdm import tqdm
import argparse as argparse

def buildingArguments() -> argparse.Namespace:
    """
        Builds the command-line argument parser.

        Returns:
            argparse.Namespace: Parsed command-line arguments from the user input.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('inputdata', type=str, 
                        help='Directory with the image(s) you want to use for testing or image file')
    parser.add_argument('config_engine', type=str, help='Config file')
    parser.add_argument('checkpoint', type=str, default=None, help='Checkpoint file')
    parser.add_argument('outputdata', type=str,  
        help='Directory where you want to save the testing result image(s) or image file to be saved')
    parser.add_argument('--with-labels', type=bool, default=False, help='The segmented images will be saved on a grey scale')
    return parser.parse_args()

def main():
    args = buildingArguments()
    if not os.path.exists(args.inputdata):
        raise ValueError(f"The input directory does not exist: {args.inputdata}")
    os.makedirs(args.outputdata, exist_ok=True)
    imgs = os.listdir(args.inputdata)
    progress_bar = tqdm(total=len(imgs), desc="Segmenting images", unit="images", bar_format="{desc}: {percentage:.2f}%|{bar}| {n_fmt}/{total_fmt} [{remaining} remaining]", dynamic_ncols=True)
    for img in imgs:
        img_name = os.path.join(args.outputdata, f"result-{img}")
        if args.with_labels:
            subprocess.run(["python", "-W", "ignore", "/mmsegmentation/demo/image_demo.py", img, args.config_engine, args.checkpoint, "--out-file", img_name, "--with-labels"], text=True)
        else:
            subprocess.run(["python", "-W", "ignore", "/mmsegmentation/demo/image_demo.py", img, args.config_engine, args.checkpoint, "--out-file", img_name], text=True)
        progress_bar.update(1)
    progress_bar.close()

if __name__ == '__main__':
    main()