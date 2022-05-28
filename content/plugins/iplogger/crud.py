from .models import IPLog


def create_record(ip: int):
    query = IPLog.create(ip=ip)

    return query


def get_record(ip: int):
    query = IPLog.get_or_none(ip)

    return query
