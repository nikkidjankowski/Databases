"""Forms for playlist app."""


from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Name", validators=[
                       InputRequired(message="Name can't be blank")])
    description = StringField("Description")
    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField("Title", validators=[
                       InputRequired(message="title can't be blank")])
    artist = StringField("Artist", validators=[
                       InputRequired(message="Artist can't be blank")])
    
    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
