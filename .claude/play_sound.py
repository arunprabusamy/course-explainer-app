import sys
import os

# Try using winsound (built-in on Windows, no installation needed)
try:
    import winsound
    sound_path = os.path.join(os.path.dirname(__file__), 'sounds', 'notification.mp3')

    # winsound only works with WAV files, so we'll use an alternative
    # Use Windows API to play sound without visible player
    import subprocess

    # This PowerShell command plays sound without opening Windows Media Player window
    ps_command = f'''
    Add-Type -AssemblyName presentationCore
    $mediaPlayer = New-Object System.Windows.Media.MediaPlayer
    $mediaPlayer.Open([uri]::new("{sound_path}"))
    $mediaPlayer.Play()
    Start-Sleep -Milliseconds 1500
    $mediaPlayer.Close()
    '''

    subprocess.run(['powershell', '-WindowStyle', 'Hidden', '-Command', ps_command],
                   creationflags=subprocess.CREATE_NO_WINDOW)
except Exception as e:
    # Silently fail if there's an issue
    pass
