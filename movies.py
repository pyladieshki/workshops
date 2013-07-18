
import json
import urllib, urllib2
import random
import pprint

def random_movies(filename):

    movienames = []

    with open(filename) as f:
        for row in f:
            name = row.strip()
            movienames.append(name)

    random.shuffle(movienames)
    return movienames

def play(filename):

    movienames = random_movies(filename)
    
    end = len(movienames)
    index = 0
    pp = pprint.PrettyPrinter(indent=4)

    print('*'*80)
    print('\nWelcome to Rating vs Rating:guess which movie got a better reception!\n')
    print('*'*80)
    
    char = raw_input('Press y to start, h for help, or q to quit.\n') 

    while(char != 'q'):
        
        if(char == 'h'):
            print('''Guess which has the higher IMDb rating from two movies.
            Ratings are fetched from the OMDb API.
            Movies are stored in movielist.txt and they are shuffled randomly 
            each time.
            You can add more movies to the file, put each on their own line.''')
            char = raw_input('Press y to start playing, or q to quit.\n')

        elif(char == 'y'):
            if (index < end - 2):

                print("Getting first movie..")

                url = 'http://www.omdbapi.com/?%s' % (urllib.urlencode({'t': movienames[index]})) 

                req = urllib2.urlopen(url)
                movie_dict1 = json.loads(req.read().decode('UTF-8'))

                rating1 = movie_dict1['imdbRating']
                if rating1 == 'N/A':
                    index += 1
                    continue

                title1 = movie_dict1['Title']
                print('Getting second movie..')

                url = 'http://www.omdbapi.com/?%s' % (urllib.urlencode({'t': movienames[index + 1]})) 

                req = urllib2.urlopen(url)
                movie_dict2 = json.loads(req.read().decode('UTF-8'))          
                rating2 = movie_dict2['imdbRating']
         
                if rating2 == 'N/A':
                    index += 1
                    continue

                title2 = movie_dict2['Title']
                answer = raw_input('Do you think %s has a higher rating than %s?(y/n)' % (title1,title2))

                if(answer == 'y' and rating1 > rating2):
                    print('Yep! ')
                elif(answer == 'n' and rating1 < rating2):
                    print('Right again! ')
                else:
                    print('Sorry. ')

                print('%s is rated %s, %s is rated %s. \n' %
                      (title1,rating1,title2,rating2))     

            else:
                print('All movies done! Add more to movielist.txt.\n')
                break
        
            index += 1
            char = raw_input('Y to play again, q to quit, m for more info\n')

        else:
            char = raw_input('Y to play, q to quit')

        if char == 'm' and title1 is not None and title2 is not None:
            print(title1)
            pp.pprint(movie_dict1)
            print(title2)
            pp.pprint(movie_dict2)
            char = raw_input(' Press y to play again, q to quit\n')

    print("Thanks for playing!\n")

if __name__ == '__main__':
    play('movielist.txt')
