 
from app.utils.logger import setup_logger
from flask import Blueprint, render_template
from app.db.models import Article



logger = setup_logger(__name__)

main_bp = Blueprint('main', __name__)

 

@main_bp.route('/')
def index():
    logger.info("GET / called")
    try:
        articles = Article.query.order_by(Article.id.desc()).limit(10).all()
        logger.info(f"Fetched {len(articles)} articles for index")
        return render_template('index.html', articles=articles)
    except Exception as e:
        logger.error(f"Error fetching articles for index: {e}", exc_info=True)
        return render_template('error.html', error="Failed to fetch articles"), 500
    

@main_bp.route('/about')
def about():
    logger.info("GET /about called")
    return render_template('about.html')