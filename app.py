import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/atrain', methods=['GET'])
def atrain():
   print('training AI')
   #AI train model work
   return redirect(url_for('index'))

@app.route('/teams', methods=['GET'])
def teams():
   team1 = request.form.get('team1')
   team2 = request.form.get('team2')

   if team1:
       print('Request for teams received with team names1=%s' % team1 + ' team2=%s' % team2)
       #AI model work here
       return render_template('index.html', team1 = team1, team2 = team2)
   else:
       print('Request for teams received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
