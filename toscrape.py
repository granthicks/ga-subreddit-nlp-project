import requests
import time
import pandas as pd

url = 'https://api.pushshift.io/reddit/search/submission'

def get_posts(subreddit, last):

	"""Very slightly modified from a script created by Alex P.
	Found at https://www.textjuicer.com/2019/07/crawling-all-submissions-from-a-subreddit/

	Crawl a page of results from a given subreddit.

    :param subreddit: The subreddit to crawl.
    :param last: The last downloaded page.

    :return: A page or results.
    """

	params = {
	'subreddit' : subreddit,
	'size' : 100,
	'sort' : 'desc',
	'sort_type' : 'created_utc'
	}

	if last != None:
		if len(last) > 0:
			params['before'] = last[-1]['created_utc']
		else:
			return []

	results = requests.get(url, params)

	return results.json()['data']


def get_num_total_posts(subreddit, num_total_posts):
	"""
  	Also found from the same link as 'get_posts'
  	Variable names are changed from original for my usage.


  	Crawl submissions from a subreddit.

  	:param subreddit: The subreddit to crawl.
  	:param num_total_posts: The maximum number of submissions to download.

  	:return: A list of submissions.
  	"""

	submissions = []
	last = None

	while last != [] and len(submissions) < num_total_posts:
		last = get_posts(subreddit, last)
		submissions += last
		time.sleep(3)
	return submissions[:num_total_posts]



def remove_bad_as_df(post_list):
	"""
	This function will take in the data that has been collected from the subreddit
	and remove any post that is [removed], [deleted], or empty and return it as a 
	dataframe to be saved to a csv file.

	:param post_list: The list of posts collected from the selected subreddit

	:return: A dataframe containing only posts with text in the body.
	"""

	data_frame = pd.DataFrame(post_list)
	data_frame = data_frame[data_frame['selftext'] != '[removed]']
	data_frame = data_frame[data_frame['selftext'] != '[deleted]']
	data_frame = data_frame[data_frame['selftext'] != '']
	data_frame = data_frame.dropna(axis = 0, subset = ['selftext'])
	return data_frame

print("This script will collect posts from a desired subreddit, eliminate deleted"
	", removed, or blank posts (usually containing only a link or image) and return"
	" the resulting information into a specified .csv file. For best results when "
	"gathering from subreddits with a high number of image or link posts, use a high "
	"number of submissions to gather.")

nothing_to_search = True
while nothing_to_search:
	subreddit_to_search = input('Enter the name of the subreddit you would like to search: ')
	test_params = {'subreddit' : subreddit_to_search}
	test = requests.get(url, test_params)
	if test.status_code != 200:
		print("Something went wrong! Please try another subreddit name: ")
		nothing_to_search = True
	else:
		print('Valid subreddit!')
		nothing_to_search = False

no_post_nums = True
while no_post_nums:
	try:
		num_posts = int(input("Enter the number of posts to retrieve: "))
		no_post_nums = False
	except:
		print('Something went wrong! Please enter a valid number of posts to search: ')

num_posts_checked = False
while not num_posts_checked:
	if num_posts < 0:
		print('Please enter a valid number to check!')
		try:
			num_posts = int(input("Enter the number of posts to retrieve: "))
		except:
			print('Something went wrong! Please enter a valid number of posts to search: ')
	else:
		num_posts_checked = True


file_name = input("Enter the name for the .csv file: ")

good_to_go = False

choice = None

while choice not in('y', 'n'):
	choice = input('All set! Ready to start? ("y" to start or "n" to quit): ')
	if not choice:
		print('Sorry, please enter "y" to collect posts or "n" to quit. ')


if choice == 'n':
	exit()

print('Fetching those posts! Please be paitient, this could take a while.')

post_fetch = get_num_total_posts(subreddit_to_search, num_posts)

print('Done! Now getting rid of unuseful posts.')

clean_posts = remove_bad_as_df(post_fetch)

print('Bad posts removed, saving to file now.')

clean_posts.to_csv(file_name + '.csv', index = False)

print('File saved! See you next time!')