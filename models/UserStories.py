from models.BaseModel import *
from models.Status import *


class UserStories(BaseModel):
    story_title = CharField()
    user_story = TextField()
    acceptance_criteria = TextField()
    business_value = IntegerField()
    estimation = FloatField()
    status = ForeignKeyField(Status, related_name='user_stories')

    @classmethod
    def get_all_story(cls):
        all_stories = cls.select()
        stories = []
        for story in all_stories:
            stories.append({
                "id": story.id,
                "story_title": story.story_title,
                "user_story": story.user_story,
                "acceptance_criteria": story.acceptance_criteria,
                "business_value": story.business_value,
                "estimation": story.estimation,
                "status": story.status.name
            })

        return stories

    @classmethod
    def get_story(cls, id):
        story = cls.select().where(cls.id == id).get()
        story = {
            "id": story.id,
            "story_title": story.story_title,
            "user_story": story.user_story,
            "acceptance_criteria": story.acceptance_criteria,
            "business_value": story.business_value,
            "estimation": story.estimation,
            "status": story.status.id
        }
        return story

