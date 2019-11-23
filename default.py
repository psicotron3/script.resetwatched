# import the kodi python modules we are going to use
# see the kodi api docs to find out what functionality each module provides
import xbmc
import xbmcaddon
import sys

import json


def debug(msg, *args):
    try:
        txt=u''
        msg=unicode(msg)
        for arg in args:
            if type(arg) == int:
                arg = unicode(arg)
            if type(arg) == list:
                arg = unicode(arg)
            txt = txt + u"/" + arg
        if txt == u'':
            xbmc.log(u"WATCH: {0}".format(msg).encode('ascii','xmlcharrefreplace'), xbmc.LOGDEBUG)
        else:
            xbmc.log(u"WATCH: {0}#{1}#".format(msg, txt).encode('ascii','xmlcharrefreplace'), xbmc.LOGDEBUG)
    except:
        print "Error in Debugoutput"
        print msg
        print args
        
        
def sendJSON(command):
        data = xbmc.executeJSONRPC(command)
        return unicode(data, 'utf-8', errors='ignore')

# getting the assetTYPE so we can later confirm that it's a movie or tvshow

assetTYPE = xbmc.getInfoLabel('ListItem.DBtype')
path = xbmc.getInfoLabel('ListItem.FileNameAndPath')
ID = int(xbmc.getInfoLabel('ListItem.DBID'))

debug('assetTYPE', assetTYPE)
debug('path', path)
debug('ID', ID)

#vDir = "/special://profile/addon_data/script.pseudotv/cache/stored/Masala.xsp"



M3Ucount = 0
M3Uresume = 0
M3Ulastplayed = ""



if assetTYPE == 'movie':
    #response = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": {"movieid" : %d, "playcount": %d , "resume": {"position": %d}   }} ' % (ID, count, positionInSecond))
    
    response = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetMovieDetails", "params": {"movieid" : %d, "lastplayed": "%s", "playcount": %d , "resume": {"position": %d}   }} ' % (ID, M3Ulastplayed, M3Ucount, M3Uresume))
    
    
    
    
elif assetTYPE == 'episode':
    #response = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetEpisodeDetails", "params": {"episodeid" : %d, "playcount": %d , "resume": {"position": %d}   }} ' % (ID, count, positionInSecond))
    
    response = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.SetEpisodeDetails", "params": {"episodeid" : %d, "lastplayed": "%s", "playcount": %d , "resume": {"position": %d}   }} ' % (ID, M3Ulastplayed, M3Ucount, M3Uresume))
    
debug('response',response)
 