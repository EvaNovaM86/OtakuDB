import media
import otakudb

# Format like so
# class Movie():
#     def __init__(self, movie_title,movie_storyline, poster_image, trailer_url):
#         self.title = movie_title
#         self.storyline = movie_storyline
#         self.poster = poster_image
#         self.trailer = trailer_url


sprited_away = media.Movie('Sprited Away',
                           'Spirited Away is a 2001 Japanese animated fantasy film written and directed by '
                           'Hayao Miyazaki and produced by Studio Ghibli.The film stars Rumi Hiiragi, '
                           'Miyu Irino, Mari Natsuki, Takeshi Naito, Yasuko Sawaguchi, Tsunehiko Kamijō, '
                           'Takehiko Ono and Bunta Sugawara, and tells the story of Chihiro Ogino, '
                           'a sullen ten-year-old girl who, while moving to a new neighborhood, '
                           'enters the spirit world. After her parents are transformed into pigs'
                           ' by the witch Yubaba, Chihiro takes a job working in Yubaba\'s bathhouse to find'
                           ' a way to free herself and her parents and return to the human world.',
                           'https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG',
                           'https://www.youtube.com/watch?v=ByXuk9QqQkk')

cowboy_bebop = media.Movie('Cowboy Bebop',
                           'In the year 2071, humanity has colonized several of the planets and moons of the '
                           'solar system leaving the now uninhabitable surface of planet Earth behind.'
                           ' The Inter Solar System Police attempts to keep peace in the galaxy,'
                           ' aided in part by outlaw bounty hunters, referred to as "Cowboys".'
                           ' The ragtag team aboard the spaceship Bebop are two such individuals.',
                           'http://cdn.myanimelist.net/images/anime/4/19644.jpg',
                           'https://www.youtube.com/watch?v=Aw3fN3OPk3A',)

ghost_in_the_shell = media.Movie('Ghost in the shell',
                                 'A cyborg policewoman and her partner hunt a mysterious and powerful hacker '
                                 'called the Puppet Master.',
                                 'http://ia.media-imdb.com/images/M/MV5BMTk2ODE4MDUzNF5BMl5BanBnXkFtZTYwNTI2OTA5._V1_UY268_CR4,0,182,268_AL_.jpg',
                                 'https://www.youtube.com/watch?v=0j6wsGuzP2Q')

jojo = media.Movie('JoJo\'s Bizarre Adventure',
                   'Kujo Jotaro is a normal, popular Japanese high-schooler, until he thinks that he is '
                   'possessed by a spirit, and locks himself in prison. After seeing his grandfather, '
                   'Joseph Joestar, and fighting Joseph\'s friend Muhammad Abdul, Jotaro learns that the'
                   ' "Spirit" is actually Star Platinum, his Stand, or fighting energy given a semi-solid '
                   'form. Later, his mother gains a Stand, and becomes sick. Jotaro learns that it is '
                   'because the vampire Dio Brando has been revived 100 years after his defeat to '
                   'Jonathan Joestar, Jotaro\'s great-great-grandfather. Jotaro decides to join Joseph and '
                   'Abdul in a trip to Egypt to defeat Dio once and for all.',
                   'https://upload.wikimedia.org/wikipedia/en/a/aa/JoJo_Part_1_Phantom_Blood.jpg',
                   'https://www.youtube.com/watch?v=EO08vMz73YY')

gurren_lagann = media.Movie('Tengen Toppa Gurren Lagann',
                            'Simon and Kamina were born and raised in a deep, underground village, '
                            'hidden from the fabled surface. Kamina is a free-spirited loose cannon'
                            ' bent on making a name for himself, while Simon is a timid young boy '
                            'with no real aspirations. One day while excavating the earth, Simon '
                            'stumbles upon a mysterious object that turns out to be the ignition key '
                            'to an ancient artifact of war, which the duo dubs Lagann. Using their new '
                            'weapon, Simon and Kamina fend off a surprise attack from the surface with the '
                            'help of Yoko Littner, a hot-blooded redhead wielding a massive gun who wanders '
                            'the world above.',
                            'http://cdn.myanimelist.net/images/anime/4/5123l.jpg',
                            'https://www.youtube.com/watch?v=oXkkMhCuCMg')

lain = media.Movie('Serial Experiments Lain',
                   'Lain Iwakura, an awkward and introverted fourteen-year-old, is one of the many girls '
                   'from her school to receive a disturbing email from her classmate Chisa Yomoda—the very '
                   'same Chisa who recently committed suicide. Lain has neither the desire nor the '
                   'experience to handle even basic technology; yet, when the technophobe opens the email, '
                   'it leads her straight into the Wired, a virtual world of communication networks similar '
                   'to what we know as the internet. Lain\'s life is turned upside down as she begins to '
                   'encounter cryptic mysteries one after another. Strange men called the Men in Black begin'
                   ' to appear wherever she goes, asking her questions and somehow knowing more about her '
                   'than even she herself knows. With the boundaries between reality and cyberspace rapidly '
                   'blurring, Lain is plunged into more surreal and bizarre events where identity, '
                   'consciousness, and perception are concepts that take on new meanings.',
                   'http://cdn.myanimelist.net/images/anime/3/10243l.jpg',
                   'https://www.youtube.com/watch?v=t9CXmEUwvgM')



# Create a list of movies and pass them to our webpage
movies = [sprited_away, cowboy_bebop, ghost_in_the_shell, jojo, gurren_lagann, lain]
otakudb.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)