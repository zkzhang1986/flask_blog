from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/about/')
def about():
    return 'The about page'

#
# # 看看是周几
# def check_time_alarm(f):
#     import datetime
#
#     def wrapper():
#         d = datetime.datetime.now()
#         weekday = d.weekday()
#         if weekday < 6:
#             f()
#         return
#
#     return wrapper
#
#
# # 闹钟
# def alarm():
#     print('Good good study, Day day up!')
#
# my_alarm = check_time_alarm(alarm)
# my_alarm()

if __name__ == '__main__':
    app.debug = True
    app.run()