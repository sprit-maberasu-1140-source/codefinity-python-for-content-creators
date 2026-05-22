def generate_engagement_report():
    engagement_data = [
        {"day": "Monday", "views": 120, "likes": 25, "comments": 8},
        {"day": "Tuesday", "views": 150, "likes": 30, "comments": 10},
        {"day": "Wednesday", "views": 200, "likes": 50, "comments": 20},
        {"day": "Thursday", "views": 90,  "likes": 15, "comments": 5},
        {"day": "Friday",   "views": 175, "likes": 40, "comments": 15},
        {"day": "Saturday", "views": 220, "likes": 60, "comments": 25},
        {"day": "Sunday",   "views": 180, "likes": 35, "comments": 12}
    ]

    total_views = sum(item["views"] for item in engagement_data)
    total_likes = sum(item["likes"] for item in engagement_data)
    average_likes = total_likes / len(engagement_data)
    highest_engagement = max(
        engagement_data,
        key=lambda x: x["likes"] + x["comments"]
    )
    highest_day = highest_engagement["day"]
    highest_total = highest_engagement["likes"] + highest_engagement["comments"]

    report = (
        "=== Weekly Engagement Summary Report ===\n"
        f"Total Views: {total_views}\n"
        f"Average Likes per Day: {average_likes:.2f}\n"
        f"Highest Engagement Day: {highest_day} ({highest_total} total interactions)\n"
    )

    print(report)

generate_engagement_report()