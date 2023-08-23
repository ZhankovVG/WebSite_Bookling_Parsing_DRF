from datetime import datetime, timezone
from django.contrib.sessions.models import Session


def clean_session():
    all_session = Session.objects.all()
    now = datetime.now(timezone.utc)
    for el in all_session:
        if (now - el.expire_date).total_seconds() > 172800:
            el.delete()