## Flask Application Design

### HTML Files
- `index.html`: This file serves as the application's entry point. It displays a simple interface that users can navigate to interact with the application.
- `news_articles.html`: This file displays a list of recent news articles retrieved from an external API.

### Routes
- `/`: This route renders the `index.html` file.
- `/news_articles`: This route fetches news articles from an external API and renders the `news_articles.html` file with the retrieved articles.