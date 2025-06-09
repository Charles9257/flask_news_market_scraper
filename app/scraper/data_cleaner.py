def clean_article_data(raw_articles):
    return [
        {
            "title": a["title"].strip(),
            "link": a["link"],
        }
        for a in raw_articles
        if a.get("title") and a.get("link")
    ]
