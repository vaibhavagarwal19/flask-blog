from flaskblog import app,db

# Create the database schema
# with app.app_context():
#     db.create_all()

# Start your Flask application
if __name__ == "__main__":
    app.run(debug=True)