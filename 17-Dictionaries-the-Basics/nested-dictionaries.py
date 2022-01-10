tv_shows = {
    "The X-Files": {
        "Season 1": {
            "Episodes": ["Pilot", "Squeeze"],
            "Genre": "Science Fiction",
            "Year": 1993
        },
        "Season 2": {
            "Episodes": ["The Host", "Firewalker"],
            "Genre": "Horror",
            "Year": 1994
        }
    },
    "Lost": {
        "Season 1": {
            "Episodes": ["The Moth", "Hearts and Minds"],
            "Genre": "Science Fiction",
            "Year": 2004
        }
    }
}

print(tv_shows)

print()

print(tv_shows["The X-Files"]["Season 1"]["Episodes"][1])
print(tv_shows["The X-Files"]["Season 2"]["Year"])
print(tv_shows["Lost"]["Season 1"]["Genre"])