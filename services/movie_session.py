from django.db.models import QuerySet
from datetime import datetime

from typing import Optional

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: Optional[str] = None) -> QuerySet:
    sessions = MovieSession.objects.all()

    if session_date:
        sessions = sessions.filter(show_time__date=session_date)

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    update_fields = {}

    if show_time:
        update_fields["show_time"] = show_time
    if movie_id:
        update_fields["movie_id"] = movie_id
    if cinema_hall_id:
        update_fields["cinema_hall_id"] = cinema_hall_id
    if not update_fields:
        return None

    MovieSession.objects.filter(pk=session_id).update(**update_fields)


def delete_movie_session_by_id(session_id: int) -> int:
    deleted_session, _ = get_movie_session_by_id(session_id).delete()
    return deleted_session
