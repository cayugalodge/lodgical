from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

class S3MediaStorage(S3BotoStorage):
    def __init__(self, **kwargs):
        kwargs['location'] = kwargs.get('location', 
            settings.MEDIA_ROOT.replace('/', ''))
        super(S3MediaStorage, self).__init__(**kwargs)

class S3StaticStorage(S3BotoStorage):
    def __init__(self, **kwargs):
        kwargs['location'] = kwargs.get('location', 
            settings.STATIC_ROOT.replace('/', ''))
        super(S3StaticStorage, self).__init__(**kwargs)