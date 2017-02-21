class DataValidator:

    def __init__(self):
        self.error = {
            "messages": [],
            "value": False
        }

    def new_story_validator(self, story_title, user_story, acceptance_criteria, business_value, estimation, status):
        self.check_empty_string(story_title, "Story title")
        self.check_empty_string(user_story, "User story")
        self.is_integer(business_value, "Business value")
        self.convert_to_float(estimation, "Estimation")
        self.is_integer(status, "Status")

        return self.error

    def check_empty_string(self, string, error_message_prefix):
        if string.strip() == "":
            self.error["messages"].append(error_message_prefix+" is empty!")
            self.error["value"] = True

    def convert_to_float(self, number, error_message_prefix):
        try:
            converted_number = float(number)
        except Exception:
            self.error["messages"].append(error_message_prefix+" is not a number!")
            self.error["value"] = True
            return False
        else:
            return converted_number

    def is_integer(self, number, error_message_prefix):
        converted_number = self.convert_to_float(number, error_message_prefix)

        if converted_number:
            if not converted_number.is_integer():
                self.error["messages"].append(error_message_prefix+" is not an integer!")
                self.error["value"] = True

    def is_not_integer(self, number, error_message_prefix):
        converted_number = self.convert_to_float(number, error_message_prefix)

        if converted_number:
            if converted_number.is_integer():
                self.error["messages"].append(error_message_prefix+" is not a float!")
                self.error["value"] = True
