from googlesearch import search
def linksearch(perameterlist):
   link_list = []
   subject = 'Black entrepreneur '
   for j in perameterlist:
      for i in search(subject +j,  tld='com', lang='en', num=1, start=0, stop=3, pause=2.0):
         link_list.append(i)
   return link_list

def webinarsearch(perameterlist):
   link_list = []
   subject = 'Entrepreneurship Webinar '
   for j in perameterlist:
      if not perameterlist:
         for i in search(subject,  tld='com', lang='en', num=1, start=0, stop=3, pause=2.0):
            link_list.append(i)
      else:
         for i in search(subject +j,  tld='com', lang='en', num=1, start=0, stop=3, pause=2.0):
            link_list.append(i)
   return link_list





   
# stored queries in a list
query_list=['support', 'loan', 'guidance', 'opportunity']
