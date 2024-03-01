import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) {}

  login(email: string, password: string): Observable<any> {
    const loginData = { email, password };
    return this.http.post('http://127.0.0.1:4000/api/login', loginData , { observe: 'response' });
  }

  extractTokenAndRole(response: any): void {
    const token = response.headers.get('Authorization');
    const role = response.body.user.role;
    const user = response.body.user.email ;
    if (token) {
      localStorage.setItem('token', token);
    }

    if (role) {
      sessionStorage.setItem('role', role);
    }
    if (user) {
      sessionStorage.setItem('user' , user);
    }
  }
  logout(): Observable<any> {
    const email = sessionStorage.getItem('user')
    return this.http.get(`http://127.0.0.1:4000/api/logout/${email}`)
  }

}
