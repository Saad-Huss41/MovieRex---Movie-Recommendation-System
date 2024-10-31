from flask import Flask, render_template
from logic import get_recommendations  

app = Flask(__name__)

@app.route('/recommendations/<title>')
def recommendations(title):
    recommendations = get_recommendations(title, cosine_sim2)
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)