#10. Longest Streak

#Take a string with only A and B. ()
#Print the length of the longest consecutive streak of the same letter.
#(e.g. "AABBBBAAAAABBB" → longest is BBBB = 4)




















s = input("Enter a string of A and B: ")
max_streak = 1
current_streak = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 1

print("Longest streak:", max_streak)