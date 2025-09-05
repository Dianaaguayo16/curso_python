import requests
import plotly.graph_objects as go

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
top_ids = requests.get(url).json()[:30]

titles = []
comments = []

for story_id in top_ids:
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    try:
        story_data = requests.get(story_url).json()
        title = story_data["title"]
        comment_count = story_data.get("descendants", 0)
        titles.append(f"{title}\n{comment_count} comments")
        comments.append(comment_count)
    except KeyError:
        continue

fig = go.Figure(data=[go.Bar(x=titles, y=comments)])
fig.update_layout(title="Most Active Hacker News Discussions", xaxis_title="Title", yaxis_title="Comments")
fig.show()
