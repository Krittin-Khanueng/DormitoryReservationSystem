from dorm.models import Dormitory


def all_dormitory(self):
    dorms = Dormitory.objects.all()
    return dict(dorms=dorms)
