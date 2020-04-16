#YOUTUBE VIDEO DATE ORGANIZER (BY DATE PUBLISHED)


import sys, json
sys.path.append("/Users/Josiah Adrineda/youtube_tutorial/")
from youtube_videos import youtube_search

#Collect data
vid_dict = {'pub_date':[]}
vid_count = 0
def get_vids(keyword, token=None):
    global vid_count
    res = youtube_search(keyword)
    token = res[0]
    vids = res[1]
    for vid in vids:
        vid_dict['pub_date'].append(vid['snippet']['publishedAt'])
        vid_count += 1
    return token

#User input
search = input("Please input what you want to search: ")
token = get_vids(search)

#Repeat searches until certain number of videos have been collected
# Note: Might overload quota!!!
while vid_count < 3000:
    token = get_vids(search, token=token)



#VISUAL REPRESENTATION OF DATA


import numpy as np, matplotlib.pyplot as plt, datetime
from matplotlib.dates import DateFormatter, YearLocator
from matplotlib.pyplot import xlim

start_date = datetime.date(2005, 1, 1)
end_date = datetime.date.today()

#Convert dates published
dates = {}
for date in vid_dict['pub_date']:
    temp = date[:10]
    temp = temp.replace('-', '/')
    temp += '/'
    year = temp[:4]
    temp = temp[5:]
    temp += year
    if temp in dates:
        dates[temp] += 1
    else:
        dates[temp] = 1

#Initialize graph
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("YouTube Videos on '" + search + "'")
ax.set_xlim(start_date, end_date)
ax.set_xlabel("Date Published")
ax.set_ylabel("Frequency")
ax.xaxis.set_major_formatter(DateFormatter('%Y'))
ax.xaxis.set_major_locator(YearLocator(5))
ax.xaxis.set_minor_locator(YearLocator(1))

#Distribute dates and their frequencies to x and y axes of graph
dates_x = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in dates]
frequencies_y = [frequency for frequency in dates.values()]

#Sort data for graph consistency
dates_x.sort(), frequencies_y.sort()

#Observe data specifically before looking at graph (up to personal preference)
print(dates_x, frequencies_y)

#Plot, save, and show graph
ax.plot(dates_x, frequencies_y, c='k')
plt.savefig("youtube_video_date_organizer.png")
plt.show()