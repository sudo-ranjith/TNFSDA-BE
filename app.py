from app import app, api
import app.login.view as login_view
import app.Register.view as register_view


api.add_namespace(register_view.register)
api.add_namespace(login_view.login_ns)
api.add_namespace(register_view.register)
api.add_namespace(login_view.login_ns)


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
