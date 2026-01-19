# from flask import Flask
# from app.api.resume_routes import resume_api

# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(resume_api, url_prefix="/api/resume")

#     # Root health route
#     @app.route("/")
#     def health():
#         return {"status": "AI HR Resume Screener API is running"}

#     return app


# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template
from app.api.resume_routes import resume_api

def create_app():
    app = Flask(
        __name__,
        template_folder="../../frontend/templates",  # adjust path if needed
        static_folder="../../frontend/static"
    )

    # Register API blueprint
    app.register_blueprint(resume_api, url_prefix="/api/resume")

    # Root health route
    @app.route("/health", methods=["GET"])
    def health():
        return {"status": "AI HR Resume Screener API is running"}

    # Home route for frontend
    @app.route("/", methods=["GET"])
    def home():
        return render_template("index.html")

    return app


# Create Flask app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
