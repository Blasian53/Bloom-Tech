import numpy as np
from sklearn.linear_model import LogisticRegression
from twitoff.models import User
from twitoff.twitter import vectorize_tweet


def predict_user(username0, username1, hypo_tweet_text):
    user0 = User.query.filter(User.username == username0).one()
    user1 = User.query.filter(User.username == username1).one()

    # Grab tweet vectors from each user (as a numpy array)
    user0_vectors = np.array([tweet.vector for tweet in user0.tweets])
    user1_vectors = np.array([tweet.vector for tweet in user1.tweets])

    # Vertically stack tweet vectors into one np array
    vectors = np.vstack([user0_vectors, user1_vectors])
    labels = np.concatenate([
        np.zeros(len(user0.tweets)),
        np.ones(len(user1.tweets))
    ])

    # fit our data into model
    LogReg = LogisticRegression().fit(vectors, labels)

    # Vectorize hypo tweets
    hypo_tweet_vector = vectorize_tweet(hypo_tweet_text)

    return LogReg.predict(hypo_tweet_vector.reshape(1, -1))
