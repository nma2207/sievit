from gmusicapi import Mobileclient
import gmusicapi
from gmusicapi import Webclient
from gmusicapi import Musicmanager


def main():
    api = Mobileclient()

    while api.login('nma2207@gmail.com', '8927vfhfn',  Mobileclient.FROM_MAC_ADDRESS) !=True:
        print('.',end='')
    print('True')
    # => True

    library = api.get_all_songs()
    print(library)
    sweet_track_ids = [track['id'] for track in library
                       if track['artist'] == 'The Cat Empire']

    playlist_id = api.create_playlist('Rad muzak')
    api.add_songs_to_playlist(playlist_id, sweet_track_ids)

if __name__ == "__main__":
    main()