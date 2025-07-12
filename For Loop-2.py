total_jumping_jacks = 100
set_size = 10
completed = 0

while completed < total_jumping_jacks:
    print(f"\nDo {set_size} jumping jacks!")
    completed += set_size

    if completed >= total_jumping_jacks:
        print("\nCongratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").strip().lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"\nYou completed a total of {completed} jumping jacks.")
            break
        else:
            remaining = total_jumping_jacks - completed
            print(f"{remaining} jumping jacks remaining.")
    elif tired in ["no", "n"]:
        remaining = total_jumping_jacks - completed
        print(f"{remaining} jumping jacks remaining.")
    else:
        print("Invalid input, assuming you're not tired. Continuing...")
        remaining = total_jumping_jacks - completed
        print(f"{remaining} jumping jacks remaining.")
