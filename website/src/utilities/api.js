import wretch from "wretch";

export class AuthApi { 
    constructor() {
        this.api = wretch().url("http://localhost:5000/auth")
                           .options({ credentials: 'include' }) 
    }

    login(username, password) {
        this.api.url("/login")
            .post({'username': username, 'password': password})
            .json(response => {
                return response;
            });
    }
}

export class UserApi {
    constructor() {
        this.api = wretch().url("http://localhost:5000/user")
                           .options({ credentials: 'include' })
    }

    get_user(user_id) {
        this.api.url("/" + user_id)
            .get()
            .json(response => {
                console.log(response);
            });
    }
}
