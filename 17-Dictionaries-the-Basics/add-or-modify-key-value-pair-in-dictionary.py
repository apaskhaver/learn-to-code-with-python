sports_team_roster = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New York Giants": ["Eli Manning", "Odell Beckham"]
}

sports_team_roster["Pittsburgh Steelers"] = ["Ben Roethlisberger", "Antonio Brown"]

print(sports_team_roster["Pittsburgh Steelers"])

print()

print(sports_team_roster)

print()

sports_team_roster["New York Giants"] = ["Eli Manning"]
print(sports_team_roster["New York Giants"])

print()

video_game_options = {}
# video_game_options = dict()

video_game_options["subtitles"] = True
video_game_options["difficulty"] = "Medium"
video_game_options["volume"] = 7

print(video_game_options)

video_game_options["subtitles"] = False
video_game_options["difficulty"] = "Hard"

print(video_game_options)

video_game_options["Volume"] = 10 # case sensitivity matters
print(video_game_options)


print()
print()
print()

words = ["danger", "beware", "danger", "beware", "beware", "attention"]

def count_words(words):
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words(words))