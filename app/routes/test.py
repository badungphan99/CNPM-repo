from app import *
from app.controller import *
from flask import render_template, session, jsonify, request, json


@app.route('/test', endpoint='render_test')
@login_required
def render_test():
    return current_user.id

@app.route('/testajaxxx', endpoint='test_ajax', methods=['GET', 'POST'])
def test_ajax():
    topics = get_topic()

    result = {
        "topic" : []
    }
    for tp in topics :
        result["topic"].append({
            "name" : tp.topic_name,
            "link" : "/testajaxxx/" + str(tp.id)
        })
    return jsonify(result)

@app.route('/testajaxxx/<int:post_id>', endpoint='render_testxxx', methods=['GET', 'POST'])
def render_testxxx(post_id):
    print (post_id == 1)
    if post_id == 1:
        return render_template("block_home.html")
    return render_template("login.html")

# @app.route('/Learning/<int:id>', endpoint='render_learning', methods=['GET', 'POST'])
# def render_learning(id):
#     id = 1
#     return render_template("login.html")