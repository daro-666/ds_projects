from lyricscomfunc import artist_predictor, link_to_lyrics
from argparse import ArgumentParser


parser = ArgumentParser(
                        description="call the program with some lyrics or a link to a lyrics page and it will decide to what artist the lyrics belong",
                        )
parser.add_argument("-t", "--text",
                    help="enter your test lyrics here",
                    type=str,
                    )
parser.add_argument("-l", "--link",
                    type=str,
                    help="use hyperlink to a lyrics page"
                    )
parser.add_argument("-v", "--verbosity",
                    type=int,
                    help="show more info on whats happening in the background",
                    choices=[0,1,2],
                    default=0,
                    )
args = parser.parse_args()

res=0

if args.link:
    
    lyrics = link_to_lyrics(args.link)
    
    if lyrics == "No lyrics" or lyrics == "Failed request":
        print("No lyrics or failed request. Better luck next time!")
    else:
        res = artist_predictor(lyrics)

elif args.text:
    res = artist_predictor(args.text)

else:
    parser.print_help()
    
if not res==0:

    if args.verbosity==2:
        print()
        print(f"Wow your string was messy! Here are the essential words: {res[2]}")
        print()
        print(f"With a probability of: {res[1]}%")
        print(f"Your songs artist is : {res[0]}")
        print()
    elif args.verbosity==1:
        print()
        print(f"With a probability of: {res[1]}%")
        print(f"Your songs artist is : {res[0]}")
        print()
    else:
        print()
        print(f"Your songs artist is : {res[0]}")
        print()