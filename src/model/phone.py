class Phone:

    def __init__(self, entered_form, description=''):
        self.entered_form = entered_form
        self.description = description

    @property
    def standard_form(self):
        raise NotImplementedError
