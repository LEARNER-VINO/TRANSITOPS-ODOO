@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    # 1. Check if account is already locked
    if user.is_locked:
        return jsonify({"error": "Account locked. Please contact admin."}), 403

    # 2. Check Password
    if check_password_hash(user.password_hash, password):
        # Reset failed attempts on successful login
        user.failed_attempts = 0
        db.session.commit()
        
        access_token = create_access_token(identity={'id': user.id, 'role': user.role})
        return jsonify({
            "token": access_token,
            "role": user.role,
            "message": "Login successful"
        }), 200
    else:
        # 3. Handle Failed Attempt Logic
        user.failed_attempts += 1
        if user.failed_attempts >= 5:
            user.is_locked = True
        
        db.session.commit()
        
        error_msg = "Invalid credentials."
        if user.is_locked:
            error_msg = "Invalid credentials. Account locked after 5 failed attempts."
            
        return jsonify({"error": error_msg}), 401