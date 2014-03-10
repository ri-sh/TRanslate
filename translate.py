
-------------------------------------------------------------------------------
# Name:        translate.py
# Purpose:      translating strings using microsofts api 
#
# Author:      Rishabh
#
# Created:     27/02/2014
# Copyright:   (c) rishabh 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

""" for windows Install lxml from http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml"""


"""

Functions to access the Microsoft Translator API HTTP Interface, using python's urllib/urllib2 libraries

"""

import urllib, urllib2
import json

from datetime import datetime

def datestring (display_format="%a, %d %b %Y %H:%M:%S", datetime_object=None):
    """Convert the datetime.date object (defaults to now, in utc) into a string, in the given display format"""
    if datetime_object is None:
        datetime_object = datetime.utcnow()
    return datetime.strftime(datetime_object, display_format)

def get_access_token (client_id, client_secret):
    """Make an HTTP POST request to the token service, and return the access_token,
    as described in number 3, here: http://msdn.microsoft.com/en-us/library/hh454949.aspx
    """

    data = urllib.urlencode({
            'client_id' : client_id,
            'client_secret' : client_secret,
            'grant_type' : 'client_credentials',
            'scope' : 'http://api.microsofttranslator.com'
            })

    try:

        request = urllib2.Request('https://datamarket.accesscontrol.windows.net/v2/OAuth2-13')
        request.add_data(data)

        response = urllib2.urlopen(request)
        response_data = json.loads(response.read())

        if response_data.has_key('access_token'):
            return response_data['access_token']

    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print datestring(), 'Could not connect to the server:', e.reason
        elif hasattr(e, 'code'):
            print datestring(), 'Server error: ', e.code
    except TypeError:
        print datestring(), 'Bad data from server'

supported_languages = { # as defined here: http://msdn.microsoft.com/en-us/library/hh456380.aspx
    'ar' : ' Arabic',
    'bg' : 'Bulgarian',
    'ca' : 'Catalan',
    'zh-CHS' : 'Chinese (Simplified)',
    'zh-CHT' : 'Chinese (Traditional)',
    'cs' : 'Czech',
    'da' : 'Danish',
    'nl' : 'Dutch',
    'en' : 'English',
    'et' : 'Estonian',
    'fi' : 'Finnish',
    'fr' : 'French',
    'de' : 'German',
    'el' : 'Greek',
    'ht' : 'Haitian Creole',
    'he' : 'Hebrew',
    'hi' : 'Hindi',
    'hu' : 'Hungarian',
    'id' : 'Indonesian',
    'it' : 'Italian',
    'ja' : 'Japanese',
    'ko' : 'Korean',
    'lv' : 'Latvian',
    'lt' : 'Lithuanian',
    'mww' : 'Hmong Daw',
    'no' : 'Norwegian',
    'pl' : 'Polish',
    'pt' : 'Portuguese',
    'ro' : 'Romanian',
    'ru' : 'Russian',
    'sk' : 'Slovak',
    'sl' : 'Slovenian',
    'es' : 'Spanish',
    'sv' : 'Swedish',
    'th' : 'Thai',
    'tr' : 'Turkish',
    'uk' : 'Ukrainian',
    'vi' : 'Vietnamese',
}

def print_supported_languages ():
    """Display the list of supported language codes and the descriptions as a single string
    (used when a call to translate requests an unsupported code)"""

    codes = []
    for k,v in supported_languages.items():
        codes.append('\t'.join([k, '=', v]))
    return '\n'.join(codes)

def to_bytestring (s):
    """Convert the given unicode string to a bytestring, using utf-8 encoding,
    unless it's already a bytestring"""

    if s:
        if isinstance(s, str):
            return s
        else:
            return s.encode('utf-8')

def translate (access_token, text, to_lang, from_lang=None):
    """Use the HTTP Interface to translate text, as described here:
    http://msdn.microsoft.com/en-us/library/ff512387.aspx
    and return an xml string if successful
    """

    if not access_token:
        print 'Sorry, the access token is invalid'
    else:
        if to_lang not in supported_languages.keys():
            print 'Sorry, the API cannot translate to', to_lang
            print 'Please use one of these instead:'
            print print_supported_languages()
        else:
            data = { 'text' : to_bytestring(text), 'to' : to_lang }

            if from_lang:
                if from_lang not in supported_languages.keys():
                    print 'Sorry, the API cannot translate from', from_lang
                    print 'Please use one of these instead:'
                    print print_supported_languages()
                    return
                else:
                    data['from'] = from_lang

            try:

                request = urllib2.Request('http://api.microsofttranslator.com/v2/Http.svc/Translate?'+urllib.urlencode(data))
                request.add_header('Authorization', 'Bearer '+access_token)

                response = urllib2.urlopen(request)
                return response.read()

            except urllib2.URLError, e:
                if hasattr(e, 'reason'):
                    print datestring(), 'Could not connect to the server:', e.reason
                elif hasattr(e, 'code'):
                    print datestring(), 'Server error: ', e.code

from lxml import etree

def get_text_from_msmt_xml (xml):
#"""Parse the xml string returned by the MS machine translation API, and return just the text """

    text = []
    doc = etree.fromstring(xml)
    for elem in doc.xpath('/foo:string', namespaces={'foo': 'http://schemas.microsoft.com/2003/10/Serialization/'}):
        if elem.text:
            elem_text = ' '.join(elem.text.split())
            if len(elem_text) > 0:

                text.append(elem_text)

    return ' '.join(text)

MY_CLIENT_ID="rishabh"
MY_CLIENT_SECRET="lD0VqGRO2ztRytxw7Gp6myb9SsNqpXm4z4TIRw4vWe4="
#texttrans=raw_input('enter the text to be translated')
text= raw_input('enter the string to be translated ')
text = text.strip()
dest=raw_input("enter Destination language for example hi for hindi ")
dest =dest.strip()
source= raw_input("enter source language for example en for english")
source=source.strip()
#source_lang=raw_input('enter the text to be translated' )
#dest_lang=raw_input('enter_the_language in which text is to be converted')
token = get_access_token(MY_CLIENT_ID, MY_CLIENT_SECRET)
print " translation of " +text+" in "+supported_languages[dest]+" is :"
text= translate(token,text , dest, source)
translated=get_text_from_msmt_xml (text)
print translated
