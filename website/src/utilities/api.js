import wretch from "wretch";

export class AuthApi { 
    constructor() {
        this.api = wretch()
                    .url("http://localhost:5000/auth")
                    .options({ credentials: 'include' });
        this.refreshCsrfToken = "";
    }

    login(username, password) {
        return this.api.url("/login")
            .post({'username': username, 'password': password})
            .json(response => {
                this.refreshCsrfToken = response.refresh_csrf_token;
                return response;
            });
    }
}

export class UserApi {
    constructor(token) {
        this.api = wretch()
                    .url("http://localhost:5000/api/v1/user")
                    .options({ credentials: 'include' })
        this.accessCsrfToken = token;
    }

    getUser(userId) {
        this.api.url("/" + userId)
            .get()
            .json(response => {
                console.log(response);
            });
    }
}
