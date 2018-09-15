from flask import Flask
import random
import subprocess
app = Flask(__name__)

@app.route("/")
def palacsinta():
  subprocess.Popen(["omxplayer", "sounds/%s.mp3" % random.randint(1,3)])
  return "Csintalan palacsinta!"

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')