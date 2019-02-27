from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cricket_database import Country, Base, Player, User
engine = create_engine('sqlite:///cricketplayer.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loades into the
# database session object. Any change made against the objests in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()

session = DBSession()

# Dummy User
User1 = User(
    name="Saral Kumar",
    email="saralkumar238@gmail.com",
    picture="https://pbs.twimg.com/profile_images/ "
            "2671170543/18debd694829ed78203a5a36dd364160_400x400.png"
    )
session.add(User1)
session.commit()

# Menu(list of player) for Country India

country1 = Country(name="India", user_id=1)
session.add(country1)
session.commit()

# Gunguly player info
player1 = Player(name="Sourav Ganguly",
                 about="Sourav Chandidas Ganguly, affectionately known as"
                       "Dada,is a former Indian cricketer and captain"
                       "is a former Indian cricketer and captain of the"
                       "Indian national team, appointed as the President of"
                       "the Cricket Association of Bengal he is"
                       "and President of the Editorial Board"
                       "with Wisden India",
                 jersey_number="99",
                 runs="19,924",
                 half_century=114,
                 century=38,
                 place="Kolkata",
                 player_id=1,
                 user_id=1
                 )
session.add(player1)
session.commit()

# Sachine Player info
player2 = Player(name="Sachin Tendulkar",
                 about="Sachin Ramesh Tendulkar is a former Indian"
                       "international cricketer and a former captain of the"
                       "Indian national team, regarded as one of the greatest"
                       "batsman of all time. He is the highest run scorer of"
                       "all time in International cricket",
                 jersey_number="10",
                 runs="36,691",
                 half_century=177,
                 century=101,
                 place="Mumbai",
                 player_id=1,
                 user_id=1
                 )
session.add(player2)
session.commit()

# Dhoni Player info
player3 = Player(name="MS Dhoni",
                 about="Mahendra Singh Dhoni is an Indian international"
                       "cricketer who captained the Indian national team"
                       "in limited-overs formats from 2007 to 2016 and in"
                       "Test cricket from 2008 to 2014.",
                 jersey_number="7",
                 runs="20,793",
                 half_century=125,
                 century=16,
                 place="Ranchi",
                 player_id=1,
                 user_id=1
                 )
session.add(player3)
session.commit()

# Virat player info
player4 = Player(name="Virat Kohli",
                 about="Virat Kohli (5 November 1988) is a renowned Indian"
                       "international cricketer. Currently, he is the captain"
                       "of the India national team. Due to his excellent"
                       "performance in the field, he is often regarded as"
                       "one of the top batsmen in the world.",
                 jersey_number="18",
                 runs="24,261",
                 half_century=122,
                 century=68,
                 place="Delhi",
                 player_id=1,
                 user_id=1
                 )
session.add(player4)
session.commit()

# Rohit player info
player5 = Player(name="Rohit Sharma",
                 about="Rohit Gurunath Sharma is an Indian international"
                       "cricketer who is the vice-captain of the India"
                       "national team in limited-overs formats. He is"
                       "regarded as one of the best limited overs cricketers"
                       "in the world. He is a right-handed batsman and was"
                       "an occasional right-arm off break bowle",
                 jersey_number="45",
                 runs="16,114",
                 half_century=98,
                 century=30,
                 place="Maharashtra",
                 player_id=1,
                 user_id=1
                 )
session.add(player5)
session.commit()

# Hardik player info
player6 = Player(name="Hardik Pandya",
                 about="Hardik Pandya is the perfect modern day cricketer."
                       "He can strike the ball big, roll his arm over decently"
                       "and is a livewire in the field. It is a combination of"
                       "skills India have long waited for since the retirement"
                       "of Kapil Dev. Irfan Pathan gave them hope for a while"
                       "but then lost his mojo and soon disappeared in the"
                       "wilderness. India will wish that Pandya keeps working"
                       "on his game and ends the country search for a seam"
                       "bowling all_rounder.",
                 jersey_number="9",
                 runs="2,193",
                 half_century=10,
                 century=1,
                 place="Gujarat",
                 player_id=1,
                 user_id=1
                 )
session.add(player6)
session.commit()

# Rahul player info
player7 = Player(name="KL Rahul",
                 about="Born in Karnataka, the land of Rahul Dravid, this"
                       "lad took to cricket like fish to water. He started"
                       "early in his college, seeing his inclination towards"
                       "the game, his parents backed him. He didn't disappoint"
                       "either. With his hard work and dedication, Rahul got"
                       "into the Under-19 squad, and from there to the"
                       "Karnataka"
                       "Ranji team. This happened in 2010-11 but the dream run"
                       "didn't last long as he was dropped only to come back"
                       "better and hungrier after a couple of years. In his"
                       "comeback stint, he propelled Karnataka to the trophy"
                       "while becoming one of the prolific run-scorers in"
                       "the team.",
                 jersey_number="1",
                 runs="4,388",
                 half_century=27,
                 century=8,
                 place="Karnataka",
                 player_id=1,
                 user_id=1)
session.add(player7)
session.commit()

# Dhawan player info
player8 = Player(name="Shikhar Dhawan",
                 about="Shikhar Dhawan first made waves at the 2004 U_19 World"
                       "Cup, amassing 505 runs from seven inning to become the"
                       "leading scorer, after which many prophesied good"
                       "thingsfor him and he didnot take long to live up"
                       "to his"
                       "reputation with heavy runs in domestic cricket."
                       " However, unfortunately for him, it was during a "
                       "time when the national team was full to the brim "
                       "with world class players and it was next to imposs"
                       "ible to break into that team.",
                 jersey_number="25",
                 runs="12,763",
                 half_century=73,
                 century=22,
                 place="Delhi",
                 player_id=1,
                 user_id=1)
session.add(player8)
session.commit()

# Yuvi Player info
player9 = Player(name="Yuvraj Singh",
                 about="Son of former India player Yograj Singh, Yuvraj was a"
                       "child prodigy and made a name for himself courtesy of"
                       "power packed yet classy batting. He made big waves in"
                       "the 2000 Under_19 World Cup by plundering plenty of "
                       "runs as the team lifted the trophy. His talent didnot"
                       "go unnoticed as soon he was called up to the Indian"
                       "team for the ICC Knockout trophy in Kenya in 2000. "
                       "Playing only his second game, he scored a match winn"
                       "ing 84 against the likes of Glenn McGrath, Brett Lee"
                       "and Jason Gillespie to show that"
                       "he belonged to the big stage.",
                 jersey_number="12",
                 runs="14,430",
                 half_century=83,
                 century=17,
                 place="Chandigarh",
                 player_id=1,user_id=1)
session.add(player9)
session.commit()

# Menu(list of player) for Country Australia
country2 = Country(name="Australia",user_id=1)
session.add(country2)
session.commit()

# Warner
player1 = Player(name="David Warner",
                 about="A destructive, fiery left-handed opening batsman from"
                       "New South Wales, David Warner became the first Austra"
                       "lian cricketer in 132 years to get into the national"
                       "team without playing a first class game.An outstanding"
                       "fielder and a hard-hitting batter, he was the leading"
                       "run scorer in the 2005 to 2006 season when the"
                       "Australia Under_19s toured India. He then proceeded"
                       "to play the Under_19 World Cup.",
                 jersey_number="22",
                 runs="12,603",
                 half_century=95,
                 century=35,
                 place="New South Wales",
                 player_id=2,user_id=1)
session.add(player1)
session.commit()

# Smith
player2 = Player(name="Steven Smith",
                 about="The best Test batsman at present, Steven Smith's"
                       "career redemption is a story for the ages. Having"
                       "made his name initially as a potential leg-spinner"
                       "who could bat a bit,",
                 jersey_number="99",
                 runs="11,764",
                 half_century=64,
                 century=35,
                 place="Sydney",
                 player_id=2,user_id=1)
session.add(player2)
session.commit()

# finch
player3 = Player(name="Aaron Finch",
                 about="Aaron James Finch is an aggressive top-order batsman,"
                       "who plays for Victoria. Known for his hard-hitting and"
                       "ability to finish matches, Finch earned his spot in"
                       "Australia's Under-19 team.",
                 jersey_number="14",
                 runs="6,666",
                 half_century=41,
                 century=14,
                 place="Colac",
                 player_id=2,user_id=1)
session.add(player3)
session.commit()

# hussy
player4 = Player(name="Michael Hussy",
                 about="Holder of the tag Mr Cricket, Michael Hussey"
                       "personifies"
                       "the never say die attitude, symbolic of the archetype"
                       "Australian cricketer. Ironically though, despite"
                       "scoring tons of runs in the domestic circuit, Hussey"
                       "had to wait"
                       "till the age of 28 to make his international debut,"
                       " thanks to the embarrassing problem of plenty in the"
                       "Australian line up through those years. But he grabbed"
                       "the few opportunities presented to him and carved out"
                       "a niche for himself on the"
                       "world cricket stage.",
                 jersey_number="2",
                 runs="16,471",
                 half_century=85,
                 century=24,
                 place="Perth",
                 player_id=2,user_id=1)
session.add(player4)
session.commit()

# Watson
player5 = Player(name="Shane Waston",
                 about="Watson made his international debut in 2002 during the"
                       "tour of South Africa in the ODI series. Australia had"
                       "just appointed Ricky Ponting as the skipper and also"
                       "decided to make a selection overhaul of sorts. With"
                       "their obsession for bits-and-pieces all-rounders,"
                       "Watson was an obvious selection considering that he"
                       "was more than just a utility all-rounder.",
                 jersey_number="23",
                 runs="15,233",
                 half_century=83,
                 century=18,
                 place="Queensland",
                 player_id=2,user_id=1)
session.add(player5)
session.commit()

# head
player6 = Player(name="Travis Head",
                 about="Since Michael Hussey's retirement, Australia have"
                       "struggled to find a reliable middle order batsman"
                       "who can both anchor and finish an innings. There"
                       "have been a few who have auditioned for the spot"
                       "some with brief success as well but the consistency"
                       "hasn't been there for a longer duration. Travis Head"
                       "is touted to be capable of being that man and there"
                       "is a feeling that he can emerge as one of the country"
                       "'s finest middle-order batsmen in limited-overs"
                       "cricket",
                 jersey_number="28",
                 runs="1,500",
                 half_century=15,
                 century=1,
                 place="Adelaide",
                 player_id=2,user_id=1)
session.add(player6)
session.commit()


# Menu (list of player) for Country Pakistan
country3 = Country(name="Pakistan",user_id=1)
session.add(country3)
session.commit()

# huffise
player1 = Player(name="Mohammad Hafeez",
                 about="An opening batsman and a more than decent off-spinner,"
                       " Mohammad Hafeez, came into the Pakistan side after"
                       "their disastrous exit from the 2003 World Cup. He made"
                       "a promising start to his Test career, scoring a half-"
                       "century on debut against Bangladesh and followed it up"
                       " with a century in the next match.",
                 jersey_number="32",
                 runs="10,800",
                 half_century=58,
                 century=21,
                 place="Punjab", player_id=3,user_id=1)
session.add(player1)
session.commit()

# umar akmal
player2 = Player(name="Umar Akmal",
                 about="Born on 26 May 1990, Umar Akmal is the youngest of"
                       "the three brothers who have represented Pakistan in"
                       "International cricket",
                 jersey_number="11",
                 runs="7,333",
                 half_century=36,
                 century=3,
                 place="Lahore",
                 player_id=3,user_id=1)
session.add(player2)
session.commit()

# kakmal
player3 = Player(name="Kamran Akmal",
                 about="Test cricket, he would swiftly change to his position"
                       "in the lower middle order. He was particularly success"
                       "ful against arch-rivals India, against whom he"
                       "performed many rescue acts. His maiden Test ton was"
                       "one such show where he scored a defying century coming"
                       "down at Number 8 at Mohali in 2005",
                 jersey_number="10",
                 runs="9199",
                 half_century=28,
                 century=11,
                 place="Lahore",
                 player_id=3,user_id=1)
session.add(player3)
session.commit()

# malik
player4 = Player(name="Shoaib Malik",
                 about=" Test cricket, he would swiftly change to his position"
                       "in the lower middle order. He was particularly success"
                       "ful against arch-rivals India, against whom he perfor"
                       "med many rescue acts. His maiden Test ton was one such"
                       "show where he scored a defying century coming down at"
                       "Number 8 at Mohali in 2005.",
                 jersey_number="13",
                 runs="10,555",
                 half_century=58,
                 century=12,
                 place="Sialkot",
                 player_id=3,user_id=1)
session.add(player4)
session.commit()

# afrid
player5 = Player(name="Shahid Afridi",
                 about="Shahid Afridi, Pakistan's allrounder, is as enigmatic"
                       "a player as there ever was. He came as a 16-year-old"
                       "into the Pakistan ODI squad and was unfazed by all the"
                       "speculation regarding his real age. In only in his"
                       "second ODI against Sri Lanka in 1996, he blasted his"
                       "way to a 37-ball century",
                 jersey_number="9",
                 runs="1,222",
                 half_century=51,
                 century=11,
                 place="Khyber Agency",
                 player_id=3,user_id=1)
session.add(player5)
session.commit()

# salmon
player6 = Player(name="Salman Butt",
                 about="A career which was set to achieve heights fell to"
                       "pieces after events that unfolded during the Lords"
                       "Test against England in August, 2010.",
                 jersey_number="7",
                 runs="5,544",
                 half_century=28,
                 century=11,
                 place="Lahore",
                 player_id=3,user_id=1)
session.add(player6)
session.commit()

player7 = Player(name="Inzamam-ul-Haq",
                 about="Inzamam-ul-Haq was a symbiosis of strength and"
                       "subtlety. Power was no surprise, but sublime touch"
                       "was remarkable for a man of his bulk. He loathed"
                       "exercise and often looked a passenger in the field,"
                       " but with a willow between his palms he was suddenly"
                       "galvanised",
                 jersey_number="16",
                 runs="19,222",
                 half_century=122,
                 century=35,
                 place="Multan",
                 player_id=3,user_id=1)
session.add(player7)
session.commit()

print("List of Players are added!!!")
