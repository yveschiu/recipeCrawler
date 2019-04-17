# recipeCrawler

---

## Crawler for studying

### Steps:

1. ```icook_recipes_urls_crawler.ipynb``` will fetch all recipe-urls except vip-recipes in https://icook.tw/ and save them as an url_list file

2. ```icook_recipes_crawler_threading.ipynb``` will use the url_list file to fetch all recipe data using threading module to accelerate the crawling speed.

3. ```jsonTransformation.ipynb``` transforms the json structure of recipe as we modified some storage details.

4. ```mongodb_recipes_insertion.ipynb``` inserts all recipes into MongoDB for further uses.

5. ```recipe_model_predict_and_query_mongo.ipynb``` defines a class named 'ShoppingCart' to predict a model_tag for recipe recommendation.