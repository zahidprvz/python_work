# 8-6 City Names
c_c = {}

def city_country(name, country):
    c_c['city'] = name
    c_c['country'] = country

    return c_c

dict = city_country("Paris", "Spain") 
print(dict)
dict = city_country("Lahore", "Pakistan")
print(dict)
dict = city_country(name="Delhi", country="India")
print(dict)


print("\n")



# 8-7 Album

album = {}

def make_album(artist_name, album_title, songs=None):
    album['artist_name'] = artist_name
    album['album_title'] = album_title
    album['songs'] = songs

    return album

album = make_album("Jagjit Singh", "Dard") 
print(album)
album = make_album("Mehdi Hassan", "Raag", songs=7)
print(album)
album = make_album(artist_name="Ali Sethi", album_title="Ranjish", songs=10)
print(album)


print("\n")



# 8-8 User Albums

repeat = True
new_album = {}

while repeat:
    consent = input("Do you want to create more Albums? (yes / no):  ")
    if consent == 'yes':
        artist_name = input("Enter Artist name: ")
        album_name = input("Enter album name: ")
        songs = input("Number of songs in album: ")

        new_album = make_album(artist_name, album_name, songs)

    else:
        repeat = False

print(new_album)