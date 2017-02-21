from flask import render_template
from flask import request
from flask import redirect
from models.BuildDb import BuildDb
from models.PsqlHandler import PsqlHandler
from models.Status import *
from models.UserStories import UserStories
from models.DataValidator import DataValidator


class StoryController:

    def __init__(self):
        self.psql_handler = PsqlHandler()
        self.psql_handler.connect()

        self.build_db = BuildDb(self.psql_handler.db)
        self.build_db.start()

        self.url_rule = str(request.url_rule)

    def new(self):
        all_status = Status.get_all_status()
        return render_template("form_new_story.html", all_status=all_status, url_rule=self.url_rule)

    def add(self):
        post_values = request.form
        all_status = Status.get_all_status()

        error = DataValidator().new_story_validator(
            post_values['title'],
            post_values['story'],
            post_values['acceptance'],
            post_values['business_value'],
            post_values['estimation'],
            post_values['status']
        )

        if error["value"] is False:
            UserStories.create(
                story_title=post_values['title'],
                user_story=post_values['story'],
                acceptance_criteria=post_values['acceptance'],
                business_value=post_values['business_value'],
                estimation=post_values['estimation'],
                status=post_values['status']
            )

        return render_template("form_after_insert.html", all_status=all_status, error=error, url_rule=self.url_rule)

    def update_form(self, story_id):
        all_status = Status.get_all_status()
        story = UserStories.get_story(story_id)
        return render_template("form_update.html", story=story, url_rule=self.url_rule, all_status=all_status)

    def update(self, story_id):
        post_values = request.form
        all_status = Status.get_all_status()

        error = DataValidator().new_story_validator(
            post_values['title'],
            post_values['story'],
            post_values['acceptance'],
            post_values['business_value'],
            post_values['estimation'],
            post_values['status']
        )

        if error["value"] is False:
            story = UserStories.select().where(UserStories.id == story_id).get()
            story.story_title = post_values['title']
            story.user_story = post_values['story']
            story.acceptance_criteria = post_values['acceptance']
            story.business_value = post_values['business_value']
            story.estimation = post_values['estimation']
            story.status = post_values['status']
            story.save()

        story = UserStories.get_story(story_id)
        return render_template(
            "form_update_after.html",
            error=error,
            story=story,
            url_rule=self.url_rule,
            all_status=all_status
        )

    def select_all(self):
        all_stories = UserStories.get_all_story()
        return render_template("list_stories.html", all_stories=all_stories, url_rule=self.url_rule)

    def delete_story(self, story_id):
        story = UserStories.get(UserStories.id == story_id)
        story.delete_instance()
        return redirect("/")
