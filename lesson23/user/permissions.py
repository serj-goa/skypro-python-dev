from rest_framework import permissions
from user.models import User
from ads.models import Ad


class AdUpdateDeletePermission(permissions.BasePermission):
    message = 'The owner, moderator or admin can update or delete an ad.'

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.author_id:
            return True
        elif request.user.role == User.ADMIN or request.user.role == User.MODERATOR:
            return True
        else:
            return False