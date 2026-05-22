def summarize_articles(articles):
    summaries = {}
    for filename, text in articles.items():
        sentences = text.split('. ')
        summary = '. '.join(sentences[:2])
        if not summary.endswith('.'):
            summary += '.'
        summaries[filename] = summary
        print(f"Saving summary as {filename}_summary.txt:")
        print(summary)
        print("---")
    return summaries

articles = {
    "post1.txt": "Python is a versatile language. It is popular among content creators. You can use it for automation. It saves time.",
    "article2.txt": "Batch processing allows you to handle multiple files at once. This is useful for summarizing articles. It can also be used for renaming files. Efficiency is improved.",
    "blog3.txt": "Social media posts benefit from concise summaries. Python scripts can automate this process. Consistency is important for branding.",
}

summaries = summarize_articles(articles)