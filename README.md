# About
If you're in the situation that you have an authenticated Django view that returns
files for download, you may have noticed that Safari 9.x doesn't play audio files
properly when returning audio-files. The reason is that Safari sends a HTTP_RANGE request header and expects a proper `Content-Range` response header in return.
There is a [Django ticket](https://code.djangoproject.com/ticket/22479)
for this, however no indication that this feature will be implemented soon.

The [original suggested fix](https://github.com/satchamo/django/commit/2ce75c5c4bee2a858c0214d136bfcd351fcde11d)
applies the code to Django's static view. This is a packaged version of that fix,
but uses a modified FileResponse, instead of applying it to Django's static view.
You can use it for custom views like:

    from ranged_fileresponse import RangedFileResponse

    def some_proxy_view(request):
        filename = 'myfile.wav'
        response = RangedFileResponse(open(filename, 'r'), request, content_type='audio/wav')
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
