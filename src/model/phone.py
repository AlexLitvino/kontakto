class Phone:
    """Class that keeps specific phone number"""

    def __init__(self, entered_form, description=''):
        self.entered_form = entered_form
        self.standard_form = Phone.to_standard_form(entered_form)
        self.description = description

    @staticmethod
    def to_standard_form(phone: str) -> str:
        """
        Method transforms entered phone to standard form
        (without leading plus sign, whitespaces and hyphens for easier search)
        """
        return (phone
                .replace('+', '')
                .replace(' ', '')
                .replace('-', ''))
