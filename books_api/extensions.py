from supabase import create_client

supabase = None

def init_supabase(app):
    global supabase
    supabase_url = app.config['SUPABASE_URL']
    supabase_key = app.config['SUPABASE_KEY']
    supabase = create_client(supabase_url, supabase_key)
    return supabase