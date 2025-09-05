fig.update_layout(
    title_font=dict(size=24, family="Arial"),
    plot_bgcolor="lightgray",
    xaxis_tickangle=-45
)

for repo in data["items"]:
    print(f"{repo['name']} - {repo['owner']['login']} - {repo['html_url']}")
