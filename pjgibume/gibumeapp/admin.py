from django.contrib import admin

from .models import Perfume
from .models import Comment
from .models import User
from .models import Community
from .models import CommunityComment
from .models import *

admin.site.register(Perfume)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Community)
admin.site.register(CommunityComment)


