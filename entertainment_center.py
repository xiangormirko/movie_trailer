import media
import fresh_tomatoes


toy_story= media.Movie("Toy Story", 90, "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4") 
avatar= media.Movie("Avatar", 140, "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
interstellar= media.Movie("Interstellar", 155, "A man travels space in order to save humanity, damn legendary movie", "http://vignette2.wikia.nocookie.net/interstellarfilm/images/4/46/Interstellar_poster.jpg/revision/latest?cb=20140606051928","https://www.youtube.com/watch?v=0vxOhd4qlnA")
miss_granny= media.Movie("Miss Granny", 100, "A woman in her 70s who magically finds herself in the body of her 20-year-old self","http://upload.wikimedia.org/wikipedia/en/4/45/Miss_Granny_poster.jpg","https://www.youtube.com/watch?v=HUIkT3JA0_Q" )
inglorious_bastards= media.Movie("Inglorious Bastards", 110, "he film tells the fictional alternate history story of two plots to assassinate Nazi Germany's political leadership","http://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg","https://www.youtube.com/watch?v=6AtLlVNsuAc")
into_the_wild= media.Movie("Into the Wild",120, "It is an adaptation of the 1996 non-fiction book of the same name by Jon Krakauer based on the travels of Christopher McCandless across North America and his life spent in the Alaskan wilderness in the early 1990s.","http://upload.wikimedia.org/wikipedia/en/8/8a/Into-the-wild.jpg","https://www.youtube.com/watch?v=2LAuzT_x8Ek")
avatar_airbender=media.TvShow("Avatar: the last Airbender",30, "Avatar Ang's adventures", "http://upload.wikimedia.org/wikipedia/en/9/9b/Avatar-_The_Last_Airbender_Book_1_DVD.jpg", "https://www.youtube.com/watch?v=Rz7EsOua-D4",1, 3)
game_of_thrones= media.TvShow("Game of Thrones",40, "he fifth season of the fantasy drama television series Game of Thrones was ordered by HBO in April 2014, together with the sixth season,[1] and premiered on April 12, 2015.","http://upload.wikimedia.org/wikipedia/en/7/71/Game_of_Thrones_S5_Poster.jpg","https://www.youtube.com/watch?v=A0pLbTXPHng",5,5)
sherlock= media.TvShow("Sherlock",50,"Sherlock is a British crime drama television series and a contemporary adaptation of Sir Arthur Conan Doyle's Sherlock Holmes detective stories.","http://th07.deviantart.net/fs71/PRE/i/2012/155/1/8/sherlock_series_3_fan_poster_2_by_crqsf-d52873p.jpg","https://www.youtube.com/watch?v=9UcR9iKArd0",3,1)

#print(avatar.trailer_youtube_url)

#toy_story.show_trailer()

#interstellar.show_trailer()


movies=[toy_story,avatar, interstellar, miss_granny,inglorious_bastards, into_the_wild, avatar_airbender, game_of_thrones, sherlock]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
print(toy_story.duration)
print(avatar_airbender.season)
