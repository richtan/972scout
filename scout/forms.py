from django import forms
import json
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset, HTML, Div, Field
import tbapy
from .models import *

class PitInputForm(forms.ModelForm):
    scouter_id = forms.IntegerField(min_value=1, max_value=999999)
    team_number = forms.IntegerField(min_value=1, max_value=9999)

    drive_train = forms.ChoiceField(
        choices=(
            ("S", "Swerve"),
            ("W", "West Coast Drive"),
            ("M", "Mecanum"),
            ("H", "H-Drive"),
            ("OD", "Omni Drive"),
            ("O", "Other"),
        )
    )

    outtake_bottom = forms.BooleanField(required=False)
    outtake_outer = forms.BooleanField(required=False)
    outtake_inner = forms.BooleanField(required=False)

    ground_intake = forms.BooleanField(required=False)
    port_intake = forms.BooleanField(required=False)
    robot_intake = forms.BooleanField(required=False)

    climb_level = forms.ChoiceField(
        choices=(
            (1, "Low Climb"),
            (2, "Middle Climb"),
            (3, "High Climb"),
        ),
        required=False,
    )
    buddy_climb = forms.ChoiceField(
        choices=(
            (0, "None"),
            (1, "Carry 1 Other"),
            (2, "Carry 2 Others"),
        ),
        required=False,
    )

    class Meta():
        model = Robot
        fields = (
            "scouter_id",
            "team_number",

            "drive_train",

            "outtake_bottom",
            "outtake_outer",
            "outtake_inner",

            "ground_intake",
            "port_intake",
            "robot_intake",

            "climb_level",
            "buddy_climb",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {'novalidate': 'novalidate'}
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'General Info',
                Field('scouter_id', autofocus='autofocus'),
                Row(
                    Column('team_number', css_class='col-lg col-12'),
                    Column('drive_train', css_class='col-lg col-12'),
                ),
            ),
            HTML('<hr>'),
            Fieldset(
                'Outtake',
                Row(
                    Column('outtake_bottom', css_class='col-lg-2'),
                    Column('outtake_outer', css_class='col-lg-2'),
                    Column('outtake_inner', css_class='col-lg-2'),
                ),
            ),
            HTML('<hr>'),
            Fieldset(
                'Intake',
                Row(
                    Column('ground_intake', css_class='col-lg-2'),
                    Column('port_intake', css_class='col-lg-2'),
                    Column('robot_intake', css_class='col-lg-2'),
                ),
            ),
            HTML('<hr>'),
            Fieldset(
                'Climb',
                Row(
                    Column('climb_level', css_class='col-lg col-12'),
                    Column('buddy_climb', css_class='col-lg col-12'),
                ),
            ),
            Submit('submit', 'Submit'),
        )

