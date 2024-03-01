import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = 'http://127.0.0.1:4000/api'; 

  constructor(private http: HttpClient) {}

  registerUser(user: any): Observable<any> {

    const payload = {
      "email" : user.email ,
      "name" : user.name ,
      "password" : user.password ,
      "role" : user.role ,
      "phone_number" : user.phoneNumber

    }
    return this.http.post(`${this.apiUrl}/user`, payload);
  }
}
