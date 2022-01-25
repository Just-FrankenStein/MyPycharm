
get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()



def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "in", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "for", "The", "she", "him", "his", "her",
                           "hers", "its", "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE
    rslt = {}
    f = file_contents.split()
    for word in f:
        if word in uninteresting_words:
            pass
        elif word not in uninteresting_words:
            for letter in word:
                if letter in punctuations:
                    letter.replace(punctuations, "")
            if word not in rslt.keys():
                rslt[word] = 0
            else:
                rslt[word] += 1
    # print(result)

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(rslt)
    return cloud.to_array()

myimage = calculate_frequencies("SMS technology originated from radio telegraphy in radio memo pagers that used standardized phone protocols. "
                                "These were defined in 1986 as part of the Global System for Mobile. "
                                "The origins of the internet date back to the development of packet swtiching "
                                "and research commissioned by the United States Department of Defense in the 1960s "
                                "to enable time-sharing of computers. The primary precursor netwrok, the ARPANET, initially served as a back bone for interconnection"
                                " of regional academic and military networks in the 1970s. The development of new networking technologies, and merger of many networks.")
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()