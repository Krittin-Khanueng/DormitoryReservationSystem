from dorm.models import Dormitory


def all_dormitory(self):
    dorms = Dormitory.objects.all().values("name")
    return dict(dorms=dorms)
