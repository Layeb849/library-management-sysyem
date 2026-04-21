from django.contrib import admin

from library.models import CommitteeMember, LibraryMember, Review, YearlyAchivement, CommitteeDocument

# Register your models here.
admin.site.register(Review)
admin.site.register(YearlyAchivement)
admin.site.register(CommitteeMember)
admin.site.register(LibraryMember)
admin.site.register(CommitteeDocument)
