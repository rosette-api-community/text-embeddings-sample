#Rosette API Text Embeddings Sample Code
This is a little python code to show how to calculate the similarity between words by computing the cosine similarity (using numpy) between the words' embeddings, returned from the [Rosette API](https://developer.rosette.com/)'s new `/text-embedding` endpoint. The call to the API uses the 1.3 version of the python binding, so be sure to install that package via `$ pip install rosette-api` or `--upgrade` via pip to get the latest.

# To try it out
1. Clone the repo and open the files in your favorite text editor/python IDE.
2. In `cosine_similarity.py`, replace the `user_key` parameter's value `[your key here]` with your [Rosette API key](https://developer.rosette.com/admin/applications) and save.
3. Run `test_embeddings.py` via your python IDE or command line:
  `$ python test_embeddings.py`

# Customize for your data
Try editing `test_embeddings.py` to compare words OR longer text you might be interested in to see how their embeddings compare. And if you find anything interesting, let us know! Find us at [support.rosette.com](https://support.rosette.com/hc/en-us) or support@rosette.com.

