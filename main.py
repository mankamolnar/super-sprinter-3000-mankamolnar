from flask import *
from controllers.StoryController import StoryController
app = Flask(__name__, template_folder='view')


@app.route('/story', methods=['GET'])
def new():
    return StoryController().new()


@app.route('/story', methods=['POST'])
def add():
    return StoryController().add()


@app.route('/story/<int:story_id>', methods=['GET'])
def update_story_form(story_id):
    return StoryController().update_form(story_id)


@app.route('/story/<int:story_id>', methods=['POST'])
def update_story(story_id):
    return StoryController().update(story_id)


@app.route('/')
@app.route('/list')
def all_story():
    return StoryController().select_all()


@app.route('/delete/<int:story_id>')
def delete_story(story_id):
    return StoryController().delete_story(story_id)


if __name__ == '__main__':
    app.run()
