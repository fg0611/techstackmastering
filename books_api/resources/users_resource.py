from flask import Blueprint, request, jsonify
from flask import current_app

users_bp = Blueprint("users", __name__, url_prefix="/api/users")


@users_bp.route("/signup", methods=["POST"])
def signup_user():
    body = request.get_json()
    email = body.get("email")
    password = body.get("password")

    if not email or not password:
        return jsonify({"error": "bad body"}, 400)

    print(current_app.extensions)

    supabase_client = current_app.extensions.get("supabase")

    print(supabase_client)

    if not supabase_client:
        return jsonify({"error": "Error not getting Supabase client"}), 500

    try:
        # user, error = supabase_client.auth.sign_up(email=email, password=password)
        res = supabase_client.auth.sign_up({"email": email, "password": password})

        print(res)

        if not res:
            return jsonify({"error": "no user created"})
        return jsonify({"message": "user stored"})
    except Exception as e:
        return jsonify({"error": f"{str(e)}"}, 500)


@users_bp.route("/signin", methods=["POST"])
def signin():
    body = request.get_json()
    email = body.get("email")
    password = body.get("password")

    if not email or not password:
        return jsonify({"error": "bad body"}, 400)

    supabase_client = current_app.extensions.get("supabase")

    if not supabase_client:
        return jsonify({"error": "Error not getting Supabase client"}), 500

    try:
        res = supabase_client.auth.sign_in_with_password(body)
        print(res)

        if not res:
            supabase_client.auth.sign_out()
            return jsonify({"error": "not signed in"})
        
        return jsonify({"message": "signed in"})
    except Exception as e:
        return jsonify({"error": f"{str(e)}"}, 500)


# <supabase._sync.client.SyncClient object at 0x000001EFC069D5E0>
# user=User(id='952c8f64-ffd7-4535-9379-54f27a28d601',
# app_metadata={'provider': 'email', 'providers': ['email']},
# user_metadata={'email': 'fg2303@gmail.com', 'email_verified': False,
# 'phone_verified': False, 'sub': '952c8f64-ffd7-4535-9379-54f27a28d601'},
# aud='authenticated', confirmation_sent_at=datetime.datetime(2025, 4, 19, 22, 49, 11, 662494,
# tzinfo=TzInfo(UTC)), recovery_sent_at=None, email_change_sent_at=None, new_email=None, new_phone=None, invited_at=None,
# action_link=None, email='fg2303@gmail.com', phone='',
# created_at=datetime.datetime(2025, 4, 19, 22, 49, 11, 651968, tzinfo=TzInfo(UTC)), confirmed_at=None,
# email_confirmed_at=None, phone_confirmed_at=None, last_sign_in_at=None, role='authenticated',
# updated_at=datetime.datetime(2025, 4, 19, 22, 49, 13, 719372, tzinfo=TzInfo(UTC)),
# identities=[UserIdentity(id='952c8f64-ffd7-4535-9379-54f27a28d601',
# identity_id='af3ad80a-91cd-4698-9ec1-c2d29bee3d9e', user_id='952c8f64-ffd7-4535-9379-54f27a28d601',
# identity_data={'email': 'fg2303@gmail.com', 'email_verified': False, 'phone_verified': False,
# 'sub': '952c8f64-ffd7-4535-9379-54f27a28d601'}, provider='email',
# created_at=datetime.datetime(2025, 4, 19, 22, 49, 11, 657453, tzinfo=TzInfo(UTC)),
# last_sign_in_at=datetime.datetime(2025, 4, 19, 22, 49, 11, 657402, tzinfo=TzInfo(UTC)),
# updated_at=datetime.datetime(2025, 4, 19, 22, 49, 11, 657453, tzinfo=TzInfo(UTC)))],
# is_anonymous=False, factors=None) session=None
