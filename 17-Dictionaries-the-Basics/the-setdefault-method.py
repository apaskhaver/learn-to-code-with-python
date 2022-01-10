film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese"
}

print(film_directors.get("Goodfellas"))
print(film_directors.get("Bad Boys"))
print(film_directors.get("Bad Boys", "Michael Bay")) # does not modify film_directors

print()

print(film_directors.setdefault("The Godfather"))
print(film_directors.setdefault("Bad Boys", "Michael Bay")) # modifies film_directors, returns None
print(film_directors)

print()

print(film_directors.setdefault("Bad Boys", "A good director")) 
# doesn't change value because the key exists, prints 'Michael Bay' 
print(film_directors.setdefault("Back to the Future")) # key assigned default value of None
print(film_directors)