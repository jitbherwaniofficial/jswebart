# storage_backends.py
import os
from django.core.files.storage import Storage
from supabase import create_client
from django.conf import settings
from urllib.parse import quote_plus

class SupabaseMediaStorage(Storage):
    def __init__(self):
        self.supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    def _open(self, name, mode='rb'):
        # Not needed for Supabase usage
        pass

    def _save(self, name, content):
        # Upload file to Supabase storage
        response = self.supabase.storage.from_(settings.SUPABASE_BUCKET_NAME).upload(
            path=name,
            file=content.file,
            file_options={"content-type": content.content_type},
        )
        if 'error' in response:
            raise Exception(f"Upload failed: {response['error']}")
        return name

    def url(self, name):
        # Return the public URL of the file (Important Fix Here)
        return f"{settings.SUPABASE_URL}/storage/v1/object/public/{settings.SUPABASE_BUCKET_NAME}/{quote_plus(name)}"
