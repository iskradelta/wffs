# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from hayfind.models import IncludePaths, WfsEntry
import os
from pwd import getpwuid
from grp import getgrgid
import magic
import datetime

def default(request):
    return render_to_response('index.html', {'default': True}, context_instance=RequestContext(request))

def settings(request):
    return render_to_response('settings.html', {'default': True}, context_instance=RequestContext(request))

def save(the_path=None, stated=None):
    if the_path is not None and stated is not None:
        entry = WfsEntry(
            path=the_path,
            size=stated.st_size,
            owner=getpwuid(stated.st_uid).pw_name,
            group=getgrgid(stated.st_gid).gr_name,
            is_dir=os.path.isdir(the_path),
            file_type=magic.from_file(the_path),
            atime=datetime.datetime.fromtimestamp(stated.st_atime),
            ctime=datetime.datetime.fromtimestamp(stated.st_ctime))
        entry.save()
        print "performed save"
    else:
        print "the path or stated was None!"

def updatedb(request):
    include_path = IncludePaths.objects.all()
    for path in include_path:
        for root, dirs, files in os.walk(path):
            print "walkin in cluded path"
            print include_path
    
    for root, dirs, files in os.walk('.'):
        for a_dir in dirs:
            the_path = os.path.join(root, a_dir)
            stated = os.stat(the_path)
            save(the_path, stated)
            print "saved dir"
        for a_file in files:
            the_path = os.path.join(root, a_file)
            stated = os.stat(the_path)
            save(the_path, stated)
            print "saved file"

def find(request):
    print "lol"
    term = request.GET.get('term', None)
    # in_path = request.GET.get('in_path', None)
    # order_by = request.GET.get('order_by', None)
    # file_type = request.GET.get('file_type', None) # fuzzy for hay-find later
    # ends_with = request.GET.get('ends_with', None) # path__endswith=ends_with
    print term
    found_entries = WfsEntry.objects.all().filter(path__contains=term)
    print "matches finished it is"
    print found_entries

    return render_to_response('snippets/result_list.html',
            {'default': True, 'found_entries': found_entries },
                              context_instance=RequestContext(request))

def adv_search(request):
    return render_to_response('snippets/na.html', context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))
def contact(request):
    return render_to_response('contact.html', context_instance=RequestContext(request))