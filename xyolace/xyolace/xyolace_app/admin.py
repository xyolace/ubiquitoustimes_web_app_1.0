from django.contrib import admin

from .models import *

admin.site.register((A0PAGETOP,
                    A1NAVBAR,
                    A2TOPPICKS,
                    A3NEWSTODAY,
                    A4HOTPICKS,
                    A5SUBSCRIBENEWS,
                    A6OTHERNEWS,
                    A7ECOANDWORLD,
                    A8LIFESTYLE,
                    A9BOTTOMNAV,
                    B1OURORIGINAL,
                    B2STOREADS,
                    B3WEBSITE_TAGS,
                    B4HORIZONTABANNER,
                    B5KEYWORDS_DES,
                    ))

'''
admin.site.register(A3TOPFEATURED)
admin.site.register(A4NEWPOST)
admin.site.register(A5TOPSTORY)
admin.site.register(A6TRENDINGTOPSTORY)
admin.site.register(A7SUBSCRIBENEWS)
admin.site.register(A9OTHERTRENDINGSTORIES)
admin.site.register(B2MOSTVIEWS)
admin.site.register(B3OTHERNEWS)
admin.site.register(B6STOREADS)
admin.site.register(B7BOTTOMNAV)
admin.site.register(B8IMAGEGALLERY)

'''
