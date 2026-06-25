"""
Play a .wav sound file using Python's built-in winsound module (Windows).
"""

import winsound
import os
import sys


def play_wav(file_path: str) -> None:
    """Play a WAV file using winsound (Windows only).

    Args:
        file_path: Path to the .wav file.

    Raises:
        FileNotFoundError: If the file does not exist.
        RuntimeError: If playback fails.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    print(f"Playing: {file_path}")
    # SND_FILENAME | SND_NOWAIT | SND_ASYNC = play asynchronously
    # Use SND_SYNC (the default) for blocking playback
    winsound.PlaySound(file_path, winsound.SND_FILENAME)
    print("Done.")


def main() -> None:
    args = sys.argv[1:]

    if args:
        # Use the first CLI argument as the file path
        file_path = args[0]
    else:
        # Default to the Alarm01.wav bundled with this project
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "sounds", "Alarm01.wav")

    try:
        play_wav(file_path)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Playback error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
