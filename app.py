from pj_match_history.api import create_app
from werkzeug.serving import run_simple

app = create_app()

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)