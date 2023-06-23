from flask import Flask, render_template, request
from twitoff.predict import predict_user
from twitoff.twitter import add_or_update_user, vectorize_tweet
from twitoff.models import User, Tweet, DB
import os


def create_app():
    app = Flask(__name__)

    # DB Config
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        # query db for users
        users = User.query.all()
        return render_template('base.html', title='HOME', users=users)

    @app.route('/test')
    def test():
        return 'test'

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return """The db has been reset
        <a href='/'>Go to Home<a>
        <a href='/reset'>Go to reset<a>
        <a href='/populate'>Go to Populate<a>"""

    @app.route('/user', methods=['POST'])
    def add_user():
        username = request.values['user_name']
        add_or_update_user(username)
        user = User.query.filter(User.username == username).one()
        return render_template(
            'user.html',
            title=username,
            message='User added successfully',
            tweets=user.tweets
        )

    @app.route('/compare', methods=['POST'])
    def compare():
        username0 = request.values['user0']
        username1 = request.values['user1']
        hypo_tweet_text = request.values['tweet_text']

        if username0 == username1:
            message = 'Cannot compare user to themselves'
        else:
            prediction = predict_user(username0, username1, hypo_tweet_text)
            if prediction:
                predicted_user = username1
            else:
                predicted_user = username0
            message = f"This tweet is more likely written by {predicted_user}"

        return render_template(
            'prediction.html',
            title='Prediction',
            message=message
            )

    @app.route('/user/<name>')
    def user(name=None):
        user = User.query.filter(User.name == name).one()
        return render_template(
            'user.html',
            title=name,
            message='User added successfully',
            tweets=user.tweets
        )

    @app.route('/update')
    def update():
        users = User.query.all()
        for user in users:
            add_or_update_user(user.username)

        return """Users have been updated
        <a href='/'>Go to Home<a>
        <a href='/reset'>Go to reset<a>
        <a href='/populate'>Go to Populate<a>"""

    @app.route('/populate')
    def populate():
        user1 = User(id=1, username='rey')
        DB.session.add(user1)
        user2 = User(id=2, username='ben')
        DB.session.add(user2)

        tweet1 = Tweet(
            id=1, text="This is a tweet",
            user=user1,
            vector=vectorize_tweet("This is a tweet")
        )
        tweet2 = Tweet(
            id=2,
            text="This is another tweet",
            user=user2,
            vector=vectorize_tweet("This is another tweet")
        )
        DB.session.add(tweet1)
        DB.session.add(tweet2)

        DB.session.commit()
        return """The db has been reset
        <a href='/'>Go to Home<a>
        <a href='/reset'>Go to reset<a>
        <a href='/populate'>Go to Populate<a>"""

    return app
