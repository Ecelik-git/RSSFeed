import feedparser

#enter rss url
NewsFeed = feedparser.parse(input("Enter RSS: "))

print('Number of RSS posts :', len(NewsFeed.entries))

for i in range(len(NewsFeed.entries)):
  entry = NewsFeed.entries[i]
  #printing title, description and link
  print('Post Title :',entry.title)
  print('Post Description :',entry.description)
  print('Post link :',entry.link)
