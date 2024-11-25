# Hangman CLI

A CLI-based word-guessing game, a classic known as Hangman.

## Features

- 500 words for offline play.
- Millions of words for online play.
- Multiple characters to choose from.
- Multiple difficulty levels.

## Libraries Used

- `pyfiglet`
- `requests`

**Use `requirements.txt` to download libraries**  
Command:
```pip install -r requirements.txt```

## Build Executable Using PyInstaller

### Linux

```pyinstaller --onefile -n hangman src/main.py --icon assets/icon.ico --add-data "{PATH_TO_YOUR_GITHUB_DIR.}/RhombixTechnologies_Tasks/hangman-game/lib/python3.12/site-packages/pyfiglet/fonts:pyfiglet/fonts" --add-data "{PATH_TO_YOUR_GITHUB_DIR}/RhombixTechnologies_Tasks/hangman-game/src/utils/data:data";```

### Windows

## Screenshots

![main](screenshots/main-screen.png)

**[more](screenshots/)**

