from functools import wraps

def role_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt() # Get additional data from JWT
            if claims['role'] not in allowed_roles:
                return jsonify({"msg": "Unauthorized role"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Example usage for the Dispatcher UI
@app.route('/api/dispatch/new-trip', methods=['POST'])
@role_required(['Dispatcher', 'Fleet Manager'])
def create_trip():
    # Logic to create trip...
    return jsonify({"msg": "Trip Created"})