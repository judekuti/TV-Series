"""
This creates instances of the class Movie contained in the module media.
This file drives the movie website but with a requirement that the media,
and fresh_tomatoes modules are in same folder.

"""
import media
import fresh_tomatoes

# Below is a catalog of twelve TV series trailers displayed.
# Eight parameters are employed to x-ray the TV series


dsurvivor=media.Movie("Designated Survivor",
                    "PG 13",
                    "A lower-level cabinet member who unexpectedly becomes president\
                    after a devastating attack on Washington He will struggle to\
                    prevent the country and his own family from falling into chaos,\
                    as he is thrust into one of the most difficult presidencies in history",
                    "Action",
                    "http://www.gstatic.com/tv/thumb/tvbanners/14387024/p14387024_b_v8_aa.jpg",
                    "https://youtu.be/N_f1v0Nx5Sw",
                    "Season II",
                    "Episode 4"
                    )


waywardpines=media.Movie("Wayward Pines",
                        "PG",
                        "Each step closer to the truth takes Ethan further from\
                        the life he knew, from the husband and father he was, until\
                        he must face the terrifying reality that he may never get out\
                        of Wayward Pines alive.",
                        "Sci-Fi",
                        "http://www.gstatic.com/tv/thumb/tvbanners/12670025/p12670025_b_v8_aa.jpg",
                        "https://youtu.be/AhvszRrle5o",
                        "Season II",
                        "Episode 10"
                        )


banshee=media.Movie("Banshee",
                    "R",
                    "Set in the small town of Banshee in Pennsylvania Amish country, \
                    the series' main character is an enigmatic ex-con (Antony Starr), \
                    who assumes the identity of Lucas Hood, the town's murdered sheriff,\
                    to hide from powerful crime lord Rabbit (Ben Cross).",
                    "Action",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BYWRjY2Y1OGQtZTRmYS00OTFmLTg0OTUtZWJiZmYwMDk2M2QzXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY1200_CR93,0,630,1200_AL_.jpg", 
                    "https://youtu.be/1aYDopySWJQ",
                    "Season IV",
                    "Episode 8")

narcos=media.Movie( "Narcos",
                    "PG-13",
                    "The Medellin cartel - the most violent, ruthless and wealthy \
                    criminal organization in the history of modern crime. \
                    And the one man who lorded over them all... Pablo Escobar. ",
                    "Drama",
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:\
                    ANd9GcSUoTHVtBd1HyofXuIFUyDTzTs_hoCpzfi2Ky7mWXWqTfUDW3G7cQ",
                    "https://youtu.be/U7elNhHwgBU",
                    "Season III",
                    "Episode 10")

empire=media.Movie( "Empire",
                    "PG-13",
                    "A sexy and powerful new drama about the head of a music empire\
                    (Terrence Howard) whose three sons and ex-wife all battle for his throne.",
                    "Musical",
                    "http://legacy.shadowandact.com/wp-content/uploads/2016/05/empire-pos-3.jpg",
                    "https://youtu.be/lmi5QbkhQ1Q",
                    "Season IV",
                    "Episode 4")

star=media.Movie("Star",
                "PG",
                "Three talented singers, desperate for a new start and with ambitions of stardom,\
                navigate the cut-throat music business on their road to success.",
                "Musical",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA3MTMyNzc5NTReQTJeQWpwZ15BbWU4MDY3Mjc0NjAy._V1_UY1200_CR89,0,630,1200_AL_.jpg",
                "https://youtu.be/T2snL9QUIZI",
                "Season II",
                "Episdoe 4")


the_americans=media.Movie("The Americans",
                        "R",
                        "It is a 1980s Cold War drama. The premise is that a group of \
                        Soviet KGB officers have been trained to impersonate American citizens,\
                        so that each one can become a sleeper agent, with a cover which may \
                        even include an unwitting spouse and family.",
                        "Drama",
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn:\
                        ANd9GcQffLyLTEZwdua-twnX_0Jrb-JtCp8rghBkcDcTtSita-wBXXorug",
                        "https://youtu.be/YGr75NZ5y34",
                        "Season V",
                        "Episode 13")

