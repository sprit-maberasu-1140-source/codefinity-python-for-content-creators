def get_top_performing_content(content_list):
    # Calculate engagement for each post (views + likes)
    for post in content_list:
        post['engagement'] = post['views'] + post['likes']
    # Sort posts by engagement in descending order
    sorted_posts = sorted(content_list, key=lambda x: x['engagement'], reverse=True)
    # Get the top 3 posts
    return sorted_posts[:3]

content_data = [
    {"title": "How to Edit Photos Like a Pro", "views": 1200, "likes": 300},
    {"title": "10 Tips for Better Videos", "views": 950, "likes": 210},
    {"title": "Behind the Scenes: My Studio Setup", "views": 1800, "likes": 400},
    {"title": "Beginner's Guide to Lighting", "views": 750, "likes": 120},
    {"title": "Instagram Growth Hacks", "views": 2100, "likes": 500},
    {"title": "Editing with Mobile Apps", "views": 600, "likes": 80},
    {"title": "Creative Storytelling Ideas", "views": 1700, "likes": 350}
]

top_content = get_top_performing_content(content_data)
for post in top_content:
    summary = f"Title: {post['title']}, Views: {post['views']}, Likes: {post['likes']}, Engagement: {post['engagement']}"
    print(summary)