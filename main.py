from flask import Flask, jsonify

import controllers.boroughs

app = Flask(__name__)

app.add_url_rule('/api/v1/boroughs', 'get_boroughs', controllers.boroughs.get_boroughs)

if __name__ == '__main__':
    app.run(debug=True)
