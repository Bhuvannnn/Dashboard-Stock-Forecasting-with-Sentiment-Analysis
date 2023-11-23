from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def keyword_search():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        noOfTweet = request.form.get('noOfTweet')
        # Perform your keyword search and sentiment analysis here using the keyword and noOfTweet variables
        return "Keyword: {}, No. of Tweets: {}".format(keyword, noOfTweet)
    return render_template('sent.html')

if __name__ == '__main__':
    app.run(debug=True)
