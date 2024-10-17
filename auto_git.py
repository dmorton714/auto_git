import subprocess


def run_git_command(command):
    """Run a git command using subprocess."""
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout


def main():
    # Step 1: Check for changes using git status
    status_output = run_git_command(['git', 'status', '--porcelain'])

    if not status_output.strip():
        print("No changes to commit.")
    else:
        # Step 2: Add changes with git add .
        print("Changes detected. Adding changes...")
        run_git_command(['git', 'add', '.'])

        # Step 3: Prompt for a commit message
        commit_message = input("Enter your commit message: ")

        # Step 4: Commit the changes
        run_git_command(['git', 'commit', '-m', commit_message])
        print(f"Committed with message: '{commit_message}'")

        # Step 5: Push the changes
        push_output = run_git_command(['git', 'push'])
        print(push_output)


if __name__ == "__main__":
    main()
