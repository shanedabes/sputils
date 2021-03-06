import pytest
import unittest.mock

import deepdiff

from sputils import search


def test_album_to_dict_searched(api_album_searched, album_dict_searched):
    album = search.album_to_dict_searched(api_album_searched)

    assert deepdiff.DeepDiff(album, album_dict_searched) == {}


def test_track_to_dict_searched(api_track_searched, track_dict_searched):
    track = search.track_to_dict_searched(api_track_searched)

    assert deepdiff.DeepDiff(track, track_dict_searched) == {}


def test_artist_to_dict_searched(api_artist_searched, artist_dict_searched):
    artist = search.artist_to_dict_searched(api_artist_searched)

    assert deepdiff.DeepDiff(artist, artist_dict_searched) == {}


def test_search_album(sp_mock, api_album_searched, album_dict_searched):
    sp = sp_mock.Spotify()

    expected = [album_dict_searched]

    searched = search.search_albums(sp, 'test')

    assert deepdiff.DeepDiff(searched, expected) == {}


def test_search_track(sp_mock, api_track_searched, track_dict_searched):
    sp = sp_mock.Spotify()

    expected = [track_dict_searched]

    searched = search.search_tracks(sp, 'test')

    assert deepdiff.DeepDiff(searched, expected) == {}


def test_search_artist(sp_mock, api_artist_searched, artist_dict_searched):
    sp = sp_mock.Spotify()

    expected = [artist_dict_searched]

    searched = search.search_artists(sp, 'test')

    assert deepdiff.DeepDiff(searched, expected) == {}


def test_search_playlists(sp_mock, api_playlist, playlist_dict):
    sp = sp_mock.Spotify()

    expected = [playlist_dict]

    searched = search.search_playlists(sp, 'test')

    assert deepdiff.DeepDiff(searched, expected) == {}


@unittest.mock.patch('sputils.search.search_albums')
@unittest.mock.patch('sputils.search.search_tracks')
@unittest.mock.patch('sputils.search.search_artists')
@unittest.mock.patch('sputils.search.search_playlists')
def test_searcher(mock_sp, mock_sar, mock_st, mock_sa, sp_mock):
    sp = sp_mock.Spotify()

    search.searcher(sp, 'test', 'albums')
    mock_sa.assert_called_once()

    search.searcher(sp, 'test', 'tracks')
    mock_st.assert_called_once()

    search.searcher(sp, 'test', 'artists')
    mock_sar.assert_called_once()

    search.searcher(sp, 'test', 'playlists')
    mock_sp.assert_called_once()

    with pytest.raises(ValueError) as e:
        search.searcher(sp, 'test', 'test')
