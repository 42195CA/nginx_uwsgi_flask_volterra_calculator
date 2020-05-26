from wtforms import Form, FloatField, validators

class InputForm(Form):
    k = FloatField(
        label='shape parameter', 
        default=1.37,
        validators=[validators.InputRequired()])
    l = FloatField(
        label='scale parameter', 
        default=1228,
        validators=[validators.InputRequired()])
    t = FloatField(
        label='month', default=60,
        validators=[validators.InputRequired()])
    # w = FloatField(
    #     label='Answer', default=1,
    #     validators=[validators.InputRequired()])