from flask import Blueprint, jsonify
from app.db.models import Article
from app.utils.logger import setup_logger
 

logger = setup_logger(__name__)

api_bp = Blueprint('api', __name__)
 

@api_bp.route('/articles', methods=['GET'])
def get_articles():
    logger.info("GET /articles called")
    try:
        articles = Article.query.order_by(Article.id.desc()).limit(10).all()
        logger.info(f"Fetched {len(articles)} articles")
        return jsonify([{"title": a.title, "link": a.link} for a in articles])
    except Exception as e:
        logger.error(f"Error fetching articles: {e}", exc_info=True)
        return jsonify({"error": "Failed to fetch articles"}), 500

 
    
 