lost=media.Movie("Lost",
                "G",
                "The survivors of Oceanic Flight 815 were 1,000 miles off course \
                when they crashed on a lush, mysterious island. \
                Each person possesses a shocking secret,\
                but they've got nothing on the island itself, which harbors a monstrous\
                security system, a series of underground bunkers and a group of violent \
                survivalists hidden in the shadows.",
                "Sci-Fi",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA3NzMyMzU1MV5BMl5BanBnXkFtZTcwNjc1ODUwMg@@._V1_UY1200_CR157,0,630,1200_AL_.jpg",
                "https://youtu.be/KTu8iDynwNc",
                "Season VI",
                "Episode 18")

twenty_four=media.Movie("24",
                        "PG-13",
                        "Counterterrorism agent Jack Bauer fights the bad guys of the world,\
                        a day at a time. With each week's episode unfolding in real time,\
                        Twenty Four covers a single day in the life of Bauer each season. \
                        Jack deals with assassination attempts, nuclear attacks, bioterrorism, \
                        torture, traitors, sleeper cells, other bad guys and the alarming \
                        tendency for his romances to end badly -- very badly.",
                        "Action",
                        "http://www.gstatic.com/tv/thumb/tvbanners/7974316/p7974316_b_v8_ab.jpg",
                        "https://youtu.be/hX-z6-ApPhA",
                        "Season IX",
                        "Episode 12")

prison_break=media.Movie("Prison Break",
                        "PG",
                        "Michael Scofield is a desperate man in a desperate situation. \
                        His brother, Lincoln Burrows, was convicted of a crime he didn't \
                        commit and put on Death Row. Michael holds up a bank to get himself \
                        incarcerated alongside his brother in Fox River State Penitentiary,\
                        then sets in motion a series of elaborate plans to break Lincoln out \
                        and prove his innocence. Once out of jail, their perils aren't over\
                        the brothers must flee to escape recapture and battle an intricate political \
                        conspiracy that puts everyone's life at risk.",
                        "Action",
                        "http://www.gstatic.com/tv/thumb/tvbanners/12900907/p12900907_b_v8_aa.jpg",
                        "https://youtu.be/mZwEBHc_PBw",
                        "Season V",
                        "Episode 9")

tyrant=media.Movie( "Tyrant",
                    "PG-13",
                    "Bassam 'Barry' al-Fayeed, who has fully assimilated to living in America, \
                    is the son of a Middle Eastern dictator. Barry is a pediatrician in Los Angeles, \
                    but he and his family return to his native country for his nephew's wedding. \
                    It's his first visit in 20 years, but things don't go as planned.\
                    When his father dies suddenly, Barry and his family are embroiled in political upheaval\
                    and forced to stay in the country. A clash of cultures ensues as Barry is thrown back into\
                    the familial and national politics of his youth, which he had escaped by self-imposed exile.",
                    "Drama",
                    "http://www.gstatic.com/tv/thumb/tvbanners/12923357/p12923357_b_v8_aa.jpg",
                    "https://youtu.be/RbLK99ysvck",
                    "Season III",
                    "Episode 10")

got=media.Movie("Game of Thrones",
                "NC-17",
                "George R.R. Martin's best-selling book series 'A Song of Ice and Fire' \
                is brought to the screen as HBO sinks its considerable storytelling teeth \
                into the medieval fantasy epic. It's the depiction of two powerful families\
                kings and queens, knights and renegades, liars and honest men playing a deadly game\
                for control of the Seven Kingdoms of Westeros, and to sit atop the Iron Throne.",
                "Epic",
                "http://www.gstatic.com/tv/thumb/tvbanners/14160794/p14160794_b_v8_aa.jpg",
                "https://youtu.be/iGp_N3Ir7Do",
                "Season VII",
                "Episode 7")
# An array of the objects created in the various TV Series details.
movies=[dsurvivor,waywardpines, banshee, narcos, empire, star, the_americans,lost, twenty_four, prison_break, tyrant, got]

# The function is called from the fresh_tomatoes module to view the website and movies
fresh_tomatoes.open_movies_page(movies)

# Display in the shell summary of the module as documented using docstrings
print media.Movie.show_image.__doc__


