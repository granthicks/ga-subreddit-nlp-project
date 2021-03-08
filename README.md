# Subreddit Analysis Between Sci-Fi Fandoms

### Background

Bandai is a Japanese toy company and producer of plastic model kits. Some of their most model kits are based on characters and vehicles from science fiction franchises such as Gundam and Star Wars. The Gundam franchise is an animated series that began in 1979 that takes place in a future setting where Earth has colonized space and large human piloted robots are used as weapons of war. Bandai produces models based on these robots in a variety of 'grades' of differing levels of size and complexity. The Star Wars franchise is another science fiction franchise that features space wizard samurai as well as many spaceships and vehicles that are produced into model kits. Both of these science fiction franchises have their own subreddit forums on the site reddit.com. In these forums fans of each franchise discuss things related to the show such as their favorite characters or moments for instance. I will be looking at posts on each of these subreddits to search for any relevant insights.


### Problem Statement

Using submissions to the Gundam and Star Wars subreddits, can we build a model that could take a post from either subreddit and determine which one it came from? Will looking at the most commonly discussed terms or characters provide insight on new plastic model kits that could be produced that would be popular with fans?

---

### Data Used

The data used was collected from posts on two subreddit forums on the site reddit.com. The two subreddits used are r/gundam and r/starwars. The data was collected using a script that has already removed any posts that show up as deleted, removed, or have no text in them (usually just an image or article link). Since these posts would not be useful for the model I will be building they were removed before being saved to a csv file. The script is located under the filename 'toscrape.py' and can be used to scrape any target subreddit to a determined amount of posts, then remove the posts without text and save the results to csv.

---

### Model Evaluation

When looking at differences in subreddit posts I compared three models, Random Forest, Naive Bays, and K-Nearest Neighbors. The Random Forest model correctly predicted 84% of the test data into the corresponding subreddit. This was a better result than both the Naive Bays and KNN models that, which both had a much better accuracy than the baseline but performed slightly worse than the random forest model at 79.9% and 82.9% respectively.

---

### Conclusion
All tests perform better than the baseline score and are able to predict which subreddit a post most likely originated from. Each subreddit shows preferences for certain characters which would mean that plastic model kits that are related with those characters could be more popular with fans. With two characters from the Star Wars show 'The Mandalorian' showing up in the top 10 characters mentioned on the subreddit, it could be a good idea for Bandai to release a plastic model kit based on the show.