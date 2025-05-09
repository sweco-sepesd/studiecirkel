# -*- coding: utf-8 -*-
import os, sys, subprocess, collections

#reload(sys)
#sys.setdefaultencoding('iso-8859-1')

def hello(**kwargs):
    Artist = ""
    Album = ""
    Format = ""
    for k,v in kwargs.items():
        #print(str(k)+":"+str(v))
        if k == "Artist":
            Artist = v
        if k == "Album":
            Album = v
        if k == "Format":
            Format = v
    
    #Fetch eventual command line parameters
    #Commented since change to keyword arguments
    # arg_names = ['File', 'Artist', 'Album', 'Format']
    # args = dict(zip(arg_names, sys.argv))
    # Arg_list = collections.namedtuple('Arg_list', arg_names)
    # args = Arg_list(*(args.get(arg, None) for arg in arg_names))
    
    #If command line arguments exists assign these to the correct variables
    #Commented since change to keyword arguments
    # if args.Artist is not None:
        # Artist = args.Artist
    # if args.Album is not None:
        # Album = args.Album
    # if args.Format is not None:
        # Format = args.Format
    
    def guess_fme_home():
        for folder in [
                  r'C:\Program Files\FME2024.2'
                , r'C:\Program Files\FME2024'
                , r'C:\Program Files\FME']:
            if os.path.exists(os.path.join(folder, 'fme.exe')):
                return folder
    #Fetch FME path from system variable FME_HOME, and if this don't exists test for likely folders that FME 2024 might reside in.
    fme_home = os.environ.get("FME_HOME", guess_fme_home())
    FmePath = None
    if fme_home is not None:
        FmePath = os.path.join(fme_home, 'fme.exe')
    
    #Default values for search filter, resulting in favorite record from Discogs
    if Artist == "" and Album == "" and Format == "":
        Artist="Kraftwerk"
        Album="Trans Europa Express"
        Format="Vinyl"
    
    #Calling FME as a python subprocess if path to a FME installation has been found on the system
    if FmePath:
        fme_workspace = os.path.join(os.path.dirname(__file__), 'FetchRecords.fmw')
        cmd= """\"%s\" \"%s\" --Artist \"%s\" --Album \"%s\" --Format \"%s\" --FME_LAUNCH_VIEWER_APP \"NO\"""" % (FmePath, fme_workspace, Artist, Album, Format)
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        process.wait()
        #Read text file created by FME
        try:
            file = open('Records.txt', mode = 'r')
            lines = file.readlines()
            file.close()
            editions = []
            skivor = []
            #print(lines)
            for line in lines:
                type = line.split('-')[1].split('(')[2].split(')')[0].strip()
                year = line.split('-')[1].split('(')[1].strip()
                favoritskiva = line.split('(')[0].strip()
                edition = year + '(' + type + ')'
                skivor.append(favoritskiva + '(' + type + ') (' + year + ')')
                editions.append(edition)
                pass
            if Artist == "Kraftwerk" and Album == "Trans Europa Express":
                result = 'Hej,\nDetta är resultatet av Hans bidrag till python-projektet.\nMin favoritskiva är ' + favoritskiva + '.\nJag har dessa utgåvor av skivan:\n' + '\n'.join(editions) +'\n(Informationen hämtad från Discogs)'
            else:
                result = 'Hej,\nDetta är resultatet av Hans bidrag till python-projektet.\nHär är några av mina bästa skivor med ' + Artist + ':\n' + '\n'.join(skivor) + '\n(Informationen hämtad från Discogs)'
        except:
            result = 'Hej,\nDetta är resultatet av Hans bidrag till python-projektet.\nVi lyckades tyvärr inte hämta någon information från Discogs för Hans.'
    else:
        result = 'Hej,\nDetta är resultatet av Hans bidrag till python-projektet.\nVi lyckades tyvärr inte hämta någon information från Discogs för Hans pga att systemet saknar installation av FME 2024.2 eller senare.'
    return(result)
