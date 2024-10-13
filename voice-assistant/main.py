from src.commands import Commands

if __name__ == "__main__":
    command = Commands()
    try:
        command.commands()
    except KeyboardInterrupt:
        print("\nProgram closed by User.")
    