# Music-Sentiment-Analysis
This is a music sentiment analysis project, it uses the music dataset from spotify, the dataset can be found <a href="https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=data.csv">here</a>.


**Idea:** Giving each song a sentiment based on its valence value (Valence describes the positvity of a song, the higher it is the more cheerful a song).


**Steps:** 
1. Data Cleaning steps for the song name, removing parts like live, remaster, demo, etc.
Steps include: 
 	- Removal of punctuations
 	- Tokenization
	- Lemmatization
	- Restructuring into a string
2. Calculate valence value of the song of 3 categories: Positive, Neutral, Negative.
3. Balancing the groups of output.
4. Creating a word cloud of the lyrics to visualize which words are associated with which sentiment.
5. Use TF-IDF to vectorize the lyrics of the training and testing datasets.
6. Use different ML classifiers on the TF-IDF vectors only. (Low accuracy)
7. Use ML classifiers with lyrics and other parameters of a song as well. (Better accuracy)
8. 