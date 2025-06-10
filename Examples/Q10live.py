userin = input("Enter a string of ONLY A and B: ")

# Step 1: Validate input
valid = True
for ch in userin:
    if ch != 'A' and ch != 'B':
        valid = False
        break

if not valid:
    print("Invalid input! Please use only A and B.")
else:
    print("Valid input.")

    # Step 2: Track streaks
    count_a = 0
    count_b = 0
    max_streak = 0
    streak_char = ''  # store the letter that had the longest streak

    for ch in userin:
        if ch == "A":
            count_a += 1
            count_b = 0  # reset B streak
            if count_a > max_streak:
                max_streak = count_a
                streak_char = 'A'
        elif ch == "B":
            count_b += 1
            count_a = 0  # reset A streak
            if count_b > max_streak:
                max_streak = count_b
                streak_char = 'B'

    print("Longest streak length:", max_streak)
    print("Streak:", streak_char * max_streak)