import re

from rest_framework import serializers


class TitleValidator:

    def __init__(self, field):
        self.field = field
        print('init')

    def __call__(self, value):
        reg = re.compile('^[a-zA-Z0-9\.\-\ ]+$')
        temp_val = dict(value).get(self.field)
        print(temp_val)
        if not bool(reg.match(temp_val)):
            raise serializers.ValidationError('Title is not ok')
