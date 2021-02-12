import wretch from "wretch";

export class AuthApi { 
    constructor() {
        console.log("Auth service instance created");
        this.api = wretch()
                    .url("http://localhost:5000/auth")
                    .options({ credentials: 'include' });
        this.refreshCsrfToken = "";
    }

    login(username, password) {
        return this.api.url('/login')
            .post({'username': username, 'password': password})
            .unauthorized((error) => {
                return error;
            })
            .json((response) => {
                this.refreshCsrfToken = response.refresh_csrf_token;
                return response;
            });
    }

    logout() {
        return this.api.url('/logout')
            .post()
            .json((response) => {
                return response;
            }); 
    }

    refresh() {
        return this.api.url('/refresh')
            .headers({'X-CSRF-Token': this.refreshCsrfToken})
            .post()
            .unauthorized((error) => {
                return error;
            })
            .json((response) => {
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