class MatchInputForm(forms.ModelForm):
    match_number = forms.IntegerField(min_value=1, max_value=9999)
    team_number = forms.IntegerField(min_value=1, max_value=9999)
    scouter_id = forms.IntegerField(min_value=1, max_value=999999)
    total_balls_preloaded = forms.IntegerField(initial=0, min_value=0, max_value=3)

    # Auto
    crossed_initiation_line = forms.BooleanField(required=False)
    total_bottom_auto_scored = forms.IntegerField(initial=0, min_value=0, max_value=50)
    total_outer_auto_scored = forms.IntegerField(initial=0, min_value=0, max_value=50)
    total_inner_auto_scored = forms.IntegerField(initial=0, min_value=0, max_value=50)

    # Teleop
    total_bottom_teleop_scored = forms.IntegerField(initial=0, min_value=0, max_value=50)
    total_outer_teleop_scored = forms.IntegerField(initial=0, min_value=0, max_value=50)
    total_inner_teleop_scored = forms.IntegerField(initial=0, min_value=0, max_value=50)

    # Offense
    shooting_distance = forms.MultipleChoiceField(
        choices=(
            ("C", "Close"),
            ("M", "Mid"),
            ("T", "Trench"),
        ),
        required=False,
    )

    # Control panel
    total_rotation_tries = forms.IntegerField(initial=0, min_value=0, max_value=21)
    rotation_succeeded = forms.BooleanField(required=False)
    total_position_tries = forms.IntegerField(initial=0, min_value=0, max_value=21)
    position_succeeded = forms.BooleanField(required=False)

    # Climb
    climb_height = forms.ChoiceField(
        choices=(
            (0, "None"),
            (1, "Low"),
            (2, "Middle"),
            (3, "High"),
        ),
    )
    climb_position = forms.ChoiceField(
        choices=(
            ("N", "None"),
            ("C", "Center"),
            ("S", "Side"),
        ),
    )
    parked = forms.BooleanField(required=False)
    fell_down = forms.BooleanField(required=False)
    buddy_climb = forms.ChoiceField(
        choices=(
            (0, "None"),
            (2, "Successfully Lifted 2 Others"),
            (1, "Successfully Lifted 1 Other"),
            (-1, "Got Lifted Successfully"),
        ),
        required=False,
    )
    adjusts_position_on_bar = forms.BooleanField(required=False)

    # Defense
    defense_played = forms.ChoiceField(
        choices=(
            (0, "No defense"),
            (1, "Poor defense"),
            (2, "Moderate defense"),
            (3, "Good defense")
        ),
    )
    defense_handling = forms.ChoiceField(
        choices=(
            (0, "Not defended against"),
            (1, "Handled defense poorly"),
            (2, "Handled defense moderately"),
            (3, "Handled defense well"),
        ),
    )

    # Other
    has_technical_issues = forms.BooleanField(required=False)
    comments = forms.CharField(max_length=2000, widget=forms.Textarea(), required=False)

    class Meta:
        model = Match
        fields = (
            "match_number",
            "team_number",
            "scouter_id",

            "total_balls_preloaded",

            "crossed_initiation_line",
            "total_bottom_auto_scored",
            "total_outer_auto_scored",
            "total_inner_auto_scored",

            "total_bottom_teleop_scored",
            "total_outer_teleop_scored",
            "total_inner_teleop_scored",

            "shooting_distance",

            "total_rotation_tries",
            "rotation_succeeded",
            "total_position_tries",
            "position_succeeded",

            "climb_height",
            "climb_position",
            "parked",
            "fell_down",
            "buddy_climb",
            "adjusts_position_on_bar",

            "defense_played",
            "defense_handling",

            "has_technical_issues",
            "comments",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {'novalidate': 'novalidate'}
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'General Info',
                Field('scouter_id', autofocus='autofocus'),
                Row(
                    Column('match_number', css_class='col-lg col-12'),
                    Column('team_number', css_class='col-lg col-12'),
                ),
            ),
            HTML('<hr>'),
            Fieldset(
                'Pre Game',
                'total_balls_preloaded',
            ),
            HTML('<hr>'),
            Fieldset(
                'Auto',
                'crossed_initiation_line',
                Row(
                    Column('total_inner_auto_scored', css_class='col-lg col-12'),
                    Column('total_outer_auto_scored', css_class='col-lg col-12'),
                    Column('total_bottom_auto_scored', css_class='col-lg col-12'),
                ),
            ),
            HTML('<hr>'),
            Fieldset(
                'Teleop',
                Row(
                    Column('total_inner_teleop_scored', css_class='col-lg col-12'),
                    Column('total_outer_teleop_scored', css_class='col-lg col-12'),
                    Column('total_bottom_teleop_scored', css_class='col-lg col-12'),
                ),
            ),
            HTML('<hr>'),
            Fieldset(
                'Offense',
                Field('shooting_distance'),
            ),
            HTML('<hr>'),
            Fieldset(
                'Control Panel',
                Row(
                    Column('total_rotation_tries', css_class='col-lg col-12'),
                    Column('total_position_tries', css_class='col-lg col-12'),
                ),
                Row(
                    Column('rotation_succeeded', css_class='col-lg'),
                    Column('position_succeeded', css_class='col-lg'),
                ),
            ),
            HTML('<hr>'),
            Fieldset(
                'Endgame',
                Row(
                    Column('climb_height', css_class='col-lg col-12'),
                    Column('climb_position', css_class='col-lg col-12'),
                    Column('buddy_climb', css_class='col-lg col-12'),
                ),
                'parked',
                'fell_down',
                'adjusts_position_on_bar',
            ),
            HTML('<hr>'),
            Fieldset(
                'Defense',
                Row(
                    Column('defense_handling', css_class='col-lg col-12'),
                    Column('defense_played', css_class='col-lg col-12'),
                ),
            ),
            HTML('<hr>'),
            Fieldset(
                'Other',
                'comments',
                'has_technical_issues',
            ),
            Submit('submit', 'Submit'),
        )

    def clean(self):
        cleaned_data = super().clean()

        # Check if match number and team numbers are valid
        match_number = cleaned_data.get("match_number")
        team_number = cleaned_data.get("team_number")
        tba = tbapy.TBA(settings.TBA_API_KEY)
        if int(match_number) not in [int(match["match_number"]) for match in tba.event_matches(settings.TBA_2020SF_EVENT_KEY, simple=True)]:
                self.add_error("match_number", "Match not found")
        if match_number and team_number:
            try:
                if int(match_number) not in [int(match["match_number"]) for match in tba.team_matches(team_number, settings.TBA_2020SF_EVENT_KEY, simple=True)]:
                    self.add_error(None, "Team is not playing in match")
            except:
                self.add_error("team_number", "Team not found")

        # Check scouter ID
        scouter_id = str(cleaned_data.get("scouter_id"))
        if len(scouter_id) == 6 and scouter_id[:2] == "11":
            scouter_id = scouter_id[2:]
        if len(scouter_id) not in range(1, 5):
            self.add_error("scouter_id", "Invalid scouter ID")

        return cleaned_data

    def save(self, commit=True):
        match = super().save(commit=False)

        # Shooting distance
        shooting_distance = self.cleaned_data.get("shooting_distance")
        match.shoots_close = "C" in shooting_distance
        match.shoots_mid = "M" in shooting_distance
        match.shoots_trench = "T" in shooting_distance

        # Scouter ID
        scouter_id = str(self.cleaned_data.get("scouter_id"))
        if len(scouter_id) == 6:
            scouter_id = scouter_id[2:]
        match.scouter_id = int(scouter_id.zfill(4))

        if commit:
            match.save()
        return match
